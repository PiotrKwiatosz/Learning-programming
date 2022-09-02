from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label='Nazwa uzytkownika:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Adres email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Haslo:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Powtorz haslo:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Stworz konto!')