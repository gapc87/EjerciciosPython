class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    # metodo sobrescrito de la clase padre object
    def __add__(self, other):
        return self.__nombre + " " + other.__nombre

    def __sub__(self, other):
        return "Operación no soportada"


p1 = Persona("Juan")
p2 = Persona("Karla")

# Una nueva forma de trabajar al operador +
print(p1 + p2)

print(p1 - p2)
