"""
Ejercicio 2 
escribir un scrip que no muestre todos los numero pares del 
1 al 120

"""

contador = 0

for contador in range(1, 121):
    if contador%2 == 0:
        print(f"{contador} es par" )
    else:
        print(f"{contador} es impar ")