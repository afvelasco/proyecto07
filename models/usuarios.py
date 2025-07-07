from conexion import *

class Usuarios:
    def login(self, id, contrasena):
        cifrada = hashlib.sha512(contrasena.encode("utf-8" )).hexdigest()
        sql = f"SELECT * FROM usuarios WHERE idusuario='{id}' and contrasena='{cifrada}' and inactivo=0"
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        if len(resultado)==0:
            return False
        else:
            return True

    def consultar(self):
        sql = "SELECT * FROM usuarios WHERE inactivo=0"
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        return resultado

    def consultar_a(self,id):
        sql = f"SELECT * FROM usuarios WHERE idusuario='{id}'"
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        return resultado
    
    def agregar(self,usuario):
        nombref,extension = os.path.splitext(usuario[3].filename)
        fotonueva = usuario[0] + extension
        cifrada = hashlib.sha512(usuario[2].encode("utf-8")).hexdigest()
        sql = f"INSERT INTO usuarios (idusuario,nombre,contrasena,foto) values ('{usuario[0]}','{usuario[1]}','{cifrada}','{fotonueva}')"
        mi_cursor.execute(sql)
        miDB.commit()
        usuario[3].save("uploads/"+fotonueva)
        
        
        

mi_usuarios = Usuarios()

        