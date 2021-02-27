from coche import Coche


carro = Coche("Amarillo","Honda","Civic",150,200,4)

print(carro.getInfo())


# detectar tipado
if type(carro)==Coche:
    print("es un objeto coche")
else:
    print ("no es un objeto coche")


# visibilidad de atributos  publico o privados 

print(carro.getPrivado())
