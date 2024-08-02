import click
import os
import sqlite3
from flask import app, current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES,
            check_same_thread=False
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = [dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall()]
    cur.close()
    return (rv[0] if rv else None) if one else rv

def execute_db(query, args=()):
    db = get_db()
    cur = db.cursor()
    cur.execute(query, args)
    db.commit()
    cur.close()

def init_db():
        db = get_db()
        with current_app.open_resource('schema.sql', mode='r') as f:
            db.executescript(f.read())
        db.commit()

def init_app(app):
    app.teardown_appcontext(close_connection)
    app.cli.add_command(init_db_command, name='init-db')

def init_db_command():
    app.teardown_appcontext(close_connection)
    app.cli.add_command(init_db_command)

def close_connection(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()