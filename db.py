import click
import os
import sqlite3
from flask import current_app, g

def get_db_con(pragma_foreign_keys = True):
    if 'db_con' not in g:
        g.db_con = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db_con.row_factory = sqlite3.Row
        if pragma_foreign_keys:
            g.db_con.execute('PRAGMA foreign_keys = ON;')
    return g.db_con

def close_db_con(e=None):
    db_con = g.pop('db_con', None)
    if db_con is not None:
        db_con.close()

@click.command('init-db') #aslo a decorater just like @app. Hiermit kann man Kommandozeilen erstellen
def init_db():
    try: #In einem try except Paket falls Python kein Zugriff auf das Dateissystem haben sollte.
        os.makedirs(current_app.instance_path) #Hier wird eine automatische Datei erzeugt
    except OSError:
        pass
    db_con = get_db_con()
    with current_app.open_resource('sql/drop_tables.sql') as f: #Hier wird die Datei droptables SQL geöffnet und mit Read gelesen. Execute führt es aus.
        db_con.executescript(f.read().decode('utf8')) 
    with current_app.open_resource('sql/create_tables.sql') as f: #Hier wird es dann neu erzeugt
        db_con.executescript(f.read().decode('utf8'))
    click.echo('Database has been initialized.') #Hier wird die Meldung "Database initialized" an dem User zurückgegeben.

def insert_sample():
    db_con = get_db_con()
    with current_app.open_resource('sql/insert_sample.sql') as f:
        db_con.executescript(f.read().decode('utf8'))

