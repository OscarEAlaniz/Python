"""
Ejercicio 2.
Escribir un porgrama que anada valres  a una lista mientras 
su longitud sea menor a 120 y luego mostrar lista
plus: usar while y for

"""
coleccion = []
"""
for contador in range(0,120):
    coleccion.append(f"elemento - {contador}")
    print("mostrnado el :"+ coleccion[contador])

print(coleccion)
"""
contador = 0
while contador <120:
    coleccion.append(f"elemento - {contador}")
    print("mostrnado el :"+ coleccion[contador])
    contador+=1