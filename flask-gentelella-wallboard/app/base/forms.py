from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField

## login and registration


class LoginForm(FlaskForm):
    username = TextField('Usuario', id='username_login')
    password = PasswordField('Contraseña', id='pwd_login')


class CreateAccountForm(FlaskForm):
    username = TextField('Usuario', id='username_create')
    email = TextField('Email')
    password = PasswordField('Contraseña', id='pwd_create')
