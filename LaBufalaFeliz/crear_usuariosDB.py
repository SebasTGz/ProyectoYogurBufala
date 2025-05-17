'''Crear usuarios en la base de datos y la tabla de usuarios'''
#SOLO EJECUTAR UNA VEZ, ES PARA INICIALIZAR LA BASE DE DATOS.

import sqlite3

# conn = sqlite3.connect('usuarios.db')
# conn.execute('''
# CREATE TABLE IF NOT EXISTS usuarios (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT UNIQUE NOT NULL,
#     password TEXT NOT NULL
# )
# ''')
# conn.commit()
# conn.close()
# print("Base de datos y tabla de usuarios creadas.")

# #YA SE EJECUTÓ, NO VOLVER A HACERLO


#VER LOS USUARIOS CREADDOS
conn = sqlite3.connect('usuarios.db')
cursor = conn.execute('SELECT id, username FROM usuarios')
usuarios = cursor.fetchall()
conn.close()

for usuario in usuarios:
    print(f"ID: {usuario[0]}, Usuario: {usuario[1]}")
