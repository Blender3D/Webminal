# -*- coding: utf-8 -*-
import os, re, hashlib, hmac, base64, time, calendar, gevent
import datetime
import stripe
import threading
import subprocess

from flask import Flask, url_for, render_template, render_template_string, \
    safe_join, request, flash, redirect, session, abort, Response

from flask_wtf.csrf import CSRFProtect

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask.ext.mail import Mail, Message
from flask.ext.flatpages import FlatPages, pygments_style_defs, pygmented_markdown
from flask.ext.bcrypt import Bcrypt

from wtforms import Form, TextField, PasswordField, BooleanField, validators,SelectMultipleField,widgets, SelectField
from flask_wtf import FlaskForm as Form,RecaptchaField #--> enable this for recaptchav2

## rq imports
from rq import Connection, Queue, Worker
from redis import Redis

from smtplib import SMTPException
import requests
from urllib import urlencode

import uuid


app = Flask(__name__.split('.')[0])

if os.path.isfile('config.py'):
  app.config.from_pyfile('config.py')
else:
  app.config.from_pyfile('/var/www/webminal/config_default.py')

app.secret_key = os.environ.get('FLASK_SECRET_KEY') or app.config.get('SECRET_KEY', 'CHANGE_ME_IN_CONFIG_PY')
app.debug = app.config.get('DEBUG', False)
RECAPTCHA_PUBLIC_KEY = app.config.get('RECAPTCHA_PUBLIC_KEY', '')
RECAPTCHA_PRIVATE_KEY = app.config.get('RECAPTCHA_PRIVATE_KEY', '')

if app.config['USE_MYSQL']:
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{username}:{password}@{host}/{database}'.format(
    username=app.config['MYSQL_USERNAME'],
    password=app.config['MYSQL_PASSWORD'],
    host=app.config['MYSQL_HOST'],
    database=app.config['MYSQL_DATABASE']
  )
else:
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{path}/database.db'.format(path=os.getcwd())

stripe_keys = {
    'secret_key': os.environ.get('STRIPE_SECRET_KEY', ''),
    'publishable_key': os.environ.get('STRIPE_PUBLISHABLE_KEY', '')
}

stripe.api_key = stripe_keys['secret_key']

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', '')


mail = Mail(app)
bcrypt = Bcrypt(app)
pages = FlatPages(app)
db = SQLAlchemy(app)

# Enforce CSRF protection on all POST/PUT/PATCH/DELETE requests.
# All POST forms render {{ form.csrf_token }} in their templates.
csrf = CSRFProtect(app)


def ratelimit_ok(key, limit, window):
    """Simple Redis-backed per-key rate limiter.

    Returns True if the request is allowed, False if over `limit` within
    `window` seconds. Fails open if Redis is unreachable so a Redis outage
    never locks users out.
    """
    try:
        r = Redis(REDIS_HOST, password=REDIS_PASSWORD)
        rk = "rl:" + key
        current = r.incr(rk)
        if current == 1:
            r.expire(rk, window)
        return current <= limit
    except Exception:
        return True



class RegistrationForm(Form):
  username = TextField('Username', [validators.Regexp(r'^\d*[a-zA-Z][a-zA-Z0-9]*$',message="Name should begin with Alphabet."),validators.Length(min=5, max=14)])
  email = TextField('Email Address', [validators.Email(message='Invalid email address.')])
  
  password = PasswordField('New Password', [
    validators.Required(),
    validators.Regexp(r'^[\w]+$', message="Passwords can only contain alphanumeric "),
    validators.Length(min=5, max=14),
    validators.EqualTo('confirm', message='Passwords must match')
  ])
  
  confirm = PasswordField('Repeat Password')
  accept_tos = BooleanField('I accept the TOS', [validators.Required()])
  # July-2 Fix remove recaptcha from login

class LoginForm(Form):
  username = TextField('Username', [validators.Length(min=4, max=25), validators.Required()])
  password = PasswordField('Password', [validators.Required()])


  # Disable after https://www.taringa.net/posts/ebooks-tutoriales/20143212/Aprende-todo-sobre-la-terminal-de-Linux-de-forma-interactiva.html
  # July-2 Fix remove recaptcha from login

class PricingForm(Form):
  email = TextField('Email Address', [validators.Email(message='Invalid email address.')])

class ResetLoginForm(Form):
  username = TextField('Username', [validators.Length(min=4, max=25)])
  email = TextField('Email Address', [validators.Email(message='Invalid email address.')])

  captcha = RecaptchaField()

class ResetForm(Form):
  username = TextField('Username', [validators.Length(min=4, max=25)])
  email = TextField('Email Address', [validators.Email(message='Invalid email address.')])
  password = PasswordField('New Password', [
    validators.Required(),
    validators.Regexp(r'^[\w]+$', message="Passwords can only contain alphanumeric "),
    validators.Length(min=5, max=14),
    validators.EqualTo('confirm', message='Passwords must match')
  ])
  
  confirm = PasswordField('Repeat Password')

data = [('wmshell','Ubuntu'), ('wmawk','Fedora') ,  ('wmmysql','Slackware'),('wmmail','Arch')]

class ProfileForm(Form):
  example2 = SelectMultipleField(
        'Pick Things!',
        choices=data,
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False)
        )
  example = BooleanField('Drop a mail but don\'t spam!')

class TermForm(Form):
     topics = [(50,'Select'), (100,'Lesson1'), (200,'Lesson2'), (300,'Lesson3'), (400,'Lesson4'), (500,'Lesson5'), (600,'Lesson6'), (700,'Lesson7'), (800,'Lesson8'),(801,'Lesson9'),(802,'Lesson10'),(803,'Lesson11'),(900,'Mysql'),(1000,'ScriptingIntro'),(1001,'ScriptingInputs'),(1002,'ScriptingLoops'),(1003,'ScriptingMisc'),('1004','FindCommandBasics'),('2000','Python'),('3000','date_command'),(3001,'ACL'),(3002,'configure_sudo_access'),(3003,'User_Group_Management')]
     side_course = SelectField(u'side_course', choices=topics)

class ProgTermForm(Form):
     topics = [(50,'Select'), (100,'Python')]
     side_course = SelectField(u'side_course', choices=topics)

class LoginHistory(db.Model):
  __tablename__ = 'LoginHistory'
  uid = db.Column(db.Integer,primary_key=True)
  loginAt = db.Column(db.DateTime)
  userID = db.Column(db.Integer)

  def __init__(self,userID):
    self.loginAt = datetime.datetime.now()
    self.userID = userID

class UserProfile(db.Model):
  __tablename__ = 'UserProfile'
  nickname = db.Column(db.String(40), primary_key=True)
  wmshell  = db.Column(db.Boolean)
  wmawk = db.Column(db.Boolean)
  wmmysql = db.Column(db.Boolean)
  wmreserved = db.Column(db.Boolean)
  wmmail = db.Column(db.Boolean)

  def __init__(self,name):
    self.nickname = name
    self.wmshell  = 1
    self.wmawk = 0
    self.wmmysql = 0
    self.wmreserved = 0
    self.wmmail = 1 

  def __repr__(self):
    return '<UserProfile {username}>'.format(username=self.nickname)



class UserRemap(db.Model):
  __tablename__ = 'UserRemap'
  name = db.Column(db.String(40),primary_key=True)
  email = db.Column(db.String(255))
  password = db.Column(db.String(64))
  flag = db.Column(db.String(1))

  def __init__(self, name, email, password):
    self.email = email
    self.name = name
    self.password = password
    self.flag = 'N'

  def __repr__(self):
    return '<UserRemap {name}>'.format(name=self.name)



class User(db.Model):
  uid = db.Column(db.Integer, primary_key=True)
  nickname = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
  password = db.Column(db.String(128))
  verify_key = db.Column(db.String(16), unique=True)
  verified = db.Column(db.Boolean)
  logins = db.Column(db.Integer)
  joinedOn = db.Column(db.DateTime)
  active = db.Column(db.Boolean)

  lazy_account = db.Column(db.Boolean)
  lazy_verified = db.Column(db.Boolean)


  def __init__(self, username, email, password):
    self.email = email
    self.nickname = username
    self.password = password
    self.verify_key = base64.urlsafe_b64encode(os.urandom(12))
    self.joinedOn = datetime.datetime.now()
    self.logins = 0
    
    self.verified = False
    self.active = False


    self.lazy_account = False
    self.lazy_verified = False

    
  def create_account(self):
    # ADD USER CREATION CODE HERE
    self.set_password(self.password)

  def set_password(self, password):
     self.password = bcrypt.generate_password_hash(password, rounds=13)

  def verify_password(self, password):
     try:
        retval = False
        retval = bcrypt.check_password_hash(self.password, password)
        return retval
     except:
        return retval
  
  def generate_verify_key(self):
    self.verify_key = base64.urlsafe_b64encode(os.urandom(12))
    
    return self.verify_key
  
  def __repr__(self):
    return '<User {username}>'.format(username=self.nickname)


#Distro model
#   ############## New tables #################
class distrodb(db.Model):
    __tablename__ = 'distro'
    did = db.Column(db.Integer, primary_key = True)
    distroname = db.Column(db.String(64), index = True)
    distrovers = db.Column(db.SmallInteger)

    def __repr__(self):
        return '<distrodb %r>' % (self.distroname)

class topic(db.Model):
    __tablename__ = 'topic'
    tid = db.Column(db.Integer, primary_key = True)
    topicname = db.Column(db.String(64))
    timelimit = db.Column(db.SmallInteger)
    catagory = db.Column(db.String(64))

    def __repr__(self):
        return '<topic %r>' % (self.topicname)

class paidtopic(db.Model):
    __tablename__ = 'paidtopic'
    tid = db.Column(db.Integer, primary_key = True)
    topicname = db.Column(db.String(64))
    timelimit = db.Column(db.SmallInteger)
    catagory = db.Column(db.String(64))

    def __repr__(self):
       return '<topic %r>' % (self.topicname)



class SupportedConfig(db.Model):
    __tablename__ = 'SupportedConfig'
    sid = db.Column(db.Integer, primary_key = True)
    did = db.Column(db.Integer)
    tid = db.Column(db.Integer)

    def __repr__(self):
        return '<SupportedConfig %r>' % (self.sid)


class UserCourse(db.Model):
    __tablename__ = 'UserCourse'
    ucid = db.Column(db.Integer, primary_key = True)	
    uid = db.Column(db.Integer)
    sid = db.Column(db.Integer)
    timelimit = db.Column(db.Integer)
    status = db.Column(db.String(64))
    endtime = db.Column(db.Integer)
    starttime = db.Column(db.Integer)
    finitime = db.Column(db.Integer)

    def __init__(self, uid, sid, timelimit, status, endtime, starttime, finitime):
        self.uid = uid
        self.sid = sid
        self.timelimit = timelimit
        self.status = status
	self.endtime = endtime
	self.starttime = starttime
	self.finitime = finitime

    def __repr__(self):
        return '<UserCourse %r>' % (self.uid)


# Web-course progress: lean per-lesson completion, one row per (user, topic).
# Decoupled from the timed Root-Lab UserCourse/SupportedConfig flow.
class LessonProgress(db.Model):
    __tablename__ = 'LessonProgress'
    lpid = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, index=True)
    tid = db.Column(db.Integer, index=True)
    status = db.Column(db.String(16))          # 'in-progress' | 'completed'
    last_accessed = db.Column(db.DateTime)

    def __init__(self, uid, tid, status, last_accessed=None):
        self.uid = uid
        self.tid = tid
        self.status = status
        self.last_accessed = last_accessed

    def __repr__(self):
        return '<LessonProgress uid=%r tid=%r %r>' % (self.uid, self.tid, self.status)


def rot47(s):
    x = []
    for i in xrange(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return re.sub(r'\W+', '',''.join(x))


@app.route('/')
def index():
  return render_template('index.html',counter=get_counter())



@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404

@app.route('/about/')
def about():
  return render_template('about.html')


# category slug -> course presentation. A 'course' is a topic.catagory group.
COURSE_META = [
  ('basics',      {'title': 'Linux Basics',          'icon': u'\U0001F427', 'desc': 'Core commands: ls, cd, cat, grep, find and friends.'}),
  ('scripting',   {'title': 'Shell Scripting',        'icon': u'\U0001F4DC', 'desc': 'Variables, inputs, loops and the find command.'}),
  ('programming', {'title': 'Programming',            'icon': u'\U0001F40D', 'desc': 'Write and run Python in a real Linux environment.'}),
  ('storage',     {'title': 'Storage & Filesystems',  'icon': u'\U0001F5C4', 'desc': 'fdisk, LVM, RAID, XFS, ext4, fsck and mount.'}),
  ('security',    {'title': 'Security & Permissions', 'icon': u'\U0001F510', 'desc': 'ACL, sudo access and user / group management.'}),
  ('tools',       {'title': 'Developer Tools',        'icon': u'\U0001F9F0', 'desc': 'strace, monitoring, git and svn.'}),
  ('database',    {'title': 'Databases',              'icon': u'\U0001F5C3', 'desc': 'MySQL, PostgreSQL and MongoDB practice.'}),
  ('services',    {'title': 'Services',               'icon': u'\U0001F310', 'desc': 'NFS and other network services.'}),
]
COURSE_ORDER = dict((slug, i) for i, (slug, _) in enumerate(COURSE_META))
COURSE_LOOKUP = dict(COURSE_META)


def compute_course_list(uid):
  """Group topics into courses by category and overlay this user's progress."""
  groups = {}
  for t in topic.query.all():
    groups.setdefault(t.catagory or 'other', []).append(t)

  done = set()
  seen = set()
  for lp in LessonProgress.query.filter_by(uid=uid).all():
    seen.add(lp.tid)
    if lp.status == 'completed':
      done.add(lp.tid)

  course_list = []
  for cat, lessons in groups.items():
    meta = COURSE_LOOKUP.get(cat, {'title': cat.title(), 'icon': u'\U0001F4D8', 'desc': ''})
    total = len(lessons)
    completed = sum(1 for l in lessons if l.tid in done)
    touched = any(l.tid in seen for l in lessons)
    pct = int(round(completed * 100.0 / total)) if total else 0
    if total and completed >= total:
      status = 'Completed'
    elif touched or completed:
      status = 'In Progress'
    else:
      status = 'Not started'
    course_list.append({
      'slug': cat, 'title': meta['title'], 'icon': meta['icon'], 'desc': meta['desc'],
      'total': total, 'completed': completed, 'pct': pct, 'status': status,
    })

  course_list.sort(key=lambda c: COURSE_ORDER.get(c['slug'], 99))
  return course_list


@app.route('/courses/')
def courses():
  if 'user' not in session:
    flash('You must be logged in to view courses', category='warning')
    return redirect(url_for('login'))
  course_list = compute_course_list(session.get('uid'))
  active = [c for c in course_list if c['status'] != 'Not started']
  return render_template('courses.html', courses=course_list, active=active,
                         uname=session.get('username'))

@app.route('/sponsors/')
def sponsors():
  return render_template('sponsors.html')


@app.route('/faq/')
def faq():
  return render_template('faq.html')

@app.route('/contact/')
def contact():
  return render_template('contact.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
  if 'user' in session:
    return redirect(url_for('index'))
  form = LoginForm(request.form)
  if request.method == 'POST' and not ratelimit_ok("login:" + str(request.remote_addr), 10, 300):
    flash('Too many attempts. Please wait a few minutes and try again.', category='warning')
    return render_template('login.html', form=form)
  if request.method == 'POST' and form.validate():
    user = User.query.filter_by(nickname=form.username.data).first()
    
    if user:
        if not user.verified:
          flash('Your account has not been verified. Do you want to <a href="{url}">resend the email</a>?'.format(
            url=url_for('resend', verify_key=user.verify_key))
          )
          
          return render_template('login.html', form=form)
        
        if not user.active:
	   userremap=UserRemap.query.filter_by(name=user.nickname,flag='Y').first()

    if user:
      if user.verify_password(form.password.data):
        flash('You have been logged in')
        
        user.logins += 1
        
        db.session.add(LoginHistory(user.uid))
        db.session.commit()
        
        session['user'] = str(user)
	session['username'] = user.nickname
	session['uid'] = user.uid
	session['endtime'] = 0
	session['timeout'] = 0
        session['active'] = user.active
        session['logins']=user.logins

        session['lazy_account'] = user.lazy_account
        session['lazy_verified'] = user.lazy_verified
        session['verify_key'] = user.verify_key
        session['vnc_pass']=base64.urlsafe_b64encode(os.urandom(9))[:12]
        session['joined'] = user.joinedOn.strftime('%B %Y') if user.joinedOn else ''
        try:
            with open('/etc/wmsudo.txt', 'r') as f:
                session['lab_enabled'] = str(session['uid']) in f.read().splitlines()
        except:
            session['lab_enabled'] = False


	#retrieve profile and store them in a session
    	userprofile = UserProfile.query.filter_by(nickname=form.username.data).first()
	if userprofile == None:
    		userprofile = UserProfile(form.username.data)
		db.session.add(userprofile)
        	db.session.commit()
	session['wmshell']=userprofile.wmshell
	session['wmawk']=userprofile.wmawk
	session['wmmysql']=userprofile.wmmysql
	session['wmmail']=userprofile.wmmail
	session['wmreserved']=userprofile.wmreserved

        return redirect(url_for('index'))
    
    flash('Invalid username or password', category='error')
  
  return render_template('login.html', form=form)



@app.route('/logout/')
def logout():
  if 'user' in session:
    username=str(session['username'])
    session.pop('user', None)
    if username != "root" and username != "":
        subprocess.call(["pkill", "-KILL", "-u", username])
    flash('You have been logged out')
  
  return redirect(url_for('index'))


@app.route('/settings/save',methods=['GET','POST'])
def settings_save():
  if 'user' in session:
    form=ProfileForm(request.form)
    if request.method == "POST": #and form.validate():
        flash('Your changes have been saved.')

	if form.example2.data:
	     for item in form.example2.data:
		if "wmshell" in form.example2.data:
			session['wmshell']=True;
		else:
			session['wmshell']=False;
	
		if "wmawk" in form.example2.data:
			session['wmawk']= True;
		else:
			session['wmawk']= False;
		
		if "wmmysql" in form.example2.data:
			session['wmmysql']=True;
		else:
			session['wmmysql']= False;
		if "wmmail" in form.example2.data:
			session['wmmail']=True;
		else:
			session['wmmail']= False;
	else:
			session['wmshell']=False;
			session['wmawk']= False;
			session['wmmysql']= False;
			session['wmmail']= False;
	if form.example.data:
		session['wmreserved']=True;
	else:
		session['wmreserved']=False;
	username=session.get('username')

    	userprofile = UserProfile.query.filter_by(nickname=username).first()
	if userprofile == None:
		flash ("Unable to find record!")
	else:
		userprofile.wmshell=session['wmshell']
		userprofile.wmawk=session['wmawk']
		userprofile.wmmysql=session['wmmysql']
		userprofile.wmmail=session['wmmail']
		userprofile.wmreserved=session['wmreserved']
		#store session values -> db
	        db.session.commit()
	return render_template('settings.html',form = form,usrname=session.get('username'),acc_status=session.get('acc_status'),vnc_pass=session['vnc_pass'],logins=session.get('logins',0),joined=session.get('joined',''),lab_enabled=session.get('lab_enabled',False))


@app.route('/settings/',methods=['GET','POST'])
def settings():
  if 'user' in session:
    username=session.get('username')
    userremap = UserRemap.query.filter_by(name=username,flag='L').first()
    if userremap: 
       if userremap.flag == "L":
             acc_status="Active, Please login."
             session['acc_status']=acc_status
    else:
        acc_status="Inactive, Please wait for 2 minutes and refresh this page."
        session['acc_status']=acc_status

    form=ProfileForm()
    if request.method == "POST":# and form.validate():
        return redirect(url_for('save'))
    else:
	chkbox=[]
	if session.get('wmshell'):
		chkbox.append('wmshell')
	if session.get('wmawk'):
		chkbox.append('wmawk')
	if session.get('wmmysql'):
		chkbox.append('wmmysql')
	if session.get('wmmail'):
		chkbox.append('wmmail')
 	if session.get('wmreserved'):
		form.example.data=session['wmreserved']		
	form.example2.data=chkbox
	return render_template('settings.html',form = form,usrname=username,acc_status=session.get('acc_status'),vnc_pass=session['vnc_pass'],logins=session.get('logins',0),joined=session.get('joined',''),lab_enabled=session.get('lab_enabled',False))
   



@app.route('/register/', methods=['GET', 'POST'])
def register():
  if 'user' in session:
    return redirect(url_for('index'))
  
  form = RegistrationForm(request.form)
  # July-2 Fix remove recaptcha from login
  if request.method == 'POST' and form.validate():
    if User.query.filter_by(nickname=form.username.data).first():
      flash('This username has already been taken', category='warning')
      return render_template('register.html', form=form)
    
    if User.query.filter_by(email=form.email.data).first():
      flash('An account already exists for the email address', category='warning')
      return render_template('register.html', form=form)
    
    user = User(form.username.data, form.email.data, form.password.data)
    userremap = UserRemap(form.username.data, form.email.data, form.password.data)
    user.lazy_account = 1
    user.lazy_verified = 1
    
    db.session.add(user)
    db.session.add(userremap)
    db.session.commit()
    
    message = Message('Webminal Account Verification')
    message.add_recipient(user.email)
    message.sender = 'Administrator <efgadmin@webminal.org>'

    message.html = '''
      Hello {username},

      Welcome to Webminal! Before you can begin using your account, you need to activate it using the below link:

      After verification, please wait for 5minutes then login to your account. Please login using your nickname and 
      remember Webminal terminal username & password is case-sensitive.


      http://www.webminal.org{verify_url}

      Have a nice day,
        The Webminal Team
    '''
    
    message.html = message.html.format(
      username=user.nickname,
      verify_url=url_for('verify', verify_key=user.verify_key)
    )
    subj ='Webminal Account Verification'
    to_addr=user.email
    mail_message = message.html
    d = threading.Thread(name=user.nickname, target=send_simple_message, args=(user.email,subj,mail_message,))
    d.setDaemon(True)
    d.start()
    # ends

    flash('Check your Spambox/Inbox, an email has been sent to "{email}" with a confirmation link.'.format(email=user.email))
    
    return redirect(url_for('login'))
  return render_template('register.html', form=form)

#send mail via smtp
def daemon(message):
    if app.config['MAIL']:
      try:
         mail.send(message)
      except SMTPException as error:
         print "Mail FAILED",error
    else:
      pass

#send mail via mailgun
MAILGUN_URL = os.environ.get('MAILGUN_URL', '')
MAILGUN_AUTH = os.environ.get('MAILGUN_AUTH', '')
FROM_ADDR="webminal bot<noreply@webminal.org>"

def mailgun_send_simple_message(TO_ADDR,SUBJ,MAIL_MESSAGE):
    return requests.post(
	MAILGUN_URL,
	auth=("api",MAILGUN_AUTH),
        data={"from": FROM_ADDR,
              "to": [TO_ADDR],
              "subject": SUBJ,
              "text": MAIL_MESSAGE})

import json
ZEPTO_URL = os.environ.get('ZEPTO_URL', 'https://api.zeptomail.in/v1.1/email')
ZEPTO_AUTH = os.environ.get('ZEPTO_AUTH', '')
def send_simple_message(TO_ADDR, SUBJ, MAIL_MESSAGE):
    payload = {
        "from": {
            "address": "noreply@webminal.org",
            "name": "efgadmin"
        },
        "to": [{
            "email_address": {
                "address": TO_ADDR,
                "name": TO_ADDR.split('@')[0]
            }
        }],
        "subject": SUBJ,
        "textbody": MAIL_MESSAGE
    }
    
    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'authorization': ZEPTO_AUTH
    }
    
    return requests.post(
        ZEPTO_URL,
        data=json.dumps(payload),
        headers=headers
    )
@app.route('/register/verify/<verify_key>/')
def verify(verify_key):
  if 'user' in session:
    return redirect(url_for('index'))
  
  user = User.query.filter_by(verify_key=verify_key, verified=False).first()
  
  if user:
    user.verified = True
    user.create_account()

    userremap = UserRemap.query.filter_by(name=user.nickname,flag='N').first()
    userremap.flag = 'Y'

    db.session.add(userremap)
    db.session.commit()  
    flash('Verified, wait for 5minutes then login. Check your profile for account status.')
    
    return redirect(url_for('login'))
  
  flash('Invalid verify key', category='error')
  return redirect(url_for('index'))

@app.teardown_request
def checkin_db(exc):
    try:
        print "Removing db session."
        db.session.remove()
    except AttributeError:
        pass




@app.route('/login/forgot/', methods=['GET', 'POST'])
def forgot():
  if 'user' in session:
    return redirect(url_for('index'))
  
  form = ResetLoginForm(request.form)

  if request.method == 'POST' and not ratelimit_ok("forgot:" + str(request.remote_addr), 10, 300):
    flash('Too many attempts. Please wait a few minutes and try again.', category='warning')
    return render_template('forgot.html', form=form)
  if request.method == 'POST':
    user = User.query.filter_by(nickname=form.username.data, email=form.email.data).first()
    if not user:
      print "Invalid entry"
      flash('The username or email incorrect')
      return render_template('forgot.html', form=form)

    if not user.verified:
      flash('Please verify your account first before resetting password')
      return render_template('forgot.html', form=form)
    
    message = Message('Webminal Account Password Reset')
    message.add_recipient(user.email)
    message.sender = 'Administrator <efgadmin@webminal.org>'
    
    message.html = '''
      Hello {username},

      You recently requested a password reset. Click the link below to reset your password:

      http://www.webminal.org{reset_url}

        Have a nice day,

        The Webminal Team
    '''
    user.verify_key = user.generate_verify_key() 
    message.html = message.html.format(
      username=user.nickname,
      reset_url=url_for('reset', verify_key=user.verify_key)
    )
    db.session.commit()

    subj ='Webminal Account Password Reset'
    to_addr=user.email
    mail_message = message.html
    d = threading.Thread(name=user.nickname, target=send_simple_message, args=(user.email,subj,mail_message,))
    d.setDaemon(True)
    d.start()
    
    flash('An email with reset instructions has been sent to your email address')
    return redirect(url_for('index'))
  
  return render_template('forgot.html', form=form)



@app.route('/register/reset/<verify_key>/', methods=['GET', 'POST'])
def reset(verify_key):
  if 'user' in session:
    return redirect(url_for('index'))
  
  form = ResetForm(request.form)

  if request.method == 'POST' and not ratelimit_ok("reset:" + str(request.remote_addr), 10, 300):
    flash('Too many attempts. Please wait a few minutes and try again.', category='warning')
    return render_template('reset.html', form=form, verify_key=verify_key)
  if request.method == 'POST' and form.validate():
    user = User.query.filter_by(nickname=form.username.data, email=form.email.data, verify_key=verify_key).first()

    if not user:
      flash('The username or email incorrect')
      return render_template('reset.html', form=form, verify_key=verify_key)
    
    user.generate_verify_key()
    user.set_password(form.password.data)

    userremap = UserRemap.query.filter_by(name=user.nickname, email=user.email).first()
    if userremap:
      userremap.password = form.password.data
      userremap.flag = 'P'
    else:
      userremap = UserRemap(user.nickname, user.email, form.password.data)
      userremap.flag = 'P'
      db.session.add(userremap)
    db.session.commit()
    
    flash('Your password has been reset.Please login after 2 minutes.')
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
    message.sender = 'Administrator <efgadmin@webminal.org>'
    
    message.html = '''
      <p>Hello {username},</p>

      <p>You recently requested a new account verification link. Click the link below to verify your account:</p>
      <p><a href="http://www.webminal.org{verify_url}">Webminal Account Re-Verification URL</a></p>

      <p>
        Have a nice day,
        <br />
        The Webminal Team
      </p>
    '''
    
    message.html = message.html.format(
      username=user.nickname,
      verify_url=url_for('verify', verify_key=user.generate_verify_key())
    )
    
    db.session.commit()

    subj ='Webminal Account Verification'
    to_addr=user.email
    mail_message = message.html
    d = threading.Thread(name=user.nickname, target=send_simple_message, args=(user.email,subj,mail_message,))
    d.setDaemon(True)
    d.start()
    
    return render_template('resend.html', message='A new verification link was sent to your registered email')
  
  return render_template('index.html',counter=get_counter())  

DISCOURSE_SSO_SECRET = os.environ.get('DISCOURSE_SSO_SECRET', '')

@app.route('/sso/discourse/')
def discourse_sso():
    from urlparse import parse_qs
    if 'user' not in session:
        return redirect(url_for('login'))
    payload = request.args.get('sso', '')
    sig = request.args.get('sig', '')
    expected_sig = hmac.new(DISCOURSE_SSO_SECRET, payload, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(str(sig), str(expected_sig)):
        abort(403)
    decoded = base64.b64decode(payload)
    params = parse_qs(decoded)
    nonce = params['nonce'][0]
    user = User.query.filter_by(nickname=session['username']).first()
    response_params = urlencode({
        'nonce': nonce,
        'email': user.email,
        'external_id': str(session['uid']),
        'username': session['username'],
        'name': session['username'],
    })
    response_payload = base64.b64encode(response_params)
    response_sig = hmac.new(DISCOURSE_SSO_SECRET, response_payload, hashlib.sha256).hexdigest()
    return redirect('https://community.webminal.org/session/sso_login?sso=' + response_payload + '&sig=' + response_sig)

# Lab view - open to all logged-in users
# Distro view (legacy)
@app.route('/terminal/')
def terminal():
  if 'user' in session:

    form = TermForm(request.form)
    username=session.get('username')
    return render_template('terminal.html',form=form,uname=username)
  
  flash('You must have an account to use the online terminal', category='warning')
  return redirect(url_for('register'))


def get_counter():
    try:
        with open(".counter", 'r') as file:
            counter = int(file.read().strip())
    except (IOError, OSError, ValueError):
        counter = 0
    return counter

@app.route('/help/<command>/')
def help_command(command):
  return redirect(url_for('help_command_full', command=command))


@app.route('/live/')
def live():
  return render_template('live.html', counter=get_counter())

@app.route('/funding.json')
def funding_json():
  fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'funding.json')
  if not os.path.exists(fpath):
    fpath = 'funding.json'
  with open(fpath, 'r') as f:
    return Response(f.read(), mimetype='application/json')

@app.route('/api/live/')
def live_cmds():
  live_path = '.live_cmds'
  if not os.path.exists(live_path):
    return Response('', mimetype='text/plain')
  with open(live_path, 'r') as f:
    return Response(f.read(), mimetype='text/plain')

@app.route('/api/tutorial/<course>/')
def tutorial_json(course):
  import re
  if not re.match(r'^[a-zA-Z0-9_]+$', course):
    abort(404)
  json_path = os.path.join('templates', 'tutorialjson_files', 'centos', course + '.json')
  if not os.path.exists(json_path):
    abort(404)
  with open(json_path, 'r') as f:
    return Response(f.read(), mimetype='text/plain')

@app.route('/help/<command>/plain/')
def help_command_plain(command):
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



@app.route('/golf/')
def golf():
  return render_template('golf.html')

@app.route('/golf/leaderboard/')
def golf_leaderboard():
  return render_template('golf_leaderboard.html')

if __name__ == '__main__':
  app.run()
