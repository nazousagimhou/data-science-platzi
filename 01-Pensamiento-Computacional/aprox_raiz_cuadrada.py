#Aproximacion de una raiz cuadrada

#objetivo = int(input('Escoge un numero entero: '))
#epsilon = 0.01
#paso = epsilon**2
#respuesta = 0.0

#while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
#	respuesta += paso

#if abs(respuesta**2 -objetivo) >= epsilon:
#	print(f'No se encontro la raiz cuadrada {objetivo}')
#else:
#	print(f'La raiz cuadrada de {objetivo} es {respuesta}')


#########################################################################

#Busqueda binaria de una raiz cuadrada

objetivo = int(input('Escoge un numero '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0 , objetivo)
respuesta = (alto + bajo)/2

while abs(respuesta**2 - objetivo ) >= epsilon:
	if respuesta**2 < objetivo:
		bajo = respuesta
	else:
		alto = respuesta

	respuesta = (alto + bajo) /2

print(f'La raiz cuadrada de {objetivo} es {respuesta}')
