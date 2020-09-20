import json
import requests
from flask import *

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'DevRootsSecretKey'

@app.route("/")
def index():
    session['menuList'] = [{'url': '/', 'class': 'navbarItem', 'label': 'Home'},{'url': '/about', 'class': 'navbarItem', 'label': 'About Us'},{'url': '/resources', 'class': 'navbarItem', 'label': 'Resources'},{'url': '/login', 'class': 'navbarItem', 'label': 'Account'}]
    return render_template("index.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")


if __name__ == "__main__":
    app.run(debug = True)

