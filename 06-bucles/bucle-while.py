"""
# bucle while
estructura de control que itera o repite la ejcuacion de una 
de instrucciones tantas veces como sea necesario hasta que deje
deje de cumplirse la condicione


while condicion:
    bloque de instrucciones
    actuaizacion de contador
 """
contador = 1

while contador <= 100:
    print(f"estoy en el numero {contador}")
    contador =contador + 1


print("--------------------------------------------")

contador = 1
muestrame = str(0)
while contador <= 100:
    muestrame+=","+str(contador)
    print(f"estoy en el numero {contador}")
    contador =contador + 1

print(muestrame)


 ### EJEMPLO #####

print("#### EJEMPLO #####")

numero_usuario =int (input("de que numero quires la tabla: ")
)

if numero_usuario < 1:
    numero_usuario = 1

print(f"## tabla de {numero_usuario} ###")

contador = 1

while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador}")
    contador+=1
else:
    print("tabla finalizada")
