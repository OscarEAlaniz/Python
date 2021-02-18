"""
Ejercicio 7
HAcer un programa que muestre todos los numero impares entre dos
numero que elija el usuario
"""

numero1 = int(input("numero 1: "))
numero2 = int(input("numero 2: "))

contador = 0

if numero1 < numero2:
    for contador in range(numero1,(numero2+1)):
        if contador%2 != 0:
            print (f"{contador} es impar")
      



else:
    print("el numero 1 debe ser mayor que numero 2")