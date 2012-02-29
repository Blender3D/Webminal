import os, re, hashlib, base64, time
from datetime import datetime

from flask import Flask, url_for, render_template, render_template_string, safe_join, request, flash, redirect, session

from flaskext.sqlalchemy import SQLAlchemy
from flaskext.mail import Mail, Message
from flaskext.flatpages import FlatPages, pygments_style_defs, pygmented_markdown

from wtforms import Form, TextField, PasswordField, BooleanField, validators

app = Flask(__name__.split('.')[0])

app.secret_key = '\x9a\xa7A\xd0\xd2\xa5\x01v\x1d[\xb3\xc32\x9f\xd1nB)m\xc8\xa1\xf0\xf3\x1f'
app.debug = True

if os.path.isfile('config.py'):
  app.config.from_pyfile('config.py')
else:
  app.config.from_pyfile('config_default.py')

if app.config['USE_MYSQL']:
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{username}:{password}@{host}/{database}'.format(
    username=app.config['MYSQL_USERNAME'],
    password=app.config['MYSQL_PASSWORD'],
    host=app.config['MYSQL_HOST'],
    database=app.config['MYSQL_DATABASE']
  )
else:
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{path}/database.db'.format(path=os.getcwd())

mail = Mail(app)
pages = FlatPages(app)
db = SQLAlchemy(app)



class RegistrationForm(Form):
  username = TextField('Username', [validators.Length(min=4, max=25)])
  email = TextField('Email Address', [validators.Length(min=6, max=35)])
  
  password = PasswordField('New Password', [
    validators.Required(),
    validators.EqualTo('confirm', message='Passwords must match')
  ])
  
  confirm = PasswordField('Repeat Password')
  accept_tos = BooleanField('I accept the TOS', [validators.Required()])



class LoginForm(Form):
  username = TextField('Username', [validators.Length(min=4, max=25), validators.Required()])
  password = PasswordField('Password', [validators.Required()])



class ResetLoginForm(Form):
  username = TextField('Username', [validators.Length(min=4, max=25)])
  email = TextField('Email Address', [validators.Length(min=6, max=35)])



class ResetForm(Form):
  username = TextField('Username', [validators.Length(min=4, max=25)])
  email = TextField('Email Address', [validators.Length(min=6, max=35)])
  password = PasswordField('New Password', [
    validators.Required(),
    validators.EqualTo('confirm', message='Passwords must match')
  ])
  
  confirm = PasswordField('Repeat Password')



class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
  password = db.Column(db.String(128))
  verify_key = db.Column(db.String(12), unique=True)
  verified = db.Column(db.Boolean)
  num_logins = db.Column(db.Integer)
  joined_on = db.Column(db.DateTime)
  activated = db.Column(db.Boolean)

  def __init__(self, username, email, password):
    self.email = email
    self.username = username
    self.password = password
    self.verify_key = base64.urlsafe_b64encode(os.urandom(12))
    self.joined_on = datetime.now()
    self.num_logins = 0
    
    self.verified = False
    self.activated = False
    
  def create_account(self):
    # ADD USER CREATION CODE HERE
    self.set_password(self.password)
  
  def set_password(self, password):
    self.password = hashlib.sha512(
      hashlib.sha512(self.username).hexdigest() + 
      hashlib.sha512(password).hexdigest() + 
      hashlib.sha512(self.email).hexdigest()
    ).hexdigest()
  
  def generate_verify_key(self):
    self.verify_key = base64.urlsafe_b64encode(os.urandom(12))
    
    return self.verify_key
  
  def __repr__(self):
    return '<User {username}>'.format(username=self.username)



@app.route('/')
def index():
  return render_template('index.html')



@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404



@app.route('/login/', methods=['GET', 'POST'])
def login():
  if 'user' in session:
    return redirect(url_for('index'))
  
  form = LoginForm(request.form)
  
  if request.method == 'POST' and form.validate():
    user = User.query.filter_by(username=form.username.data).first()
    
    if user:
      password_hash = hashlib.sha512(
        hashlib.sha512(user.username).hexdigest() + 
        hashlib.sha512(form.password.data).hexdigest() + 
        hashlib.sha512(user.email).hexdigest()
      ).hexdigest()
      
      if password_hash == user.password:
        if not user.verified:
          flash('Your account has not been verified. Do you want to <a href="{url}">resend the email</a>?'.format(
            url=url_for('resend', verify_key=user.verify_key))
          )
          
          return render_template('login.html', form=form)
        
        if not user.activated:
          flash('Please try again in a few minutes. Our admin is rushing to create an account for you!', category='error')
          
          return render_template('login.html', form=form)
        
        flash('You have been logged in')
        session['user'] = user
        
        return redirect(url_for('index'))
    
    flash('Invalid username or password', category='error')
  
  return render_template('login.html', form=form)



@app.route('/logout/')
def logout():
  if 'user' in session:
    session.pop('user', None)
    flash('You have been logged out')
  
  return redirect(url_for('index'))


@app.route('/register/', methods=['GET', 'POST'])
def register():
  if 'user' in session:
    return redirect(url_for('index'))
  
  form = RegistrationForm(request.form)
  
  if request.method == 'POST' and form.validate():
    if User.query.filter_by(username=form.username.data).first():
      flash('This username has already been taken', category='warning')
      return render_template('register.html', form=form)
    
    if User.query.filter_by(email=form.email.data).first():
      flash('An account already exists for the email address', category='warning')
      return render_template('register.html', form=form)
    
    user = User(form.username.data, form.email.data, form.password.data)
    
    db.session.add(user)
    db.session.commit()
    
    message = Message('Webminal Account Verification')
    message.add_recipient(user.email)
    message.sender = 'Administrator <admin@webminal.org>'
    
    message.html = '''
      <p>Hello {username},</p>

      <p>Welcome to Webminal! Before you can begin using your account, you need to activate it using the below link:</p>

      <p><a href="{verify_url}">{verify_url}</a></p>

      <p>
        Have a nice day,
        <br />
        The Webminal Team
      </p>
    '''
    
    message.html = message.html.format(
      username=user.username,
      verify_url=url_for('verify', verify_key=user.verify_key)
    )
    
    if app.config['MAIL']:
      mail.send(message)
    else:
      print message.html
    
    flash('Thanks for registering. A email has been sent to "{email}" with a confirmation link.'.format(email=user.email))
    
    return redirect(url_for('login'))
  return render_template('register.html', form=form)



@app.route('/register/verify/<verify_key>/')
def verify(verify_key):
  if 'user' in session:
    return redirect(url_for('index'))
  
  user = User.query.filter_by(verify_key=verify_key, verified=False).first()
  
  if user:
    user.verified = True
    user.create_account()
    db.session.commit()  
    
    flash('Your account has been verified')
    
    return redirect(url_for('login'))
  
  flash('Invalid verify key', category='error')
  return redirect(url_for('index'))



@app.route('/login/forgot/', methods=['GET', 'POST'])
def forgot():
  if 'user' in session:
    return redirect(url_for('index'))
  
  form = ResetLoginForm(request.form)
  
  if request.method == 'POST' and form.validate():
    user = User.query.filter_by(username=form.username.data, email=form.email.data).first()
    
    if not user:
      flash('The username or email incorrect')
      return render_template('forgot.html', form=form)
    
    message = Message('Webminal Account Password Reset')
    message.add_recipient(user.email)
    message.sender = 'Administrator <admin@webminal.org>'
    
    message.html = '''
      <p>Hello {username},</p>

      <p>You recently requested a password reset. Click the link below to reset your password:</p>

      <p><a href="{reset_url}">{reset_url}</a></p>

      <p>
        Have a nice day,
        <br />
        The Webminal Team
      </p>
    '''
    
    message.html = message.html.format(
      username=user.username,
      reset_url=url_for('reset', verify_key=user.generate_verify_key())
    )
    
    db.session.commit()
    
    if app.config['MAIL']:
      mail.send(message)
    else:
      print message.html
    
    flash('An email with reset instructions has been sent to your email address')
    return redirect(url_for('index'))
  
  return render_template('forgot.html', form=form)



@app.route('/register/reset/<verify_key>/', methods=['GET', 'POST'])
def reset(verify_key):
  if 'user' in session:
    return redirect(url_for('index'))
  
  form = ResetForm(request.form)
  
  if request.method == 'POST' and form.validate():
    user = User.query.filter_by(username=form.username.data, email=form.email.data, verify_key=verify_key).first()
    
    if not user:
      flash('The username or email incorrect')
      return render_template('reset.html', form=form, verify_key=verify_key)
    
    user.generate_verify_key()
    user.set_password(form.password.data)
    db.session.commit()
    
    flash('Your password has been reset')
    return redirect(url_for('login'))
    
  return render_template('reset.html', form=form, verify_key=verify_key)



@app.route('/register/resend/<verify_key>/')
def resend(verify_key):
  user = User.query.filter_by(verify_key=verify_key).first()
  
  if not user:
    return render_template('resend.html', message='Your verification key is invalid')
  
  if user and not user.verified:
    message = Message('Webminal Account Re-Verification')
    message.add_recipient(user.email)
    message.sender = 'Administrator <admin@webminal.org>'
    
    message.html = '''
      <p>Hello {username},</p>

      <p>You recently requested a new account verification link. Click the link below to verify your account:</p>

      <p><a href="{verify_url}">{verify_url}</a></p>

      <p>
        Have a nice day,
        <br />
        The Webminal Team
      </p>
    '''
    
    message.html = message.html.format(
      username=user.username,
      verify_url=url_for('verify', verify_key=user.generate_verify_key())
    )
    
    db.session.commit()
    
    if app.config['MAIL']:
      mail.send(message)
    else:
      print message.html
    
    return render_template('resend.html', message='A new verification link was sent to your registered email')
  
  return render_template('index.html')  



@app.route('/terminal/')
def terminal():
  if 'user' in session:
    return render_template('terminal.html')
  
  flash('You must be logged in to use the online terminal', category='warning')
  return redirect(url_for('login'))



@app.route('/help/<command>/')
def help_command(command):
  return redirect(url_for('help_command_full', command=command))


@app.route('/help/<command>/plain/')
def help_command_plain(command):
  time.sleep(1)
  content = pages.get(command)
  
  if not content:
    return render_template('help_plain.html', content=pages.get('404'))
  
  return render_template('help_plain.html', content=content)


@app.route('/help/<command>/full/')
def help_command_full(command):
  content = pages.get(command)
  
  if not content:
    return render_template('404.html'), 404
  
  return render_template('help_full.html', content=content)



if __name__ == '__main__':
  app.run()
