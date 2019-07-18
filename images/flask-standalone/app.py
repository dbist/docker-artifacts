import os
import socket
import time
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    count = "<b>cannot connect to Phoenix, counter disabled</b>" 

    html = "<h3>Hello from Flask!</h3>" \
           "Hostname: <b>{hostname}</b><br/>" \
           "<b>{visits}</b>"
    return html.format(hostname=socket.gethostname(), visits=count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
