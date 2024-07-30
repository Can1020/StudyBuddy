from math import e
import sqlite3
from flask import Flask, jsonify, render_template, redirect, url_for, request, flash, g
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db, query_db, execute_db, init_db, close_connection, init_app
from models import User
import email_validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError, InputRequired, Length, EqualTo, NumberRange
from email_validator import validate_email, EmailNotValidError
import logging
from forms import ForgotPasswordForm, ResetPasswordForm, LoginForm, RegistrationForm
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
import os
from datetime import datetime, timedelta
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask import session
import random

db_initialized = False

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['DATABASE'] = 'database.db'
login_manager = LoginManager(app)
login_manager.login_view = 'login'
socketio = SocketIO(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'studywithyourbuddy0@gmail.com'
app.config['MAIL_PASSWORD'] = 'uaon kvfy hemv nhsz'
app.config['MAIL_DEFAULT_SENDER'] = 'studywithyourbuddy0@gmail.com'

mail = Mail(app)

s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

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
users = {'user1': User(id=1, name='Dzhan Nezhdet', age = '23', location = 'Berlin', university='HWR', course_of_study='Wirtschaftsinformatik', semester='5', skills='web development', email='s_nezhdet22@stud.hwr-berlin.de', password='password')}

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

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        email = form.email.data
        user = query_db('SELECT * FROM user WHERE email = ?', [email], one=True)
        if user:
            token = s.dumps(email, salt='email-confirm')
            expires_at = datetime.utcnow() + timedelta(minutes=15)
            execute_db('INSERT INTO password_reset (email, token, expires_at) VALUES (?, ?, ?)', [email, token, expires_at])

            msg = Message('Password Reset Request', sender='studywithyourbuddy0@gmail.com', recipients=[email])
            link = url_for('reset_password', token=token, _external=True)
            msg.body = f'Your password reset link is {link}'
            mail.send(msg)

            flash('Check your email for the instructions to reset your password', 'info')
        else:
            flash('Invalid email address', 'danger')
    return render_template('forgot_password.html', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
    except:
        flash('The reset link is invalid or has expired', 'danger')
        return redirect(url_for('forgot_password'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        execute_db('UPDATE user SET password = ? WHERE email = ?', [hashed_password, email])
        execute_db('DELETE FROM password_reset WHERE email = ?', [email])

        flash('Your password has been updated!', 'success')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
            try:
                execute_db('INSERT INTO user (name, age, location, university, course_of_study, semester, skills, email, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                [form.name.data, int(form.age.data), form.location.data, form.university.data, form.course_of_study.data, form.semester.data, form.skills.data, form.email.data, hashed_password])
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

        if user_data:
            is_password_correct = check_password_hash(user_data['password'], password)

            if is_password_correct:
                user = User(*user_data.values())
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
    users = query_db('SELECT name, age, location, university, location, course_of_study, semester, skills FROM user WHERE id != ?', [current_user.id])
    matches= query_db('SELECT * FROM matches WHERE user1_id = ? OR user2_id = ?', [current_user.id, current_user.id])
    random.shuffle(users)
    return render_template('welcome.html', users=users, current_user=current_user, matches=matches)

@app.route('/like', methods=['POST'])
@login_required
def like_user():
    data = request.get_json()
    liked_user_id = data['liked_user_id']

    # Check if a match already exists
    match_exists = query_db('SELECT * FROM matches WHERE (user1_id = ? AND user2_id = ?) OR (user1_id = ? AND user2_id = ?)',
                            [current_user.id, liked_user_id, liked_user_id, current_user.id], one=True)

    if match_exists:
        return jsonify({'match': True})

    # Insert the like into the database
    execute_db('INSERT INTO likes (user_id, liked_user_id) VALUES (?, ?)', [current_user.id, liked_user_id])

    # Check if the other user liked this user back
    reciprocal_like = query_db('SELECT * FROM likes WHERE user_id = ? AND liked_user_id = ?', [liked_user_id, current_user.id], one=True)

    if reciprocal_like:
        # Create a match
        execute_db('INSERT INTO matches (user1_id, user2_id) VALUES (?, ?)', [current_user.id, liked_user_id])
        return jsonify({'match': True, 'match_user':reciprocal_like})

    return jsonify({'match': False})

@app.route('/dislike/<int:user_id>', methods=['POST'])
@login_required
def dislike_user(user_id):
    # Logic for dislike can be added if needed, e.g., tracking dislikes
    return redirect(url_for('welcome'))

@app.route('/matches')
@login_required
def matches():
    matches = query_db('SELECT * FROM matches WHERE user1_id = ? OR user2_id = ?', [current_user.id, current_user.id])
    match_users = []
    for match in matches:
        user_id = match['user1_id'] if match['user2_id'] == current_user.id else match['user2_id']
        user = query_db('SELECT * FROM user WHERE id = ?', [user_id], one=True)
        match_users.append(user)
    return render_template('match.html', matches=match_users)

@app.route('/chats')
@login_required
def chats ():
    existing_chats = query_db('SELECT * FROM matches WHERE user1_id = ? OR user2_id = ?', [current_user.id, current_user.id])
    chat_users = []
    for chat in existing_chats:
        user_id = chat['user1_id'] if chat['user2_id'] == current_user.id else chat['user2_id']
        user = query_db('SELECT * FROM user WHERE id = ?', [user_id], one=True)
        chat_users.append(user)
    return render_template('chats.html', chat_users=chat_users)

@app.route('/chat/,<int:match_id>')
@login_required
def chat(match_id):
    match_user = query_db('SELECT * FROM matches WHERE id = ?', [match_id], one=True)
    if match_user:
        room = f"{min(current_user.id, match_id)}-{max(current_user.id, match_id)}"
        return render_template('chat.html', username=current_user.name, match_username=match_user['name'], room=room)
    else:
        flash('Chat not found', 'danger')
        return redirect(url_for('matches'))

@socketio.on('send_message')
def handle_send_message(data):
    room = data['room']
    message = data['message']
    emit('receive_message', {'message': message, 'username': data['username']}, room=room)

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)

@socketio.on('leave')
def handle_leave(data):
    room = data['room']
    leave_room(room)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.html'))

if __name__ == '__main__':
    socketio.run(app, debug=True)
    app.run(debug=True)