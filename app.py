from flask import Flask

app = Flask(__name__)

@app.route("/")
def principal():
    return """
        <a href='/comentario'>Coment</a>
        <a href='/enviar'>Send</a>
        """

@app.route("/comentario")
def comentar():
    return "<p>Comente aquí</p>"

@app.route("/enviar")
def envio():
    return "<p>envíe</p>"
