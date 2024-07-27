import sqlite3
from flask import Flask, render_template, redirect, url_for, request, flash, g
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegistrationForm
from db import get_db, query_db, execute_db, init_db
from models import User
import email_validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, InputRequired, Length, EqualTo
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Example user database
users = {'user1': User(id=1, name='Dzhan Nezhdet', university='HWR', course_of_study='Wirtschaftsinformatik', semester='5', skills='web development', email='s_nezhdet22@stud.hwr-berlin.de', password='password')}

@login_manager.user_loader
def load_user(user_id):
    user_data = query_db('SELECT * FROM user WHERE id = ?', [user_id], one=True)
    if user_data:
        return User(*user_data)
    return None

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

@app.route('/register', methods=['GET', 'POST'])
def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            try:
                execute_db('INSERT INTO user (name, university, course_of_study, semester, skills, email, password) VALUES (?, ?, ?, ?, ?, ?, ?)',
                           [form.name.data, form.university.data, form.course_of_study.data, form.semester.data, form.skills.data, form.email.data, hashed_password])
                flash('Registration successful! Please log in.')
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                flash('Email address already registered')
        return render_template('register.html', form=form)

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user_data = query_db('SELECT * FROM user WHERE email = ?', [email], one=True)


        user = next((u for u in users.values() if u.email == email and u.password == password), None)
        if user_data and check_password_hash(user_data[8], password):
            user = User(*user_data)
            login_user(user)
            return redirect(url_for('welcome'))
        if user:
            if user.email != email:
                flash('Invalid email')
                return redirect(url_for('login'))
            if user.password != password:
                flash('Invalid password')
                return redirect(url_for('login'))
            else:
                flash('Invalid email or password')
                return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/welcome')
@login_required
def welcome():
    return f"Welcome to StudyBuddy, {current_user.email}!"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)