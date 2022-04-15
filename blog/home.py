from flask import (Flask, Blueprint, render_template, url_for, )

home = Blueprint('home', __name__, )

@home.route("/")
def index():
    return render_template("index.html")