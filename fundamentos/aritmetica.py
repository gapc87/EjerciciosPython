class Aritmetica:
    """ Clase aritmética para realizar las operaciones de sumar, restar, etc """
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def sumar(self):
        """ Se realiza la operación con los atributos de la clase """
        return self.op1 + self.op2

    def restar(self):
        return self.op1 - self.op2

    def multiplicar(self):
        return self.op1 * self.op2

    def dividir(self):
        return self.op1 / self.op2


# Creamos un objeto nuevo
aritmetica = Aritmetica(2, 4)
print("Resultado de la suma", aritmetica.sumar())
