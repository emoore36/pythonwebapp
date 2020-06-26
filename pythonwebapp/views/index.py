from flask import Blueprint, render_template

print = Blueprint(__name__, __name__, template_folder='templates')

@print.route('/')
def show():
    return render_template("index.html")