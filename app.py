from flask import Flask, url_for, redirect

app = Flask(__name__)

def main():
    url_d = url_for("dia")
    url_t = url_for("tarde")
    url_n = url_for("noche")

    return f"""
    <a href="(url_d)">dia</a>
    <a href="(url_t)">tarde</a>
    <a href="(url_n)">noche</a>
    """

@app.route('/saludo/dia')
def dia():
    return "Días"

@app.route('/saludo/tarde')
def tarde():
    return "Tardes"

@app.route('/saludo/noche')
def noche():
     return "Noches"