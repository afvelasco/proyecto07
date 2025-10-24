from flask import Flask, jsonify, request
from flask_cors import CORS # Necesario para permitir peticiones desde el frontend

app = Flask(__name__)
# Configura CORS para permitir peticiones desde cualquier origen (necesario en desarrollo)
CORS(app) 

# Base de datos simulada
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1200, "usuario": "afvelasco"},
    {"id": 2, "nombre": "Mouse", "precio": 25, "usuario": "afvelasco"},
]
id_contador = 3

@app.route('/productos', methods=['GET'])
def listar_productos():
    return jsonify(list(productos)), 200

@app.route('/productos/<nom>', methods=['GET'])
def busca_producto(nom):
    for p in productos:
        if p["nombre"]==nom:
            return jsonify(p), 200
    return jsonify({"id":0, "precio": " Producto no encontrado"}), 200

@app.route('/productos', methods=['POST'])
def crear_producto():
    global id_contador
    data = request.json
    nuevo_producto = {"id": id_contador, "nombre": data['nombre'], "precio": data['precio'], "usuario": data['usuario']}
    productos.append(nuevo_producto)
    id_contador += 1
    return jsonify(nuevo_producto), 201

@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    if id not in productos:
        return jsonify({"mensaje": "Producto no encontrado"}), 404
    data = request.json
    productos[id]['nombre'] = data.get('nombre', productos[id]['nombre'])
    productos[id]['precio'] = data.get('precio', productos[id]['precio'])
    productos[id]['usuario'] = data.get('usuario', productos[id]['usuario'])
    return jsonify(productos[id]), 200

@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    """D (Delete): Elimina un producto."""
    if id not in productos:
        return jsonify({"mensaje": "Producto no encontrado"}), 404
    del productos[id]
    return jsonify({"mensaje": f"Producto {id} eliminado"}), 200

if __name__ == '__main__':
    # Este servicio debe correr en un puerto diferente al de Usuarios
    app.run(host="0.0.0.0",port=5001, debug=True)