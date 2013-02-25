from flask.ext.security.forms import RegisterForm
from flask.ext.wtf import TextField, Length

from app import user_datastore

class UsernameRegisterForm(RegisterForm):
    username = TextField('Username', validators=[Length(3, 64)])
    
    def validate(self):
        if not super(UsernameRegisterForm, self).validate():
            return False
        
        if user_datastore.find_user(username=self.username.data.strip()):
            self.username.errors.append('This username has already been taken')
            return False
        
        return True