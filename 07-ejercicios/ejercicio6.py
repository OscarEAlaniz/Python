"""
Ejericico 6
Mostrar todas la tablas de multiplicar del 1 al 10
mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

"""
numero_contador =0 
numero_tabla =0

for cabecera in range(1,11):
    print("########################################")
    print(f"############ TABLA DEL {cabecera}  ##############")
    print("########################################")
    for numero_contador in range(1,11):
        print(f"{cabecera} x {numero_contador} = {numero_contador*cabecera}")
    
    print ("\n")

