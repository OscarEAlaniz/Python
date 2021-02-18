"""
Funciones:
una funcion es un conjunto de instrucciones bajo
un nombre concreto que pueden reutilizarse invocando a
la funcion tantas veces sea necesario

def nombreDeMIFuncion(paramteros)
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)
nombreDeMiFuncion(mi_parametro)
"""
# ejmeplo  1
print ("##### EJEMPLO 1 ####")

def muestraNombres():
    print("Oscar ")
    print("David ")
    print("Esteban ")
    print("\n")

    # invocar funcion

muestraNombres()

print ("##### EJEMPLO 2 ####")


def mostrarTunombre(nombre):
    print(F"tu nombre es: {nombre}")

nombre=input("introduce tu nombre: ")
mostrarTunombre(nombre)

print ("##### EJEMPLO 3 ####")

def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")


    for contador in range(1, 11):
        operacion = contador*numero
        print(f"{numero} x {contador} = {operacion}")
    print("\n") 


for numero_tabla in range(1,11):
    tabla(numero_tabla)


print ("##### EJEMPLO 4 ####")

# parametro opcionales

def getEmpleado(nombre, ID = False):
    print("EMPLEADO")
    print(f"nombre: {nombre}")
    if ID!= False:
        print(f"ID: {ID}")

getEmpleado("oscar alaniz","12345")

print ("##### EJEMPLO 5 ####")

# parametro opcionales y return 

def calculadora(numero1, numero2, basicos = False):
    suma = numero1 +numero2
    resta = numero1 - numero2
    multi = numero1 *numero2
    division = numero1/numero2

    cadena = ""

    cadena+="suma: "+ str(suma)
    cadena+="\n"
    cadena+="resta: "+ str(resta)
    cadena+="\n"
    cadena+="multiplicacion: "+ str(multi)
    cadena+="\n"
    cadena+="division: "+ str(division)

    return cadena


print (calculadora(2,2))
