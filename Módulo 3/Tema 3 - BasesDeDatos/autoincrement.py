import sqlite3

connection = sqlite3.connect("productos.db")
cursor = connection.cursor()

cursor.execute('''
	CREATE TABLE IF NOT EXISTS productos(
	    id INTEGER PRIMARY KEY AUTOINCREMENT,
	    nombre VARCHAR(100) NOT NULL,
	    marca VARCHAR(50) NOT NULL,
	    precio FLOAT NOT NULL
	)
	''')

productos = [
    ('Ratón','Logitech',17.95),
    ('Tablet','Samsung',134.80),
    ('Monitor','Philips',152.50)
]

#En el insert, el campo autoincremental, el campo
#q pertenece se deja como null
#cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

#mostrar en consola
cursor.execute("SELECT * FROM productos")
catalogo = cursor.fetchall()

for producto in catalogo:
	print(producto)

connection.commit()
connection.close()