import sqlite3
from sqlite3 import Error

def create_connection(path):
	connection = None
	try:
		# Creamos conexión a BBDD para students.db
		connection = sqlite3.connect(path)

		# Creamos un cursor para la conexión
		cursor = connection.cursor()

		# Creamos una tabla students dentro de la BBDD students.db
		cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre VARCHAR(100), dni VARCHAR(9), edad INTEGER, email VARCHAR(100))")


        #Insertar varios valores con executemany()
		usuarios_list = [
		    ('Pilar', '11111111A',20, 'pilar@ejemplo.com'),
		    ('Pepe', '22222222B',37, 'pepe@ejemplo.com'),
		    ('Leonidas', '33333333C',29, 'leonidas@ejemplo.com'),
		    ('Alba', '44444444D',37,'alba@ejemplo.com')

		]

		cursor.executemany("INSERT INTO usuarios VALUES(?,?,?,?)", usuarios_list)


        #Guardamos los cambios en BBDD
		connection.commit()

		return connection

	except Error as e:
		print(f"Ha ocurrido un error: e")

connection = create_connection("usuarios.db")
connection.close()