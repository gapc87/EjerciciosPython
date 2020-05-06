from .numeros_identicos_exception import NumerosIdenticosException

resultado = None

try:
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    if a == b:
        raise NumerosIdenticosException("Ocurrió un error, números idénticos")
    resultado = a / b
except ZeroDivisionError as e:
    print("Ocurrió un error", e)
    print(type(e))
except TypeError as e:
    print("Ocurrió un error", e)
    print(type(e))
except ValueError as e:
    print("Ocurrió un error", e)
    print(type(e))
except Exception as e:
    print("Ocurrió un error", e)
    print(type(e))
else:
    print("No hubo ninguna excepción")
finally:
    print("Fin del manejo de excepciones")

print('resultado:', resultado)
print("continuamos")
