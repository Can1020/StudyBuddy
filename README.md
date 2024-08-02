# StudyBuddy

## Instructions
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up the database:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```
5. Run the application:
    ```bash
    flask run

## Introduction
StudyBuddy is an innovative app that aims to facilitate networking among students and create a supportive community for academic collaboration.

## Tech Stack
- Python
- Flask
- Flask-SocketIO
- Flask-Login
- Flask - Mail
- flask_wtf
- SQLite
- SQLAlchemy
- HTML
- CSS

## Features
- Login with university email.
- Register with university email and password.
- Add database functionality for user management.
- Networking and matching.
- Chat functionality.

## Future Improvements
- Add Search Filters.
- Add Search Bar.
- Add Profiles in User Settings.
- Add Profile Pictures.
- Implement Image sharing after matching.