import click
from flask import current_app, g
from flask.cli import with_appcontext
import phoenixdb

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql', mode='r') as f, db.cursor() as cursor:
        lines = [line.rstrip('\n').rstrip(';') for line in f]
        for line in lines:
            if not line.startswith('--'):
                cursor.execute(line)
    db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Initializes the database."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def connect_db():
    try:
         db = phoenixdb.connect('http://pqs:8765', autocommit=True)
    except phoenixdb.errors.InterfaceError as exc:
        print("Database is initializing")
    return db

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if 'db' not in g:
        g.db = connect_db()
        g.db.cursor_factory = phoenixdb.cursor.DictCursor
    return g.db

def upsert_db():
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("UPSERT INTO HITS.HITS(id) VALUES(NEXT VALUE FOR HITS.HIT_SEQUENCE)")
        cursor.execute("SELECT MAX(ID) FROM HITS.HITS")
        count = cursor.fetchone()
    except phoenixdb.errors.InterfaceError as exc:
        raise exc

def close_db(error):
    """Closes the database again at the end of the request."""
    db = g.pop('db', None)

    if db is not None:
        db.close()
