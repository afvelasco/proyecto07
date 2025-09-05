from models.usuarios import mi_usuarios
from conexion import *
import hashlib
import pytest

class Test_usuarios:
    def setup_class(self):
        #Preparar el entorno para la prueba
        self.id="prueba"
        self.contra = "super"
        cifrada = hashlib.sha512(self.contra.encode("UTF-8")).hexdigest()
        sql = f"INSERT INTO usuarios (idusuario,contrasena) VALUES ('{self.id}','{cifrada}')"
        mi_cursor.execute(sql)
        miDB.commit()
    
    @pytest.mark.parametrize(["id_entrada","contra_entrada","esperado"],
                             [("prueba","super",True),
                              ("prueba","súper",False),
                              ("pruebita","hkhj",False)])
        
    def test_login(self,id_entrada,contra_entrada,esperado):
        #Ejecutar la prueba
        calculado = mi_usuarios.login(id_entrada,contra_entrada)
        #Verificación
        assert calculado == esperado

    def teardown_class(self):
        #Limpieza
        sql = f"DELETE FROM usuarios WHERE idusuario='{self.id}'"
        mi_cursor.execute(sql)
        miDB.commit()
        