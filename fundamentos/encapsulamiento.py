class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre


p1 = Persona("Juan")
print(p1.getNombre())
 
p1.setNombre('Karla')
print(p1.getNombre())
