from flask import Flask, request, jsonify, render_template
import qrcode
import io
import base64

app = Flask(__name__)

# Función principal para generar el QR y devolverlo en Base64
def generar_qr_base64(data):
    """
    Genera un código QR para el 'data' proporcionado y lo devuelve
    como una cadena Base64 (formato PNG).
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Crea la imagen QR
    img = qr.make_image(fill_color="black", back_color="white")

    # Usamos io.BytesIO para guardar la imagen en memoria
    # sin tener que escribirla en el disco
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    
    # Codifica los bytes de la imagen a Base64
    qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return qr_base64

# ----------------- Rutas de Flask -----------------

# Ruta de la API para generar el QR (consumida por AJAX/fetch)
@app.route('/api/generate_qr', methods=['POST'])
def generate_qr():
    # Obtener el texto del cuerpo JSON de la solicitud
    data = request.json.get('text', '')
    
    if not data:
        return jsonify({"error": "El campo 'text' es obligatorio"}), 400

    try:
        # Generar la cadena Base64
        qr_base64_string = generar_qr_base64(data)
        
        # Devolver el resultado al frontend
        return jsonify({
            "qr_image": qr_base64_string,
            "data_url": f"data:image/png;base64,{qr_base64_string}"
        })
    except Exception as e:
        return jsonify({"error": f"Error al generar QR: {str(e)}"}), 500

# Ruta principal para servir la interfaz HTML
@app.route('/')
def index():
    return render_template('qr.html')

if __name__ == '__main__':
    # Ejecuta la aplicación en modo debug
    app.run(host="0.0.0.0", port=5080, debug=True)