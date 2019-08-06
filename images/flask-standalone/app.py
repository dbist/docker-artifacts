import os
import phoenixdb
import socket
from flask import Flask

app = Flask(__name__)

def get_hit_count():
    retries = 5
    while True:
        try:
            phoenixdb.connect("http://pqs:8765", autocommit=True)
        except phoenixdb.errors.InterfaceError as exc:
            raise exc

        html = "<h3>Hello from {name}!</h3>" \
           "Hostname: <b>{hostname}</b><br/>"
    return html.format(name=os.getenv("NAME", "Standalone Flask App"), hostname=socket.gethostname())

@app.route('/')
def hello():
    count = get_hit_count()
    return '{}.\n'.format(count)
