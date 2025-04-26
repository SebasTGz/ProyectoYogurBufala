# config/__init__.py
class Config:
    SECRET_KEY = 'mi_clave_secreta'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://usuario:contraseña@localhost/nombre_basedatos'
