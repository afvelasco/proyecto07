from conexion import *
import routes.usuarios

@app.route("/uploads/<nombre>")
def uploads(nombre):
    return send_from_directory(app.config['CARPETAUP'],nombre)

@app.route("/")
def raiz():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5080,debug=True)