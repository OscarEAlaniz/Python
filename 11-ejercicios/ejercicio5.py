"""
Ejercici 5.
Crear una lista con el contenido de esta tabla:

ACCION  AVENTURA                DEPORTES
GTA     ASSINS                  FIFA 21
COD     CRASH                   PRO 21
PUGB    principe de perdia      MOTO GP 21

mostrar esta informacion ordenada
"""

tabla = [
    {
        "categoria": "ACCIÓN",
        "juegos" : ["GTA", "call of duty", "PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSASINS", "Crash Bandicoot", "Principe de percia"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21","PES 21", "MOTO GP 21"]        
    }
]


for categoria in tabla:
    print(f"----------{categoria['categoria']}-------------")
    for juego in categoria['juegos']:
        print(juego)