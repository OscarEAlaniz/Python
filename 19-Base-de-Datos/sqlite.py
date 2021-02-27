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

conexion.commit()


# insertar datos

cursor.execute("INSERT INTO productos VALUES (null, 'primer producto ', 'descripcion de mi producto', 550)")
conexion.commit()


# listar datos

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

#print(productos)
for producto in productos:
    print("Titulo: ", producto[1])
    print("Descripción: ", producto[2])
    print("Descripción: ", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos ")
producto =  cursor.fetchone()
print(producto)

# cerrar conxion
conexion.close()

