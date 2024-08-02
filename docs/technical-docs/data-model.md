---
title: Data Model
parent: Technical Docs
nav_order: 2
---

{: .label }
[Dzhan Nezhdet]

{: .no_toc }
# Data model

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## StudyBuddy Datenmodell-Datenstruktur

```mermaid
classDiagram
    class FlaskApp {
        - app: Flask
        - db: SQLite
        - mail: Flask Mail
        - socketio: SocketIO
        + create_app(): FlaskApp
    }

    class User {
        - id: Integer
        - name: String
        - age: Integer
        - location: String
        - university: String
        - course_of_study: String
        - semester: String
        - skills: String
        - email: String
        - password: String
        + __init__(id, name, age, location, university, course_of_study, semester, skills, email, password)
        + get_id()
        + set_password(password)
        + check_password(password)
    }

    class Match {
        - id: Integer
        - user1_id: Integer
        - user2_id: Integer
    }

    class Like {
        - id: Integer
        - user_id: Integer
        - liked_user_id: Integer
    }

    class PasswordReset {
        - id: Integer
        - email: String
        - token: String
        - expires_at: DateTime
    }

    class RegistrationForm {
        - name: StringField
        - age: IntegerField
        - location: StringField
        - university: StringField
        - course_of_study: StringField
        - semester: StringField
        - skills: StringField
        - email: StringField
        - password: PasswordField
        - confirm_password: PasswordField
        + validate_email()
    }

    class LoginForm {
        - email: StringField
        - password: PasswordField
        + validate()
    }

    class ForgotPasswordForm {
        - email: StringField
        + validate_email()
    }

    class ResetPasswordForm {
        - password: PasswordField
        - confirm_password: PasswordField
    }

    class Database {
        + database.db
    }

    class SocketIOHandler {
        + send_message(data)
        + join_room(data)
        + leave_room(data)
    }

    FlaskApp --> Database
    FlaskApp --> SocketIOHandler

    RegistrationForm <|-- LoginForm
    RegistrationForm <|-- ForgotPasswordForm
    RegistrationForm <|-- ResetPasswordForm
