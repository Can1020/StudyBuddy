import click
import os
import sqlite3
from flask import app, current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('database.db')
        g.db.row_factory = sqlite3.Row
    return g.db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
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
        table_exists = query_db("SELECT name FROM sqlite_master WHERE type='table' AND name='user';", one=True)
        if table_exists is None:
            with current_app.open_resource('schema.sql', mode='r') as f:
                db.executescript(f.read())
        db.commit()

def init_app(app):
    app.teardown_appcontext(close_connection)
    app.cli.add_command(init_db_command, name='init-db')


@click.command('init-db')
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def close_connection(_):
    db = g.pop('db', None)
    if db is not None:
        db.close()