from conexion import *
from models.usuarios import mi_usuarios
@app.route("/login", methods=['POST'])
def login():
    id = request.form['nom']
    contrasena = request.form['contra']
    seguir = mi_usuarios.login(id,contrasena)
    if seguir:
        session["logueado"] = True
        session["id"] = id
        return render_template("opciones.html")
    else:
        return render_template("index.html",msg = "Credenciales incorrectas")

@app.route("/usuarios")
def usuarios():
    if session.get("logueado"):
        resultado = mi_usuarios.consultar()
        return render_template("usuarios.html",usua = resultado)
    else:
        return redirect("/")

@app.route("/agregausuario")
def agregausuario():
    if session.get("logueado"):
        return render_template("agregausuario.html")
    else:
        return redirect("/")

@app.route("/guardausuario", methods=['POST'])
def guardausuario():
    id = request.form['id']
    nombre = request.form['nombre']
    contra = request.form['contra']
    foto = request.files['foto']
    resultado = mi_usuarios.consultar_a(id)
    if len(resultado)==0:
        mi_usuarios.agregar([id,nombre,contra,foto])
        return redirect("/usuarios")
    else:
        return render_template("agregausuario.html",msg = "Id ya registrado!!!")
