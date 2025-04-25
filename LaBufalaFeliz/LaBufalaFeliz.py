from flask import Flask ,render_template, redirect, request, url_for
from config.config import Config
from controlador.clientes_controlador import clientes_blueprint

app = Flask(__name__)
app.config.from_object(Config)

# Registro de Blueprints
app.register_blueprint(clientes_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sabores')
def sabores():
    # Aquí puedes cargar sabores desde la base de datos
    sabores = [
        {"id": 1, "nombre": "Mora", "descripcion": "Delicioso yogurt de mora", "precio": 5.0, "imagen": "/static/images/mora.jpg"},
        {"id": 2, "nombre": "Café", "descripcion": "Aromático yogurt de café", "precio": 5.5, "imagen": "/static/images/cafe.jpg"},
    ]
    return render_template('sabores.html', sabores=sabores)

@app.route('/personaliza', methods=['GET', 'POST'])
def personaliza():
    if request.method == 'POST':
        # Procesar personalización
        base = request.form['base']
        sabor = request.form['sabor']
        ingredientes = request.form['ingredientes']
        # Guardar en base de datos o sesión
        return redirect(url_for('carrito'))  # Ir al carrito tras personalizar
    return render_template('personaliza.html')

@app.route('/dietetico')
def dietetico():
    return render_template('dietetico.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Procesar login
        username = request.form['username']
        password = request.form['password']
        # Validar usuario
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/carrito')
def carrito():
    # Cargar el carrito desde sesión o base de datos
    carrito = []
    return render_template('carrito.html', carrito=carrito)

if __name__ == '__main__':
    app.run(debug=True)
