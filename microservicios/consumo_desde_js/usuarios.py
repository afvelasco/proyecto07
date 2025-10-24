from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# Base de datos simulada
usuarios = {
    101: {"nombre": "Alice", "rol": "Admin"},
    102: {"nombre": "Bob", "rol": "Cliente"},
}

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(list(usuarios.values())), 200

if __name__ == '__main__':
    # Este servicio debe correr en un puerto diferente al de Productos
    app.run(host="0.0.0.0", port=5002, debug=True)