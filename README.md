If you want to set this up on your server, you'll need uwsgi.

Add this to Apache's config (after installing uwsgi):

    <Location />
      SetHandler uwsgi-handler
      uWSGISocket 127.0.0.1:1973
    </Location>

And run Webminal (from the source directory):

    uwsgi -s 127.0.0.1:1973 -w server:app

Then start SIAB (from the source directory again):

    sudo shellinaboxd -s /:LOGIN --disable-ssl -f styles.css:static/shellinabox.css -f ShellInABox.js:static/shell_in_a_box.js --localhost-only -d

My config assumes that you have this mapping:

    localhost:4200 -> localhost/terminal/proxy/

Enjoy ;)
