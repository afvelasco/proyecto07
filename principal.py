import os
from flask import Flask, redirect, render_template, request, send_from_directory
import mysql.connector
import hashlib

app = Flask(__name__)
miDB = mysql.connector.connect(host="localhost",
                               port="3306",
                               user="root",
                               password="",
                               database="proyecto07")
mi_cursor = miDB.cursor()
app.config['CARPETAUP'] = os.path.join('uploads')

@app.route("/uploads/<nombre>")
def uploads(nombre):
    return send_from_directory(app.config['CARPETAUP'],nombre)

@app.route("/")
def raiz():
    return render_template("index.html")

@app.route("/login", methods=['POST'])
def login():
    id = request.form['nom']
    contrasena = request.form['contra']
    cifrada = hashlib.sha512(contrasena.encode("utf-8" )).hexdigest()
    sql = f"SELECT * FROM usuarios WHERE idusuario='{id}' and contrasena='{cifrada}' and inactivo=0"
    mi_cursor.execute(sql)
    resultado = mi_cursor.fetchall()
    if len(resultado)==0:
        return render_template("index.html",msg = "Credenciales incorrectas")
    else:
        return render_template("opciones.html")
    
@app.route("/usuarios")
def usuarios():
    sql = "SELECT * FROM usuarios WHERE inactivo=0"
    mi_cursor.execute(sql)
    resultado = mi_cursor.fetchall()
    return render_template("usuarios.html",usua = resultado)

@app.route("/agregausuario")
def agregausuario():
    return render_template("agregausuario.html")

@app.route("/guardausuario", methods=['POST'])
def guardausuario():
    id = request.form['id']
    nombre = request.form['nombre']
    contra = request.form['contra']
    foto = request.files['foto']
    sql = f"SELECT * FROM usuarios WHERE idusuario='{id}'"
    mi_cursor.execute(sql)
    resultado = mi_cursor.fetchall()
    if len(resultado)==0:
        nombref,extension = os.path.splitext(foto.filename)
        fotonueva = id + extension
        cifrada = hashlib.sha512(contra.encode("utf-8")).hexdigest()
        sql = f"INSERT INTO usuarios (idusuario,nombre,contrasena,foto) values ('{id}','{nombre}','{cifrada}','{fotonueva}')"
        mi_cursor.execute(sql)
        miDB.commit()
        foto.save("uploads/"+fotonueva)
        return redirect("/usuarios")
    else:
        return render_template("agregausuario.html",msg = "Id ya registrado!!!")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5080,debug=True)