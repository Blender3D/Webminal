#!/usr/bin/env python2
from flup.server.fcgi import WSGIServer
from server import app

if __name__ == '__main__':
  app.secret_key = '\x9a\xa7A\xd0\xd2\xa5\x01v\x1d]\xb3\xc32\x9f\xd1nB)m\xc8\xa1\xf0\xf3\x1f' # REPLACE ME WHEN RELEASING
  #app.debug = True

  WSGIServer(app, bindAddress='/tmp/webminal-fcgi.sock').run()
