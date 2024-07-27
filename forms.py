from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, InputRequired, Length, EqualTo
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
        
class RegistrationForm(FlaskForm):
        name = StringField('Name', validators=[InputRequired(), Length(min=2, max=50)])
        university = StringField('University', validators=[InputRequired(), Length(min=2, max=100)])
        course_of_study = StringField('Course of Study', validators=[InputRequired(), Length(min=2, max=100)])
        semester = StringField('Semester', validators=[InputRequired(), Length(min=1, max=2)])
        skills = StringField('Skills and Interests', validators=[InputRequired(), Length(min=2, max=200)])
        email = StringField('University Email', validators=[InputRequired(), Email()])
        password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=100)])
        confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password', message='Passwords must match')])
        submit = SubmitField('Register')