from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, InputRequired, Regexp
import bleach
import re

def validate_username(form, field):
    input_email = field.data

    if len(input_email)  > 254:
        raise ValidationError("Email address must not exceed 254 characters")

    if '@' not in input_email:
        raise ValidationError("Invalid Email format")



def validate_password(form, field):
    #no repeated character

    username = form.username.data
    password = field.data
    blacklist = ["Password123$", "Qwerty123!", "Adminadmin1@", "welcome123!"]
    if password.lower() in blacklist:
        raise ValidationError("Invalid Password")
    if password.lower() in username.lower():
        raise ValidationError("Password must not contain the username")

    # no repeated character
    for i in range(0, len(password)):
        if password[i] == password[i + 1] == password[i + 2]:
            raise ValidationError("Password must not be repeated characters")

    # include at least one uppercase letter, one digit, and one special character
    if not re.search(r'[A-Z]', password):
        raise ValidationError('Password must contain at least one uppercase')
    if not re.search(r'[0-9]', password):
        raise ValidationError('Password must contain at least one digit')
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError('Password must contain at least one special character')

def sanitize(user_input):
    safe_html = bleach.clean(
        user_input,
        tags=['b', 'i', 'u', 'em', 'strong', 'p', 'ul', 'ol', 'li', 'br'],
        attributes={'a': ['href', 'title']},
        strip=True
    )

    return safe_html


class Forms(FlaskForm) :
    username = EmailField("Email", validators = [DataRequired(), validate_username])
    password = PasswordField("Password", validators = [DataRequired(), Length(min=10), validate_password])
    bio = TextAreaField("Bio", validators=[DataRequired(), Length(min=3, max=200)])