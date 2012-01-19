import os, re, hashlib, base64, httplib

from flask import Flask, url_for, render_template, request, flash, redirect, session
from flaskext.sqlalchemy import SQLAlchemy
from flaskext.mail import Mail, Message

from werkzeug.datastructures import Headers

from wtforms import Form, TextField, PasswordField, BooleanField, validators

app = Flask(__name__.split('.')[0])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{path}/database.db'.format(path=os.getcwd())
mail = Mail(app)

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



class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
  password = db.Column(db.String(120))
  verify_key = db.Column(db.String(12), unique=True)
  verified = db.Column(db.Boolean)
  

  def __init__(self, username, email, password):
    self.email = email
    self.username = username
    self.password = password
    self.verify_key = base64.urlsafe_b64encode(os.urandom(12))
    self.verified = False
    
  def createAccount(self):
    print ' * Creating user "{username}".'.format(username=self.username)
    # ADD USER CREATION CODE HERE
    self.password = hashlib.sha512(
      hashlib.sha512(self.username).hexdigest() + 
      hashlib.sha512(self.password).hexdigest() + 
      hashlib.sha512(self.email).hexdigest()
    ).hexdigest()
    
  def __repr__(self):
    return '<User {username}>'.format(username=self.username)



@app.route('/')
def index():
  return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
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
          flash('Your account has not been verified. Do you want to <a href="{url}">resend the email</a>'.format(
            url=url_for('resend', verify_key=user.verify_key))
          )
          
          return render_template('login.html', form=form)
        
        session['user'] = user
        
        flash('You have been logged in')
        
        return redirect(url_for('index'))
    
    flash('Invalid username or password')
  
  return render_template('login.html', form=form)



@app.route('/logout')
def logout():
  session.pop('user', None)
  return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
  if 'user' in session:
    return redirect(url_for('index'))
  
  form = RegistrationForm(request.form)
  
  if request.method == 'POST' and form.validate():
    if User.query.filter_by(username=form.username.data).first():
      flash('This username has already been taken')
      return render_template('register.html', form=form)
    
    if User.query.filter_by(email=form.email.data).first():
      flash('An account already exists for the email address')
      return render_template('register.html', form=form)
    
    user = User(form.username.data, form.email.data, form.password.data)
    
    db.session.add(user)
    user.createAccount()
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
    
    mail.send(message)
    
    flash('Thanks for registering. A email has been sent to "{email}" with a confirmation link.'.format(email=user.email))
    
    return redirect(url_for('login'))
  
  return render_template('register.html', form=form)



@app.route('/register/verify/<verify_key>')
def verify(verify_key):
  if 'user' in session:
    return redirect(url_for('index'))
  
  user = User.query.filter_by(verify_key=verify_key, verified=False).first()
  
  if user:
    user.verified = True
    db.session.commit()  
    
    flash('Your account has been verified')
    
    return redirect(url_for('login'))
  return render_template('index.html')
  


@app.route('/register/reset/<verify_key>')
def reset(username):
  user = User.query.filter_by(verify_key=verify_key).first()
  
  if user:
    return render_template('reset.html')
    
  return render_template('index.html')  



@app.route('/register/resend/<verify_key>')
def resend(username):
  user = User.query.filter_by(verify_key=verify_key).first()
  
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
      verify_url=url_for('verify', verify_key=user.verify_key)
    )
    
    mail.send(message)
    
    return render_template('resend.html')
  return render_template('index.html')  



@app.route('/terminal')
def terminal():
  if 'user' in session:
    return render_template('terminal.html')
  
  flash('You must be logged in to use the online terminal')
  return redirect(url_for('login'))



if __name__ == '__main__':
  app.secret_key = '\x9a\xa7A\xd0\xd2\xa5\x01v\x1d]\xb3\xc32\x9f\xd1nB)m\xc8\xa1\xf0\xf3\x1f' # REPLACE ME WHEN RELEASING
  app.debug = True
  app.run()
