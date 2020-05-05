a = int(input("Proporciona un valor:"))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valorMinimo <= a <= valorMaximo)  # (a >= valorMinimo and a <= valorMaximo)
print(dentroRango)
if dentroRango:
    print('dentro de rango')
else:
    print('fuera de rango')


vacaciones = False
diaDescanso = False
if vacaciones or diaDescanso:
    print('podemos ir al parque')
else:
    print('tienes deberes que hacer')

# con not() invertimos el valor
print(not vacaciones)
