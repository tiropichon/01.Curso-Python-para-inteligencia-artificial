import sqlite3
from sqlite3 import Error

def create_connection(path):
	connection = None
	try:
		connection = sqlite3.connect(path)
		print("Conexión a BBDD SQLite ejecutada")
	except Error as e:
		print(f"Ha ocurrido el error 'e'")
	return connection

connection = create_connection("students.db")

#cerrar la BBDD
connection.close()