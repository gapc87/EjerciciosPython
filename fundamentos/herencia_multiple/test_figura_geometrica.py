from fundamentos.herencia_multiple.cuadrado import Cuadrado
# from fundamentos.herencia_multiple.figura_geometrica_abstract import FiguraGeometrica

# No es posible crear objetos de una clase abstracta
# figuraGeometrica = FiguraGeometrica()

cuadrado = Cuadrado(4, "rojo")
print(cuadrado.area())
print(cuadrado)

print(Cuadrado.mro())
