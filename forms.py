import email
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    ValidationError,
    InputRequired,
    Length,
    EqualTo,
    NumberRange,
)
from email_validator import validate_email as email_validator, EmailNotValidError


class LoginForm(FlaskForm):
    email = StringField("University Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("LOG IN")

    def email_validator(self, field):
        try:
            email_validator(field.data)
            if "@stud" not in field.data:
                raise ValidationError("Please enter your university email address")
        except EmailNotValidError:
            raise ValidationError("Invalid email address")


class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired(), Length(min=2, max=50)])
    age = IntegerField("Age", validators=[InputRequired(), NumberRange(min=18)])
    location = StringField(
        "Location", validators=[InputRequired(), Length(min=2, max=100)]
    )
    university = StringField(
        "University", validators=[InputRequired(), Length(min=2, max=100)]
    )
    course_of_study = StringField(
        "Course of Study", validators=[InputRequired(), Length(min=2, max=100)]
    )
    semester = StringField(
        "Semester", validators=[InputRequired(), Length(min=1, max=2)]
    )
    skills = StringField(
        "Skills and Interests", validators=[InputRequired(), Length(min=2, max=200)]
    )
    email = StringField("University Email", validators=[InputRequired(), Email()])
    password = PasswordField(
        "Password", validators=[InputRequired(), Length(min=8, max=100)]
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            InputRequired(),
            EqualTo("password", message="Passwords must match"),
        ],
    )
    submit = SubmitField("Register")

    def validate_email(self, field):
        try:
            email_validator(field.data)
            if "@stud." not in field.data:
                raise ValidationError("Please use your university email address.")
        except EmailNotValidError:
            raise ValidationError("Invalid email address.")


class ForgotPasswordForm(FlaskForm):
    email = StringField("University E-Mail", validators=[DataRequired(), Email()])
    submit = SubmitField("Submit")


class ResetPasswordForm(FlaskForm):
    password = PasswordField(
        "New Password", validators=[DataRequired(), Length(min=8, max=100)]
    )
    confirm_password = PasswordField(
        "Confirm New Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match"),
        ],
    )
    submit = SubmitField("Submit")
