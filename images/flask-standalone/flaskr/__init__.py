import os
import socket
import time
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from flaskr import db
    db.init_app(app)

    def get_hit_count():
        retries = 5
        while True:
            visits = db.upsert_db()

            html = "<h3>Hello from {name}!</h3>" \
            "Hostname: <b>{hostname}</b><br/>" \
            "This site has been visited: <b>{visits}</b> times!"
            return html.format(name=os.getenv("NAME", "Apache Phoenix"), hostname=socket.gethostname(), visits=visits)

    @app.route('/')
    def hello():
        count = get_hit_count()
        return '{}.\n'.format(count)

    return app
