import sqlite3

connection = sqlite3.connect("usuarios2.db")

cursor=connection.cursor()

cursor.execute('''
	CREATE TABLE IF NOT EXISTS usuarios2 (
	id VARCHAR(4) PRIMARY KEY, 
	nombre VARCHAR(100), 
	apellidos VARCHAR(100), 
	puntos INTEGER
	)
	''')

usuarios2 = [
    ('N001','Rebeca','Pérez',120),
    ('N002','Mario','García',87)
]

#cursor.executemany("INSERT INTO usuarios2 VALUES (?,?,?,?)", usuarios2)

cursor.execute("INSERT INTO usuarios2 VALUES ('N004','Mario','Ruiz',45)")
connection.commit()
connection.close()