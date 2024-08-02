from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail, Message as Flask_Message
from flask_socketio import SocketIO
import os



basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "database.db")
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "studywithyourbuddy0@gmail.com"
app.config["MAIL_PASSWORD"] = "uaon kvfy hemv nhsz"
app.config["MAIL_DEFAULT_SENDER"] = "studywithyourbuddy0@gmail.com"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = "login"
mail = Mail(app)
socketio = SocketIO(app)

from routes import *

if __name__ == "__main__":
    socketio.run(app, debug=True)
    app.run(debug=True)