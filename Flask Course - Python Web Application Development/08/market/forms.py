from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label='Nazwa uzytkownika:')
    email_address = StringField(label='Adres Email:')
    password1 = PasswordField(label='Haslo:')
    password2 = PasswordField(label='Powtorz haslo:')
    submit = SubmitField(label='Stworz konto!')