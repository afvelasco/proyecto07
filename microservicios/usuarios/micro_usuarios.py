from flask import Flask, request, jsonify
import json
import mysql.connector
import hashlib

programa = Flask(__name__)
miDB = mysql.connector.connect(host="localhost",
                               port="3306",
                               user="root",
                               password="",
                               database="proyecto07")
mi_cursor = miDB.cursor()

@programa.route("/usuarios", methods=['GET'])
def get_usuarios():
    sql = f"SELECT * FROM usuarios WHERE inactivo=0"
    mi_cursor.execute(sql)
    usuarios=mi_cursor.fetchall()
    datos = []
    for usuario in usuarios:
        datos.append({"id":usuario[0],"nombre":usuario[1],"foto":usuario[3]})
    return jsonify({"usuarios":datos})

@programa.route("/usuarios/<id>", methods=['GET'])
def get_usuario(id):
    sql = f"SELECT * FROM usuarios WHERE idusuario='{id}' AND inactivo=0"
    mi_cursor.execute(sql)
    usuario=mi_cursor.fetchall()
    if len(usuario)>0:
        return jsonify({"id":usuario[0][0],"nombre":usuario[0][1],"foto":usuario[0][3]})
    else:
        return jsonify({"mensaje":"Id no encontrado"})

@programa.route("/usuario", methods=['POST'])
def agrega_usuario():
    nuevo_usuario = request.get_json()
    id = nuevo_usuario['id']
    sql = f"SELECT nombre FROM usuario WHERE idusuario='{id}'"
    mi_cursor.execute(sql)
    resultado = mi_cursor.fetchall()
    if len(resultado)>0:
        return jsonify({"mensaje": "Id ya registrado"})
    else:
        cifrada = hashlib.sha512(nuevo_usuario['contrasena'].encode("utf-8")).hexdigest()
        sql = f"INSERT INTO usuarios (idusuario,nombre,contrasena,foto) VALUES ('{id}','{nuevo_usuario['nombre']}','{cifrada}','{nuevo_usuario['foto']}')"
        mi_cursor.execute(sql)
        miDB.commit()
        return jsonify({"mensaje":"Usuario agregado con exito"})

@programa.route("/usuarios", methods=['PUT'])
def modifica_usuario():
    usuario = request.get_json()
    cifrada = hashlib.sha512(usuario['contrasena'].encode("utf-8")).hexdigest()
    sql = f"UPDATE usuarios SET nombre='{usuario['nombre']}', contrasena='{cifrada}', foto='{usuario['foto']}' WHERE idusuario='{usuario['id']}'"
    mi_cursor.execute(sql)
    miDB.commit()
    return jsonify({"mensaje":"Usuario modificado con exito"})

@programa.route("/usuarios/<id>", methods=['DELETE'])
def elimina_usuario(id):
    sql = f"UPDATE usuarios SET inactivo=1 WHERE idusuario='{id}'"
    mi_cursor.execute(sql)
    miDB.commit()
    return jsonify({"mensaje":"Usuario eliminado con exito"})

@programa.route("/validalogin",methods=['POST'])
def validalogin():
    usuario = request.get_json()
    id = usuario['id']
    contra = usuario['contrasena']
    cifrada = hashlib.sha512(contra.encode("utf-8")).hexdigest()
    sql = f"SELECT nombre FROM usuarios WHERE idusuario='{id}' AND contrasena='{cifrada}' AND inactivo=0"
    mi_cursor.execute(sql)
    resultado=mi_cursor.fetchall()
    if len(resultado)>0:
        return "Autorizado"
    else:
        return "Denegado"

if __name__=="__main__":
    programa.run(port=9001,host="0.0.0.0",debug=True)

