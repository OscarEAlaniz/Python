peliculas =[ "batman ", "spiderman", "el seño de los anillos"]
numeros = [1,1,1,435,63,72,18,9]

# ordenar lista de numeros

numeros.sort()
print(numeros)

# añadir elementos
peliculas.append("pinocho")
peliculas.insert(1,"up")
print(peliculas)


# eliminar elementos 
peliculas.pop(1)
peliculas.remove("spiderman")
print(peliculas)

# reversa en lista
numeros.reverse()
print(numeros)

# buscar dentro d euna lista
print('pinocho' in peliculas)


#contar elementos
print(len(peliculas))

# cuantas veces aparece un numero 
print(numeros.count(1))

#conseguir iindice 
print (peliculas.index("pinocho"))

# unir lista

peliculas.extend(numeros)
print(peliculas)