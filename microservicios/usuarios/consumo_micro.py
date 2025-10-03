import requests

resultado = requests.get("http://10.6.124.182:9001/usuarios")
usuarios = resultado.json()
print(usuarios)
resultado = requests.get("http://10.6.124.182:9001/usuarios/yaperdio")
usuarios = resultado.json()
print("*****************************")
print(usuarios)
nuevo_usuario = {"id":"12121212","nombre":"Lionel Messi","contrasena":"messi","foto":"messi.jpeg"}
salida = requests.post("http://10.6.124.182:9001/usuarios",json=nuevo_usuario)
print(salida.json())