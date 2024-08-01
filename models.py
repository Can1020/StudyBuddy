from flask_login import UserMixin
from app import db
from werkzeug.security import check_password_hash, generate_password_hash
import sqlalchemy as sa
import sqlalchemy.orm as so
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = so.mapped_column(sa.Integer, primary_key=True)
    name = so.mapped_column(sa.String)
    age = so.mapped_column(sa.Integer)
    location = so.mapped_column(sa.String)
    university = so.mapped_column(sa.String)
    course_of_study = so.mapped_column(sa.String)
    semester = so.mapped_column(sa.String)
    skills = so.mapped_column(sa.String)
    email = so.mapped_column(sa.String)
    password = so.mapped_column(sa.String)

    def __init__(self, name, age, location, university, course_of_study, semester, skills, email, password):
        self.name = name
        self.age = age
        self.location = location
        self.university = university
        self.course_of_study = course_of_study
        self.semester = semester
        self.skills = skills
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        result = check_password_hash(self.password, password)
        print(f"Checking password for user {self.name}. Result: {result}")  # Debug: Print password check result
        return result


class Matches(db.Model):
    __tablename__ = "matches"
    id = so.mapped_column(sa.Integer, primary_key=True)
    user1_id = so.mapped_column(sa.Integer)
    user2_id = so.mapped_column(sa.Integer)

class Likes(db.Model):
    __tablename__ = "likes"
    id = so.mapped_column(sa.Integer, primary_key=True)
    user_id = so.mapped_column(sa.Integer)
    liked_user_id = so.mapped_column(sa.Integer)

class PasswordReset(db.Model):
    __tablename__ = "password_reset"
    id = so.mapped_column(sa.Integer, primary_key=True)
    email = so.mapped_column(sa.String)
    token = so.mapped_column(sa.String)
    expires_at = so.mapped_column(sa.DateTime, nullable=False)

class Message(db.Model):
    __tablename__ = "messages"
    id = sa.Column(sa.Integer, primary_key=True)
    room = sa.Column(sa.String, nullable=False)
    user_id = sa.Column(sa.Integer,sa.ForeignKey('user.id'), nullable=False)
    message = sa.Column(sa.String, nullable=False)
    timestamp = sa.Column(sa.DateTime, default=sa.func.current_timestamp())
    
    user = db.relationship('User', backref='messages')

