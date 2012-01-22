import os, sys
from server import app as application

application.secret_key = '\x9a\xa7A\xd0\xd2\xa5\x01v\x1d]\xb3\xc32\x9f\xd1nB)m\xc8\xa1\xf0\xf3\x1f' # REPLACE ME WHEN RELEASING
application.debug = True
