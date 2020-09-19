from flask import Flask
from flask import render_template
# import pyrebase

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hola")
def hola():
    lol =  20
    lol += 500
    return "hola, xd " + str(lol)

@app.route("/pruba")
def aprubas():
    return render_template("prubas.html", titulo = "este es un titulo", body1 = "parte 1 del juego", body2 = 'parte 2 del juego')

@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug = True)
    