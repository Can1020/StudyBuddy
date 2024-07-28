import sqlite3
from flask import Flask, render_template, redirect, url_for, request, flash, g
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegistrationForm
from db import get_db, query_db, execute_db, init_db, close_connection, init_app
from models import User
import email_validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, InputRequired, Length, EqualTo
from email_validator import validate_email, EmailNotValidError
import logging

db_initialized = False

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

logging.basicConfig(level=logging.DEBUG)

@app.before_request
def initialize_db():
    g.db = get_db()
print("Initializing database")
with app.app_context():
    init_db()

print("Initializing app")
init_app(app)

# Example user database
users = {'user1': User(id=1, name='Dzhan Nezhdet', university='HWR', course_of_study='Wirtschaftsinformatik', semester='5', skills='web development', email='s_nezhdet22@stud.hwr-berlin.de', password='password')}

@login_manager.user_loader
def load_user(user_id):
    user_data = query_db('SELECT * FROM user WHERE id = ?', [user_id], one=True)
    if user_data:
        return User(*user_data)
    return None

@app.teardown_appcontext
def teardown(exception):
    print("Tearing down app context")
    close_connection(exception)

@app.route('/register', methods=['GET', 'POST'])
def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
            try:
                execute_db('INSERT INTO user (name, university, course_of_study, semester, skills, email, password) VALUES (?, ?, ?, ?, ?, ?, ?)',
                           [form.name.data, form.university.data, form.course_of_study.data, form.semester.data, form.skills.data, form.email.data, hashed_password])
                flash('Registration successful! Please log in.', 'success')
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                flash('Email address already registered' 'error')
        return render_template('register.html', form=form)

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user_data = query_db('SELECT * FROM user WHERE email = ?', [email], one=True)
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