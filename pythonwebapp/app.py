from flask import Flask
from views.index import print as index_print
from views.create import print as create_print

app = Flask(__name__)

app.register_blueprint(index_print)
app.register_blueprint(create_print)
