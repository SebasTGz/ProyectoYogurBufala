from flask import Flask
from config.config import Config
from controlador.clientes_controlador import clientes_blueprint

app = Flask(__name__)
app.config.from_object(Config)

# Registro de Blueprints
app.register_blueprint(clientes_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
