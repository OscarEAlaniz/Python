"""
Ejercicio 3
escribir un scrip que muestre los cuadrados de los 60 
primero numero naturales.
- resolver con for y while
"""
print("\n###resuelto con while###")
contador = 1

while contador <= 60:
    print(contador*contador)
    contador+=1

print("\n###resuelto con for###")

contador = 0

for contador in range(1, 61):
    print(contador*contador)



