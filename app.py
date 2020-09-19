import json
import requests
from flask import *

# import pyrebase

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hola")
def hola():
    with open("static/data/levels.json") as f:
        data = json.load(f)
    
    return "hola, xd " + str(lol)

@app.route("/pruba")
def aprubas():
    titulo = ''
    return render_template("prubas.html", titulo = titulo, body1 = "parte 1 del juego", body2 = 'parte 2 del juego')

@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug = True)
