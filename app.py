from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO
import re

app = Flask(__name__)
socketio = SocketIO(app)

# Regex for validating email
regex = r'^\b[A-Za-z0-9._%+-]+@stud\.[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    if re.fullmatch(regex, email):
        # Add logic for verifying email and password from the database
        return redirect(url_for('welcome'))
    else:
        return "Invalid email address. Please use your university email."

@app.route('/welcome')
def welcome():
    return "Welcome to StudyBuddy!"

if __name__ == '__main__':
    socketio.run(app, debug=True)