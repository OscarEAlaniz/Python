"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- hacer funcion Recorrer la lista y mostrarla
- ordenar y mostrar
-mostrar su longitud
-buscar algun elemento (qe el usuario pida)
"""



# crear lista

numeros = [13,64,52,73,21,7,91,63]

# funciones

def mostrarlista(lista):
    resultado = ""
    for elemento in lista:
        resultado +=str(elemento)
        resultado+="\n"

    return resultado
# recorrer y mostrar
#print("### recorrer y mostrar #####")

#for numero in numeros:
 #   print(numero)

print (mostrarlista(numeros))

print("#### ORDENAR Y MOSTRAR #####")
numeros.sort()
print(mostrarlista(numeros))




print("####  MOSTRAR LONGITUD #####")
print(len(numeros))

print("####  Busqueda en la lista #####")

busqueda = int(input ("introduce el numero: "))

comprobar = isinstance(busqueda, int)

while not comprobar or busqueda<=0:
    busqueda = int(input ("introduce el numero: "))
else:
    print(f"haz introducido: {busqueda}")


print(f"##### buscar en la lista el numero {busqueda}")

search = numeros.index(busqueda)
print(f"el numero buscado existe en la lista, es el indice: {search} ")



