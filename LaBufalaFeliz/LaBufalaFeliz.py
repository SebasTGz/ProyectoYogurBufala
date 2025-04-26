from flask import Flask, render_template, redirect, request, url_for
from config import Config

def create_app(config_name=None) -> Flask:
    """
    Crea una aplicación Flask usando una configuración específica.

    Args:
        config_name: Nombre de la configuración a usar.

    Returns:
        Una instancia de Flask configurada.
    """
    app = Flask(__name__)

    # Configuración de la aplicación
    app.config.from_object(Config)

    # Rutas de la aplicación
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/sabores')
    def sabores():
        sabores = [
            {"id": 1, "nombre": "Mora", "descripcion": "Delicioso yogurt de mora", "precio": 5.0, "imagen": "/static/images/mora.jpg"},
            {"id": 2, "nombre": "Café", "descripcion": "Aromático yogurt de café", "precio": 5.5, "imagen": "/static/images/cafe.jpg"},
        ]
        return render_template('sabores.html', sabores=sabores)

    @app.route('/personaliza', methods=['GET', 'POST'])
    def personaliza():
        if request.method == 'POST':
            base = request.form['base']
            sabor = request.form['sabor']
            ingredientes = request.form['ingredientes']
            return redirect(url_for('carrito'))
        return render_template('personaliza.html')

    @app.route('/dietetico')
    def dietetico():
        return render_template('dietetico.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            return redirect(url_for('home'))
        return render_template('login.html')

    @app.route('/carrito')
    def carrito():
        carrito = []
        return render_template('carrito.html', carrito=carrito)

    return app  # Aquí el return está dentro de la función

# Bloque principal
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
# Este bloque se ejecuta solo si el script se ejecuta directamente