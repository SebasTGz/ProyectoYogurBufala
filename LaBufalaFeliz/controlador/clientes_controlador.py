from flask import Blueprint, render_template, request, redirect, url_for
from modelo.producto import Producto
from database.db import db

clientes_blueprint = Blueprint('clientes', __name__)

@clientes_blueprint.route('/')
def inicio():
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)

@clientes_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica para manejar login
        return redirect(url_for('clientes.inicio'))
    return render_template('login.html')
