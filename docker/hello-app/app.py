from flask import Flask
import os
import socket

# Connect to Redis

#conn = sqlite3.connect('example.db')
visits = 0

app = Flask(__name__)


@app.route("/")
def hello():
    global visits
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    visits += 1
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='localhost', port=80)
