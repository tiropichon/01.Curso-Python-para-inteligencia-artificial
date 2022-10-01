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
		cursor.execute("CREATE TABLE IF NOT EXISTS students (nombre VARCHAR(100), nota_media INTEGER, email VARCHAR(100))")

		# Insertamos un registro en la tabla students
		# cursor.execute("INSERT INTO students VALUES ('Pilar',8,'pilar@ejemplo.com')")
		# cursor.execute("INSERT INTO students VALUES ('Mario',10,'mario@ejemplo.com')")

        # Vamos a hacer una consulta de la tabla students
		# cursor.execute("SELECT * FROM students")

        # fetchone recoge un registro de la tabla
		#student = cursor.fetchone()
		#print(student)

		# primer elemento de la tupla student
		#print(student[0])

		# Segundo elemento de la tupla student
		#print(student[1])

		#student2 = cursor.fetchone()
		#print(student2)


        #Insertar varios valores con executemany()
		student_list = [
		    ('Pilar', 8, 'pilar@ejemplo.com'),
		    ('Pepe', 6, 'pepe@ejemplo.com'),
		    ('Leonidas', 9, 'leonidas@ejemplo.com')

		]

		#cursor.executemany("INSERT INTO students VALUES(?,?,?)", student_list)

		cursor.execute("SELECT * FROM students")

        #mostrar todos los registros de la tabla students
		students = cursor.fetchall()

		for student in students:
			print(student[0],':',student[1])

        #Guardamos los cambios en BBDD
		connection.commit()

		return connection

	except Error as e:
		print(f"Ha ocurrido un error: 'e'")

connection = create_connection("students.db")
connection.close()