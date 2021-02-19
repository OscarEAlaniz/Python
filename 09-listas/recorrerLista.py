pelicula ="Batman"
peliculas =[ "batman ", "spiderman", "el seño de los anillos" ]
cantantes = list(('2pac','drake'))
years =list(range(2020,2250))
variada = ["oscar",30, True, "texto"]

# recorrer lista co bucle for
print( "##### listado de peliculas  ####")

nueva_peli =" "
while nueva_peli!= "parar":
    nueva_peli = input("intrudce pelicula:  ")
    peliculas.append(nueva_peli)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1} - {pelicula}")




