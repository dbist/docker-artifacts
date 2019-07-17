import time
import phoenixdb
from flask import Flask

app = Flask(__name__)
# necessary for the PQS initialization
time.sleep(15)
conn = phoenixdb.connect("http://pqs:8765", autocommit=True)
cursor = conn.cursor()
cursor.execute("CREATE SCHEMA IF NOT EXISTS HITS")
cursor.execute("CREATE TABLE IF NOT EXISTS HITS.HITS (id INTEGER PRIMARY KEY) SALT_BUCKETS=4")
cursor.execute("CREATE SEQUENCE IF NOT EXISTS HITS.HIT_SEQUENCE START 1 INCREMENT BY 1 CACHE 10")

def get_hit_count():
    retries = 5
    while True:
        try:
            cursor.execute("UPSERT INTO HITS.HITS(id) VALUES(NEXT VALUE FOR HITS.HIT_SEQUENCE)")
            cursor.execute("SELECT MAX(ID) FROM HITS.HITS")
            return cursor.fetchone()
        except phoenixdb.errors.InterfaceError as exc:
            raise exc

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello from Flask! I have been seen {} times.\n'.format(count)
