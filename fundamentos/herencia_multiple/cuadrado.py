# from fundamentos.herencia_multiple.figura_geometrica import FiguraGeometrica
from fundamentos.herencia_multiple.color import Color
from fundamentos.herencia_multiple.figura_geometrica_abstract import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def __str__(self) -> str:
        return FiguraGeometrica.__str__(self) + ", " + Color.__str__(self) + ", Área: " + str(self.area())
