from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms import LoginForm
from models import User
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Example user database
users = {'user1': User(id=1, email='s_nezhdet22@stud.hwr-berlin.de', password='password')}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = next((u for u in users.values() if u.email == email and u.password == password), None)
        if user:
            login_user(user)
            return redirect(url_for('welcome'))
        else:
            flash('Invalid email or password')

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