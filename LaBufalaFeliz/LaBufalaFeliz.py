from flask import Flask ,render_template, redirect, request, url_for
from config.config import Config
from controlador.clientes_controlador import clientes_blueprint

app = Flask(__name__)
app.config.from_object(Config)

# Registro de Blueprints
app.register_blueprint(clientes_blueprint)

@app.route('/home')
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
    carrito = [
        {"id": 1, "nombre": "Mora", "cantidad": 2, "precio": 5.0},
        {"id": 2, "nombre": "Café", "cantidad": 1, "precio": 5.5},
    ]
    total = sum(item["cantidad"] * item["precio"] for item in carrito)
    return render_template('carrito.html', carrito=carrito, total=total)

@app.route('/eliminar_del_carrito/<int:producto_id>', methods=['POST'])
def eliminar_del_carrito(producto_id):
    return redirect(url_for('carrito'))

@app.route('/checkout')
def checkout():
    return "Procesando el pago..."


if __name__ == '__main__':
    app.run(debug=True)
