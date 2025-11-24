from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, InputRequired, Regexp
# import bleach
# import re

def validate_email(form, field):
    pass

def validate_password(form, field):
    pass

def validate_bio(form, field):
    pass


class forms(FlaskForm) :
    username = EmailField("Email", validators = [DataRequired(), validate_email])
    password = PasswordField("Password", validators = [DataRequired(), validate_password])
    bio = TextAreaField("Bio", validators=[DataRequired(), validate_bio])