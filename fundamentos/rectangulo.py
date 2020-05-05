class Rectangulo:

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcularArea(self):
        return self.ancho * self.alto


print('Bienvenid@')
ancho = int(input('Introduzca el ancho del rectangulo: '))
alto = int(input('Introduzca el alto del rectangulo: '))
rectangulo = Rectangulo(ancho, alto)

print('El area del rectángulo es de', rectangulo.calcularArea())
