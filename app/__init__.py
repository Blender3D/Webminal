from flask import Flask, url_for, render_template, render_template_string, safe_join, request, flash, redirect, session

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cache import Cache
from flask.ext.flatpages import FlatPages
from flask.ext.security import Security, SQLAlchemyUserDatastore, login_required

app = Flask('webminal')
app.config.from_pyfile('config.py')

pages = FlatPages(app)
db = SQLAlchemy(app)

from app.users.models import User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html'), 403

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(410)
def gone(error):
    return render_template('errors/410.html'), 410

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500