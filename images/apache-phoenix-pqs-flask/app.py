import os
import phoenixdb
import socket
import time
from flask import Flask, current_app, g
from flask.cli import with_appcontext

app = Flask(__name__)

def init_db(conn):
    db = get_db()
    with current_app.open_resource('schema.sql', mode='r') as f, db.cursor() as cursor:
        lines = [line.rstrip('\n').rstrip(';') for line in f]
        for line in lines:
            if not line.startswith('--'):
                cursor.execute(line)
    return

def connect_db():
    return phoenixdb.connect("http://pqs:8765", autocommit=True)

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if 'db' not in g:
        g.db = connect_db()
        g.db.cursor_factory = phoenixdb.cursor.DictCursor
    return g.db

def get_hit_count(conn):
    retries = 5
    while True:
        try:
            cursor = conn.cursor()
            cursor.execute("UPSERT INTO HITS.HITS(id) VALUES(NEXT VALUE FOR HITS.HIT_SEQUENCE)")
            cursor.execute("SELECT MAX(ID) FROM HITS.HITS")
            visits = cursor.fetchone()
        except phoenixdb.errors.InterfaceError as exc:
            raise exc

        html = "<h3>Hello from {name}!</h3>" \
           "Hostname: <b>{hostname}</b><br/>" \
           "This site has been visited: <b>{visits}</b> times!"
        return html.format(name=os.getenv("NAME", "Apache Phoenix"), hostname=socket.gethostname(), visits=visits)

@app.route('/')
def hello():
    conn = connect_db()
    init_db(conn)
    count = get_hit_count(conn)
    return '{}.\n'.format(count)
