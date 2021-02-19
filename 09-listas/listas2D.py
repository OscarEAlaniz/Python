print("\n  ********* Lista contactos *******")

contactos = [['oscar','oscar@gmail.com'],['esteban','esteban@mail.com'],
             ['ivone','ivone@gmail.com']
]
print(contactos)
print(contactos[0][1])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("nombre: "+ elemento)
        else:
            print("Email: "+ elemento)
    print("\n")
