class Persona:
    def __init__(self, nombre, ape_paterno, ape_materno):
        self.nombre = nombre
        self._ape_paterno = ape_paterno
        self.__ape_materno = ape_materno

    def __metodo_privado(self):
        print(self.nombre)
        print(self._ape_paterno)
        print(self.__ape_materno)

    def metodo_publico(self):
        self.__metodo_privado()

    def set_ape_materno(self, apellido_materno):
        self.__ape_materno = apellido_materno

    def get_ape_materno(self):
        return self.__ape_materno


p1 = Persona("Juan", "López", "Pérez")
# p1.__metodo_privado() no se puede acceder debido a que es privado
p1.metodo_publico()

print(p1.nombre)
print(p1._ape_paterno)
# print(p1.__ape_materno) manda error por ser privado
print(p1.get_ape_materno())
