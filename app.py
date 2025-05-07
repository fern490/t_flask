from flask import Flask, url_for, render_template, request
import sqlite3

app = Flask(__name__)

def abrirConexion():
    conexion = sqlite3.connect("datos.sqlite")
    conexion.row_factory = sqlite3.Row
    return conexion

def cerrarConexion():
   global db
   if db is not None:
        db.close()
        db = None

@app.route("/add/<string:nombre>/<string:email>")
def agregarUs(nombre, email):
    db = abrirConexion()
    db.execute("INSERT INTO usuarios (usuario, email) VALUES (?, ?)", (nombre, email))
    db.commit()
    db.close()
    return f'Usuario agregado: {nombre}'

@app.route("/delete/<int:id>")
def eliminarUs(id):
    db = abrirConexion()
    db.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    db.commit()
    db.close()
    return f'Usuario con ID {id} eliminado'

@app.route("/show/<int:id>")
def mostrarUs(id):
    db = abrirConexion()
    datos = db.execute("SELECT usuario, email FROM usuarios WHERE id = ?", (id,)).fetchone()
    db.close()
    if datos:
        return f"Usuario: {datos['usuario']}, Email: {datos['email']}"
    return f"No se encontró el usuario con ID {id}"

@app.route("/mostrar-datos-plantilla/<int:id>")
def datos_plantilla(id):
    global db
    db = abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT id, usuario, email, telefono, direccion FROM usuarios WHERE id = ?; ", (id,))
    res = cursor.fetchone()
    cerrarConexion()
    
    usuario = None
    email = None
    telefono = None
    direccion = None

    if res != None:
        usuario = res['usuario']
        email = res['email']
        telefono = res['telefono']
        direccion = res['direccion']
    return render_template("datos2.html", id = id, usuario = usuario, email = email, telefono = telefono, direccion = direccion)
    
if __name__ == "__main__":
    app.run(debug=True)