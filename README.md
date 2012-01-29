# Installation

If you want to set this up on your server, you'll need uwsgi.

## Server configuration:

You'll need to setup a proper uwsgi handler and proxy for your webserver.

### Apache

You'll need `mod_uwsgi` enabled for this configuration to work:

    <Location /terminal/proxy/>
      ProxyPass  http://localhost:4200/
      Order      allow,deny
      Allow      from all
    </Location>
    
    <Location />
      SetHandler   uwsgi-handler
      uWSGISocket  localhost:1973
    </Location>

### nginx

nginx already has uwsgi support:

    location /terminal/proxy {
      rewrite           ^/terminal/proxy/(.*)$ /$1 break;
      proxy_pass        http://localhost:4200;
      proxy_set_header  X-Real-IP $remote_addr;
    }
    
    location / { try_files $uri @webminal; }
    location @webminal {
      include     uwsgi_params;
      uwsgi_pass  localhost:1973;
    }

## Webminal

And run Webminal (from the source directory):

    uwsgi -s 127.0.0.1:1973 -w server:app

## ShellInABox

Then start [ShellInABox](http://code.google.com/p/shellinabox/) (from the source directory again):

    sudo shellinaboxd -s /:LOGIN --disable-ssl \
        -f styles.css:static/shellinabox.css \
        -f ShellInABox.js:static/shell_in_a_box.js \
        --localhost-only -d

Enjoy ;)

# Hacking Instructions

Webminal is coded using the Flask Python microframework and a few extensions (`flask-sqlalchemy`, `flask-wtf`, `flask-mail`, `flask-flatpages` and `wtforms`). You can use `pip` or `easy_install` to install the modules.

## Code structure

All of the serverside code is inside of `server.py`. The syntax is fairly readable.

For instance, this code renders the index page when it is requested:

    @app.route('/')
    def index():
      return render_template('index.html')

A more complex example involving sessions:

    @app.route('/terminal/')
    def terminal():
      if 'user' in session:
        return render_template('terminal.html')
      
      flash('You must be logged in to use the online terminal', category='warning')
      return redirect(url_for('login'))

The `flash()` function sends a message along with the rendered template that will pop up on screen as the colored bar on top. The currently-implemented categories are `message`, `warning`, `error` and `success`.

## Templates

One reason I chose Flask for the backend is because it is very tightly integrated with the Jinja2 templating engine.

Templates are stored in the `templates/` directory and are HTML-like files that support scripting, inheritance, logic, etc.

There is a master `layout.html` template that holds the actual HTML structure, `<head>` tag, the menu, and basically anything that doesn't change from page to page.

Most templates inherit from `layout.html` using this basic code:

    {% extends "layout.html" %}

    {% block title %}Webminal{% endblock title %}

    {% block body %}
      <h2>Welcome to Webminal, the GNU/Linux Online Terminal</h2>
      
      {{ lipsum(20) }}
    {% endblock body %}

The `{% block %}` statements are defined inside of `layout.html`. Anything within a `{% block %}` statement is piped to the respective block in the parent template.

Templates also support logic and many filters. For example, the message flashing code:

      {% for category, message in get_flashed_messages(with_categories=true) %}
        <p class="flash-{{ category }}">{{ message|safe }}</p>
      {% endfor %}

If you want to actually learn Flask, just follow the [basic tutorial](http://flask.pocoo.org/docs/tutorial/) on Flask's website. The API is amazingly well-written as well, so don't be afraid to use it.
