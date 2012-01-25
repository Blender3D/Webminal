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
