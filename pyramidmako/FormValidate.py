import wtforms as wtf
from wtforms import validators, Form, TextField, PasswordField, ValidationError

from .models import User, DBSession


class FormReg(Form):
    login = TextField('Login', [validators.Length(min=4, max=25)])
    pass1 = PasswordField('New Password', [
        validators.Required(),
        validators.Length(min=6, max=35),
        validators.EqualTo('pass2', message='Passwords must match')
    ])
    pass2 = PasswordField('Repeat Password')

    def validate_register(form, field):
        login_check = DBSession.query(User).filter(User.name == field.data).first()
        if login_check is not None:
            raise ValidationError("This login is not available")


class FormLog(Form):
    login = TextField('Login', [validators.Length(min=4, max=25)])
    pass1 = PasswordField('Password', [
        validators.Required(),
        validators.Length(min=6, max=35)
    ])

    def validate_login(form, field):
        login = DBSession.query(User).filter(User.name == field.data).first()
        if login is None:
            raise ValidationError("Wrong login or password")

    def validate_pass1(form, field):
        pas = DBSession.query(User).filter(User.name == form.login.data)\
            .filter(User.password == field.data).first()
        if pas is None:
            raise ValidationError("Wrong login or password")