from flask import Flask
from pythonwebapp.views.index import print as index_print

app = Flask(__name__)

app.register_blueprint(index_print)
