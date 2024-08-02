from abc import update_abstractmethods
from flask_socketio import emit, join_room, leave_room
from app import db, login_manager, app, socketio, mail, Flask_Message
from flask_login import (
    login_user,
    login_required,
    logout_user,
    current_user,
)
from flask import redirect, url_for, render_template, flash, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy import select
from sqlalchemy.orm import Session
import random
from models import User, Matches, Likes, PasswordReset
from forms import LoginForm, ForgotPasswordForm, RegistrationForm, ResetPasswordForm
from utils import get_serializer
from models import Message
from flask import jsonify

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("welcome"))
    
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = db.session.scalar(sa.select(User).where(User.email == email))

        if user:
            print(f"User found: {user.name} - {user.email}")  # Debug: Print user details
            is_password_correct = user.check_password(password)
            print(f"Password correct: {is_password_correct}")  # Debug: Print password verification result
            
            if is_password_correct:
                login_user(user)
                return redirect(url_for("welcome"))
            if user.email != email:
                flash("Invalid email")
                return redirect(url_for("login"))
            if user.password != password:
                flash("Invalid password")
                return redirect(url_for("login"))
            else:
                flash("Invalid email or password")
                return redirect(url_for("login"))
            
    return render_template("login.html", form=form)

@app.route('/welcome')
@login_required
def welcome():
    users = User.query.filter(User.id != current_user.id).all()
    matches = Matches.query.filter(
        sa.or_(
        (Matches.user1_id == current_user.id) | 
        (Matches.user2_id == current_user.id)
        )
    ).all()

    new_match = any(

        match.user1_id == current_user.id and not Likes.query.filter_by(user_id=match.user2_id, liked_user_id=current_user.id).first() or
        match.user2_id == current_user.id and not Likes.query.filter_by(user_id=match.user1_id, liked_user_id=current_user.id).first()
        for match in matches
    )

    likes = Likes.query.filter_by(user_id=current_user.id).all()
    for like in likes:
        reciprocal_like = Likes.query.filter_by(user_id=like.liked_user_id, liked_user_id=current_user.id).first()
        if reciprocal_like:
            new_match = reciprocal_like
            break
    random.shuffle(users)

    return render_template('welcome.html', users=users, matches=matches, new_match=new_match)


@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        email = form.email.data
        session = Session(db.engine)
        stmt = select(User).where(User.email == email)
        user = session.execute(stmt).scalar_one_or_none()
        if user:
            s = get_serializer()
            token = s.dumps(email, salt="email-confirm")
            expires_at = datetime.utcnow() + timedelta(minutes=15)
            password_reset = PasswordReset(email=email, token=token, expires_at=expires_at)
            db.session.add(password_reset)
            db.session.commit()

            msg = Flask_Message(
                "Password Reset Request",
                sender=app.config['MAIL_DEFAULT_SENDER'],
                recipients=[email]
            )
            link = url_for("reset_password", token=token, _external=True)
            msg.body = f"Your password reset link is {link}"
            mail.send(msg)

            flash("Check your email for the instructions to reset your password", "info")
        else:
            flash("Invalid email address", "danger")
    return render_template("forgot_password.html", form=form)


@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    s = get_serializer()
    try:
        email = s.loads(token, salt="email-confirm", max_age=3600)
    except Exception as e:
        print(f"Token loading failed: {e}")
        flash("The reset link is invalid or has expired", "danger")
        return redirect(url_for("forgot_password"))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method="pbkdf2:sha256:600000")
        print (f"Hashed password: {hashed_password}") #Debug: Print the hashed password 

        session = Session(db.engine)
        stmt = select(User).where(User.email == email)
        user = session.execute(stmt).scalar_one_or_none()
        if user:
            print(f"User found: {user.name} - {user.email}") #Debug: Print the user details
            user.password = hashed_password
            db.session.commit()

            updated_user = db.session.scalar(sa.select(User).where(User.email == email))
            print(f"Updated password in DB: {updated_user.password}") #Debug: Print the updated password

            db.session.execute(sa.delete(PasswordReset).where(PasswordReset.email == email))

            db.session.commit()

            flash("Your password has been updated!", "success")
            return redirect(url_for("login"))

        else:
            print(f"User not found")
    return render_template("reset_password.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method="pbkdf2:sha256:600000")
        new_user = User(
            name=form.name.data,
            age=int(form.age.data),
            location=form.location.data,
            university=form.university.data,
            course_of_study=form.course_of_study.data,
            semester=form.semester.data,
            skills=form.skills.data,
            email=form.email.data,
            password=hashed_password
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for("login"))
        except sa.exc.IntegrityError:
            db.session.rollback()
            flash("Email address already registered", "error")
    return render_template("register.html", form=form)


@app.route("/like", methods=["POST"])
@login_required
def like_user():
    data = request.get_json()
    liked_user_id = data["liked_user_id"]

    match_exists = db.session.scalar(
        sa.select(Matches).where(
            (Matches.user1_id == current_user.id) & (Matches.user2_id == liked_user_id) |
            (Matches.user1_id == liked_user_id) & (Matches.user2_id == current_user.id)
        )
    )
    
    if match_exists:
        return jsonify({"match": True})

    new_like = Likes(user_id=current_user.id, liked_user_id=liked_user_id)
    db.session.add(new_like)
    db.session.commit()

    reciprocal_like = db.session.scalar(
        sa.select(Likes).where(
            (Likes.user_id == liked_user_id) & (Likes.liked_user_id == current_user.id)
        )
    )
    
    if reciprocal_like:
        new_match = Matches(user1_id=current_user.id, user2_id=liked_user_id)
        db.session.add(new_match)
        db.session.commit()
        return jsonify({"match": True})

    return jsonify({"match": False})

@app.route("/dislike/<int:user_id>", methods=["POST"])
@login_required
def dislike_user(user_id):
    return redirect(url_for("welcome"))

@app.route("/matches")
@login_required
def matches():
    matches = Matches.query.filter(
        (Matches.user1_id == current_user.id) | (Matches.user2_id == current_user.id)
    ).all()
    match_users = []
    for match in matches:
        user_id = match.user1_id if match.user2_id == current_user.id else match.user2_id
        user = db.session.scalar(sa.select(User).where(User.id == user_id))
        match_users.append(user)
    return render_template("match.html", matches=match_users)

@app.route('/chat/<int:match_id>')
@login_required
def chat(match_id):
    match_user = db.session.get(User, match_id)
    if match_user:
        room = f"{min(current_user.id, match_id)}_{max(current_user.id, match_id)}"
        messages = Message.query.filter_by(room=room).order_by(Message.timestamp).all()
        return render_template('chat.html', room=room, username=current_user.name, match_username=match_user.name, messages=messages)
    else:
        flash('Invalid match ID', 'danger')
        return redirect(url_for('matches'))

@socketio.on('send_message')
def handle_send_message(data):
    room = data['room']
    message = data['message']
    user_id = current_user.id
    new_message = Message(room=room, user_id=user_id, message=message)
    db.session.add(new_message)
    db.session.commit()
    emit('receive_message', {'message': message, 'username': data['username']}, room=room)

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)

@socketio.on('leave')
def handle_leave(data):
    room = data['room']
    leave_room(room)