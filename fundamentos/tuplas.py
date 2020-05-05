# Tupla mantiene el orden, pero ya no se puede modificar
frutas = ("Naranja", "Plátano", "Guayaba")
print(frutas)

# largo de la tupla
print(len(frutas))

# acceder a un elemento
print(frutas[0])

# navegacion inversa
print(frutas[-1])

# rango excluyendo el ultimo indicado
print(frutas[0:2])

# modificar un valor no es posible directamente
# frutas[0] = "Naranjita"
frutasLista = list(frutas)
frutasLista[1] = "Platanito"
frutas = tuple(frutasLista)
print(frutas)

# iterar una tupla
for fruta in frutas:
    print(fruta, end=" ")

# no podemos agregar ni eliminar elementos de una tupla
del frutas
