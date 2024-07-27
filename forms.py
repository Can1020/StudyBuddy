from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from email_validator import validate_email, EmailNotValidError

class LoginForm(FlaskForm):
    email = StringField('University Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('LOG IN')

    def validate_email(self, email):
        try:
            validate_email(email.data)
            if '@stud' not in email.data:
                raise ValidationError('Please enter your university email address')
        except EmailNotValidError:
            raise ValidationError('Invalid email address')