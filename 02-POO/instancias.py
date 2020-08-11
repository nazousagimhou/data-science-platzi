
class Coordenada:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distancia(self, otra_coordenada):
		x_diff = (self.x - otra_coordenada.x)**2
		y_diff = (self.y - otra_coordenada.y)**2 

		return (x_diff + y_diff)**0.5

if __name__ == '__main__':
	coord_1 = Coordenada(3, 20)
	coord_2 = Coordenada(10, 50)

	print(coord_2.distancia(coord_1))
	
	# Praca comprobar que esta instancia 
	# es un objeto Coordenada usamos 
	# la siguinte instruccion 
	print(isinstance(coord_2,Coordenada))
