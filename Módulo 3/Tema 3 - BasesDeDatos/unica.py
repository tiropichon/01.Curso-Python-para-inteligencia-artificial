import sqlite3

connection = sqlite3.connect("productos2.db")
cursor= connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos2 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        loc VARCHAR(4) UNIQUE,
        nombre VARCHAR(100),
        stock INTEGER
    )
	''')

productos=[
    ('A11','mesa',23),
    ('B20','maceta',10),
    ('C03','silla',31)
]

#cursor.executemany("INSERT INTO productos2 VALUES (null,?,?,?)",productos)
cursor.execute("SELECT * FROM productos2")
catalogo = cursor.fetchall()

for producto in catalogo:
	print(producto)

connection.commit()
connection.close()
