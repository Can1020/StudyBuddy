from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, name, university, course_of_study, semester, skills, email, password):
        self.id = id
        self.name = name
        self.university = university
        self.course_of_study = course_of_study
        self.semester = semester
        self.skills = skills
        self.email = email
        self.password = password