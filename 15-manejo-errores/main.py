# capturAR EXCEPCIONES Y MANEJAR ERRORES EN CODIGO
# suseptible a errores

try:

    nombre = input("cual es tu nombre: ")

    if len(nombre)>1:
        nombre_usuario = "el nombre es: " + nombre
    
    print(nombre_usuario)

except:
    print("ha ocurrido un errore, mete bien el nombre")

finally:
    print("fin del proceso")
