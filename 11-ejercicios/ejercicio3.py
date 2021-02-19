"""
ejercicio 3. 
programa que compruebe si una variable esta vacia
y si esta vacia, rellenarla con texto en minusculas y mostrarlo
en mayusculas

"""

texto=""

if len(texto.strip()) <=0:
    # mostrar el texto
    texto = "hola soy un texto en minusculas"
    print(texto.upper())
else:
    print(f"la variable tiene contenido {texto}")