from flask import Flask, redirect, render_template, request
import mysql.connector
import hashlib

app = Flask(__name__)
miDB = mysql.connector.connect(host="localhost",
                               port="3306",
                               user="root",
                               password="",
                               database="proyecto07")
mi_cursor = miDB.cursor()

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
        return redirect("/usuarios")
    
@app.route("/usuarios")
def usuarios():
    sql = "SELECT * FROM usuarios WHERE inactivo=0"
    mi_cursor.execute(sql)
    resultado = mi_cursor.fetchall()
    return render_template("usuarios.html",usua = resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5080,debug=True)