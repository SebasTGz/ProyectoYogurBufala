from flask import Blueprint, request, session, redirect, url_for, render_template

carrito_bp = Blueprint('carrito', __name__)

@carrito_bp.route('/agregar_carrito', methods=['POST'])
def agregar_carrito():
    productos = {
        'nombre': request.form['nombre'],
        'descripcion': request.form['descripcion'],
        'precio': float(request.form['precio']),
        'imagen': request.form['imagen'],
        'cantidad': 1
    }

    if 'carrito' not in session:
        session['carrito'] = []
    carrito = session['carrito']

    # Asegura que todos los productos tengan 'cantidad'
    for p in carrito:
        if 'cantidad' not in p:
            p['cantidad'] = 1

    # Si ya existe el producto, aumenta cantidad
    for p in carrito:
        if p['nombre'] == productos['nombre']:
            p['cantidad'] += 1
            break
    else:
        carrito.append(productos)
    session['carrito'] = carrito

    return redirect(url_for('carrito.ver_carrito'))

@carrito_bp.route('/carrito')
def ver_carrito():
    carrito = session.get('carrito', [])
    # Calcula precio_total por producto
    for p in carrito:
        p['precio_total'] = p['precio'] * p['cantidad']
    return render_template('carrito.html', carrito=carrito)

@carrito_bp.route('/quitar_producto/<int:index>', methods=['POST'])
def quitar_producto(index):
    carrito = session.get('carrito', [])
    if 0 <= index < len(carrito):
        carrito.pop(index)
    session['carrito'] = carrito
    return redirect(url_for('carrito.ver_carrito'))

@carrito_bp.route('/aumentar_cantidad/<int:index>', methods=['POST'])
def aumentar_cantidad(index):
    carrito = session.get('carrito', [])
    if 0 <= index < len(carrito):
        carrito[index]['cantidad'] += 1
    session['carrito'] = carrito
    return redirect(url_for('carrito.ver_carrito'))

@carrito_bp.route('/disminuir_cantidad/<int:index>', methods=['POST'])
def disminuir_cantidad(index):
    carrito = session.get('carrito', [])
    if 0 <= index < len(carrito):
        if carrito[index]['cantidad'] > 1:
            carrito[index]['cantidad'] -= 1
        else:
            carrito.pop(index)
    session['carrito'] = carrito
    return redirect(url_for('carrito.ver_carrito'))

@carrito_bp.route('/vaciar_carrito', methods=['POST'])
def vaciar_carrito():
    session.pop('carrito', None)
    return redirect(url_for('carrito.ver_carrito'))
