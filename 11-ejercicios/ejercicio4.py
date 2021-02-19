"""
# ejercicio 4.
crear 4 variables, una lista, string, entero y bool
que imprima un mensaje segun el tipo de dato de cada variables

"""
def comprobarTipado(dato, tipo):
    test = isinstance(dato,tipo)

    if test:
        result= print(f"este dato es del tipo {type(dato)}")
    else:
        result = None
    
    return result





mi_lista= [1,2,3,4]
mi_string="hola"
mi_entero= 1
mi_bool = True



comprobarTipado(mi_bool,bool)