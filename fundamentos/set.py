# set es una coleccion sin orden y sin indices, no permite elementos repetidos
# y los elemetos no se pueden modificar, pero si agregar nuevos o eliminar
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

# largo
print(len(planetas))

# revisar si un elemento está presente
print("Marte" in planetas)

# agregar
planetas.add("Tierra")
print(planetas)

# eliminar con remove posiblemente arroj aexcepcion
planetas.remove("Tierra")
print(planetas)

# eliminar con discard no arroja excepcion
planetas.discard("Jupiter")

# limpiar el set completamente
planetas.clear()
print(planetas)

# eliminar el set
del planetas
