
# EJEMPLO 1
print("\n######## EJEMPLO 1 ##########")

color = "verde"

if color == "rojo":
    print("ël color es ROJO")

else:
    print("el color no es ROJO")

# EJEMPLO 2
print("\n######## EJEMPLO 2 ##########")
"""== IGUAL
!= DIFENRETE 
< MENOR QUE
>MAYOR QUE
<= MENOR IGUAL QUE 
>= MAYOR IGUAL QUE 
#Operadores logicos

and Y
or O
! negacion
not NO
"""


year = 2020
#year =int(input("en que año estamos: "))
if year >= 2021:
    print ("estamos de 2021 en adelante !!")
else:
    print ("estamos año anterior a 2021 !!")

# EJEMPLO 3
print("\n######## EJEMPLO 3 ##########")

nombre = "Oscar Alaniz"
ciudad = "Barcelona"
continente = "Europa"
edad = 55
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad !!")

    if continente !="Europa":
        print("El usuario No es europeo")
    else: 
        print(f"Es europero y de {ciudad}")
else: 
    print(f"{nombre} No es mayor de edad!!")



# EJEMPLO 4
print("\n######## EJEMPLO 4 ##########")
"""
dia = int(input("introduce el # del dia de la semana: "))

if dia == 1:
    print("es Lunes")
else:
    if dia == 2:
        print("es Martes")
    else:
        if dia == 3:
            print("es Miercoles")
        else:
            if dia == 4:
                print("es Jueves")
            else: 
                if dia == 5:
                    print("es Viernes")
                else: 
                    print("es fin de semana")

"""
#dia = int(input("introduce el # del dia de la semana: "))
dia =1
if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es fin de semana")


# EJEMPLO 5 operador logico and
print("\n######## EJEMPLO 5 ##########")

edad_minima =18
edad_maxima= 65
#edad_oficial= int(input("introduce edad: "))
edad_oficial= 12
if edad_oficial >= edad_minima and edad_oficial<= edad_maxima:
    print( "esta en edad de trabajar")
else:
     print("no esta en edad de trabajar")


# EJEMPLO 5 operador logico or
print("######## EJEMPLO 6 ##########")

pais = "Alemania"

if pais=="Mexico" or pais=="España" or pais=="Colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")



# EJEMPLO 7 operador logico or
print("\n######## EJEMPLO 7 ##########")
pais = "Alemania"

if not(pais=="Mexico" or pais=="España" or pais=="Colombia"):
    print(f"{pais} no es un pais de habla hispana")
else:
     print(f"{pais} es un pais de habla hispana")
# EJEMPLO 8 operador logico or
print("\n######## EJEMPLO 8 ##########")
pais = "Alemania"

if pais!="Mexico" and pais!="España" and pais!="Colombia":
    print(f"{pais} no es un pais de habla hispana")
else:
     print(f"{pais} es un pais de habla hispana")
    
