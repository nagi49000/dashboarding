import flask
from .app import get_app


app = get_app(server=flask.Flask(__name__))
server = app.server
