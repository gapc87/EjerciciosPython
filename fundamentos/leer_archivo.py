try:
    archivo = open("prueba.txt", "r")

    # print(archivo.read())

    # leer algunos caracters
    # print(archivo.read(5))
    # print(archivo.read(3))

    # leer lineas completas
    # print(archivo.readline())

    # iterando
    # for linea in archivo:
    #    print(linea)

    # leer lineas
    # print(archivo.readlines())

    # acceder a una linea de la lista
    # print(archivo.readlines()[1])

    # Copiar un archivo
    archivo2 = open("copia.txt", "w+")
    archivo2.write(archivo.read())
except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()
