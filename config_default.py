# -*- coding: utf-8 -*-
#
# Webminal default configuration -- placeholders only.
# Real values belong in config.py (gitignored) OR environment variables.
#
# Pattern: config_default.py is checked into git with safe placeholders.
#          Create config.py alongside it (or export env vars) to override.
#

FLATPAGES_ROOT = '/var/www/webminal/templates/help'
FLATPAGES_EXTENSION = '.md'
FLATPAGES_AUTO_RELOAD = True

SECRET_KEY = 'CHANGE_ME_IN_CONFIG_PY'
DEBUG = False

RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''

SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL = False
MAIL_USE_TLS = True
MAIL_SERVER = ''
MAIL_USE_SSL = False
MAIL_USERNAME = ''
MAIL_PASSWORD = ''

USE_MYSQL = True
MYSQL_HOST = 'localhost'
MYSQL_USERNAME = ''
MYSQL_PASSWORD = ''
MYSQL_DATABASE = 'Webminal'

# Google Analytics tracking ID (e.g. 'UA-XXXXXXXX-X' or 'G-XXXXXXXXXX').
# Leave empty to disable analytics. Country-level traffic stats only — no
# individual user tracking. Set in config.py for production.
GOOGLE_ANALYTICS_ID = ''
