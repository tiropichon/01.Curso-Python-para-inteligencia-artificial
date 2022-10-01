import sqlite3
from sqlite3 import Error

def create_connection(path):
	connection = None
	try:
		# Creamos conexión a BBDD para students.db
		connection = sqlite3.connect(path)

		# Creamos un cursor para la conexión
		cursor = connection.cursor()

		cursor.execute("UPDATE usuarios SET nombre = 'Miguel', email='miguel@ejemplo.com' WHERE nombre='Pepe' ")

        #Guardamos los cambios en BBDD
		connection.commit()

		return connection

	except Error as e:
		print(f"Ha ocurrido un error: e")

connection = create_connection("usuarios.db")
connection.close()