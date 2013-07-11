import wtforms as wtf
from wtforms import validators, Form, TextField, PasswordField, ValidationError

from .models import User, DBSession


class FormReg(Form):
    def validate_login(form, field):
        log = DBSession.query(User).filter(User.name == field.data).first()
        if log is not None:
            raise ValidationError("This login is not available")
    login = TextField('Login', [validators.Length(min=4, max=25)])
    pass1 = PasswordField('New Password', [
        validators.Required(),
        validators.Length(min=6, max=35),
        validators.EqualTo('pass2', message='Passwords must match')
    ])
    pass2 = PasswordField('Repeat Password')


class FormLog(Form):
    def validate_login(form, field):
        log = DBSession.query(User).filter(User.name == field.data).first()
        if log is None:
            raise ValidationError("Wrong login")

    def validate_pass1(form, field):
        log = DBSession.query(User).filter(User.name == form.login.data)\
            .filter(User.password == field.data).first()
        if log is None:
            raise ValidationError("Wrong password")
    login = TextField('Login', [validators.Length(min=4, max=25)])
    pass1 = PasswordField('Password', [
        validators.Required(),
        validators.Length(min=6, max=35)
    ])
