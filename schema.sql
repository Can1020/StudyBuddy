CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    university TEXT NOT NULL,
    course_of_study TEXT NOT NULL,
    semester TEXT NOT NULL,
    skills TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT, INTEGER  NOT NULL
);