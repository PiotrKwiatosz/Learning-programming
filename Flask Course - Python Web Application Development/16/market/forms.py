from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Uzytkownik aktualnie istnieje! Prosze sprobuj inna nazwe uzytkownika')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Adres email aktualnie istnieje! Prosze sprobuj inny adres email')


    username = StringField(label='Nazwa uzytkownika:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Adres email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Haslo:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Powtorz haslo:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Stworz konto!')

class LoginForm(FlaskForm):
    username = StringField(label='Uzytkownik:', validators=[DataRequired()])
    password = PasswordField(label='Haslo:', validators=[DataRequired()])
    submit = SubmitField(label='Zaloguj sie!')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Kup!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sprzedaj!')