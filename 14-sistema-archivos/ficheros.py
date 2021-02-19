from io import open
import pathlib
import shutil
#abrir archivo
ruta = str(pathlib.Path().absolute())+ "fichero_texto.txt"
#archivo = open("14-sistema-archivos/fichero_texto.txt", "a+")

archivo = open(ruta,"a+")

# escribir dentro de un archivo

archivo.write("******* soy un texto metido desde python*******\n")

# cerrar archivo

archivo.close()


ruta = str(pathlib.Path().absolute())+ "fichero_texto.txt"
#archivo = open("14-sistema-archivos/fichero_texto.txt", "a+")

archivo_lectura = open(ruta,"r") # permiso de lectura


# leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

# leer contenido y guardar en una lista

lista = archivo_lectura.readlines()
archivo_lectura.close()

#print(lista)

for frase in lista:
    print("-"+frase)



# copiar archivos
ruta_original= str(pathlib.Path().absolute())+ "fichero_texto.txt"
ruta_nueva = ruta = str(pathlib.Path().absolute())+ "fichero_copiado.txt"
shutil.copyfile(ruta_original,ruta_nueva)


#mover 









