from flask import Flask, url_for

app = Flask(__name__)

@app.route("/dado/<int=caras>")
def dado(caras):
    from random import randint
    numero = randint(1, caras)
    return f"<h2>Dado de {caras} caras, salió {numero}!</h2>"
