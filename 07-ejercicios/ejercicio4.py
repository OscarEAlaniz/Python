"""
ejercicio 4
pedir dos numero al usuario y pedir todas la operaciones
de una calculadora

"""
numero1= int(input("numero1: "))
numero2= int(input("numero2: "))
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
resto = numero1 % numero2

print("********CALCULADORA****************")
print(f"la suma es: {numero1 + numero2}")
print(f"la resta es: {resta}")
print("la multiplicacion es:" , multiplicacion)
print("la division  es:" , division)
print("el resto de la division es:" , resto)