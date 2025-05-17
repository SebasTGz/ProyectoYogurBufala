from flask import Flask, render_template, redirect, request, url_for, session, flash
from config import Config
from vista.carrito import carrito_bp
import sqlite3
import os

def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), 'usuarios.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

db_path = os.path.join(os.path.dirname(__file__), 'usuarios.db')

def create_app(config_name=None) -> Flask:
    """
    Crea una aplicación Flask usando una configuración específica.
    Args:
        config_name: Nombre de la configuración a usar.
    Returns:
        Una instancia de Flask configurada.
    """
    #Configuración de Clave Secreta
    app = Flask(__name__)
    app.secret_key = 'segura_1436'

    # Registrar blueprint
    app.register_blueprint(carrito_bp) 

    # Configuración de la aplicación
    app.config.from_object(Config)

    # Rutas de la aplicación
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/sabores')
    def sabores():
        sabores = [

            {"id": 1, "nombre": "Mora", "descripcion": "Delicioso yogurt de mora", "precio": 12000, "imagen": "/static/images/yogur_real.png"},
            {"id": 2, "nombre": "Café", "descripcion": "Aromático yogurt de café", "precio": 14000, "imagen": "/static/images/yogur_real.png"},
            {"id": 3, "nombre": "Guanabana", "descripcion": "Rico yogurt de guanabana", "precio": 15000, "imagen": "/static/images/yogur_real.png"},
            {"id": 4, "nombre": "Piña", "descripcion": "Delicioso yogurt de piña", "precio": 16000, "imagen": "/static/images/yogur_real.png"},
            {"id": 5, "nombre": "Dietético", "descripcion": "Yogur Saludable, bajo en calorias", "precio": 16500, "imagen": "/static/images/yogur_real.png"}
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

    # REGISTRO DE USUARIOS
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            conn = get_db_connection()
            try:
                conn.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, password))
                conn.commit()
                flash('Usuario registrado exitosamente. Ahora puedes iniciar sesión.', 'success')
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                flash('El nombre de usuario ya existe.', 'danger')
            finally:
                conn.close()
        return render_template('registrar.html')

    # LOGIN DE USUARIOS
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            conn = get_db_connection()
            user = conn.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, password)).fetchone()
            conn.close()
            if user:
                session['usuario'] = username
                flash('¡Bienvenido, {}!'.format(username), 'success')
                return redirect(url_for('home'))
            else:
                flash('Usuario o contraseña incorrectos', 'danger')
        return render_template('login.html')

    @app.route('/logout')
    def logout():
        session.pop('usuario', None)
        flash('Sesión cerrada correctamente.', 'info')
        return redirect(url_for('login'))

    #Dejar por si falla
    # @app.route('/dietetico')
    # def dietetico():

    #     dieteticos = [
    #         {"nombre": "Dietético", "descripcion": "Yogur Saludable, bajo en calorias", 
    #         "precio": 16500, 
    #         "imagen": url_for('static', filename='images/yogur_real.png')}
    #     ]
    #     return render_template('dietetico.html', dieteticos=dieteticos)

    # @app.route('/login', methods=['GET', 'POST'])
    # def login():
    #     if request.method == 'POST':
    #         username = request.form['username']
    #         password = request.form['password']
    #         return redirect(url_for('home'))
    #     return render_template('login.html')

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