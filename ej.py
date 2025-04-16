from flask import Flask, url_for
import sqlite3

app = Flask
db = None

def abrirConexion():
    db = sqlite3.connect("datos.sqlite")
    db.row_factory = sqlite3.Row
    return db

def cerrarConexion():
    global db
    if db is not None:
        db.close()
        db = None

@app.route("/usuarios")
def obtenerGente():
    global db
    conexion = abrirConexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios')
    resultado = cursor.fetchall()
    cerrarConexion()
    fila = (dict(row) for row in resultado)
    return str(fila)

#@app.route("/rutas")
