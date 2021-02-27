# pogramcion orientado a objetos

# defino una clase (molde para crear objetos)


class Coche:

    # atributos o propiedade (variables)
    # caracteriticos del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "aventador"
    Velocidad = 100 
    caballaje = 100
    plazas = 2


    # metodos, son acciones que hace el obejto
    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.Velocidad +=1

    def frenar(self):
        self.Velocidad-=1

    def getVelocidad(self):
        return self.Velocidad

# fin de definicion clase
# crear un obejto, instaciar clase


coche = Coche()


coche.setColor("amarillo")
coche.setModelo("Murcielago")
print(coche.marca, coche.getColor(), coche.getModelo())
print("Velocidad actual", coche.getVelocidad())
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad nueva: ", coche.Velocidad)


