"""
Ejercicio 10
ingresar la calificaciond de 15 alumnoos y ahorrojar cuantos 
aprobaron y cuantos reprobaron
"""


aprobados = 0
reprobados = 0
contador_alumnos= 0

for contador_alumnos in range(1,16):
    calificacion= int(input( f"introduce calificacion {contador_alumnos}: "))
    if calificacion >= 70:
        aprobados+=1
    else:
        reprobados+=1

print(f"alumnos aprobados: {aprobados}, alumnos reprobados {reprobados}")
        
