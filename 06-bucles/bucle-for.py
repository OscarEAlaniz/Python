"""
#for
 for variable in elemento_iterable(lista,rango, etc)
 bloque instrucciones
 """
contador = 0
resultado = 0

for contador in range(0, 10):
    print( "voy por el "+ str(contador))

   # resultado = resultado + contador 
    resultado+=contador
print(f"El resultado es: {resultado}")
# ejemplo tablas de multiplicacion


print("\n ############33 EJEMPLO ##########")

numero_usuario =int(input("de que numero quieres la tabla?: ")) 

if numero_usuario < 1:
    numero_usuario = 1
print(f"\n### tabla de multiplicar del numero {numero_usuario} ####")

for numero_tabla in range(1, 11):
    print(f"{numero_usuario} X {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("tabla finalizada..")