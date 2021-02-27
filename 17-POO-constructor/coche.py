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


    # construcutor 
    def __init__(self,color,marca,modelo,velocidad,caballaje, plazas):
        self.color = color 
        self.marca = marca
        self.modelo = modelo
        self.Velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas




    # metodos, son acciones que hace el obejto
    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def acelerar(self):
        self.Velocidad +=1

    def frenar(self):
        self.Velocidad-=1

    def getVelocidad(self):
        return self.Velocidad

    def getInfo(self):
        info = "------informacion del coche---------"
        info+="\n Color: "+ self.getColor()
        info+="\n Marca: "+ self.getMarca()
        info+="\n Modelo: "+ self.getModelo()
        info+="\n Velocidad: "+ str(self.getVelocidad())
        return info
# fin de definicion clase