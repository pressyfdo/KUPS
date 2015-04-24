from flask.ext.wtf import Form 
from wtforms.fields import TextField, PasswordField, BooleanField, SubmitField
from flask.ext.wtf import validators
from wtforms.validators import ValidationError,DataRequired,Required,Email
from models import User

class LoginForm(Form):
    username = TextField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class RegistrationForm(Form):
    fullname = TextField('Full Name', validators=[Required('Please enter your fullname')])
    username = TextField('Username', validators=[Required('Please enter username')])
    email = TextField('Email', validators=[Required('Please enter email address'),Email('Please enter email address')])
    mobile = TextField('Mobile no.')
    submit = SubmitField('create account')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append('That email is already taken')
            return False
        else:
            return True

class ChangePasswordForm(Form):
    old_password = PasswordField('old_password', validators=[DataRequired()])
    new_password = PasswordField('new_password', validators=[DataRequired()])
    password_again = PasswordField('password_again', validators=[DataRequired()])
    submit = SubmitField('Change Password')
