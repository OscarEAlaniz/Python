import clases



persona = clases.Persona()
persona.setNombre("Oscar")
persona.setApellidos("Alaniz")
persona.setAltura("173cm")
persona.setEdad("1000 años")


print(f"la persona es: {persona.getNombre()} {persona.getApellidos()}")


informatico = clases.Informatico()

informatico.setNombre("Carlos")
informatico.setApellidos("Martinez")

print ("---Herencia----")
print(f"El informaticos es {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())


tecnico = clases.TecnicoRedes()
print(tecnico.auditarRedes)