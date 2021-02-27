# importar module

import sqlite3

# conexion


conexion = sqlite3.connect('pruebas.db')


# crear cursor
cursor = conexion.cursor()
# crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo varchar(255)," +
"descripcion text,"+
"precio int(255)"+
")")


# cerrar conxion
conexion.close()

