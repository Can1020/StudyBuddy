from itsdangerous import URLSafeTimedSerializer
from flask import current_app

def get_serializer():
    return URLSafeTimedSerializer(current_app.config['SECRET_KEY'])