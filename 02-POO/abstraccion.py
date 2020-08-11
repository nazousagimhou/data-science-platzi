class Lavadora:
# Objeto Lavadora

# Mi lavadora no necesita valores especificos
	def __init__(self):
		pass
# Las caracteríasticas que tiene la lavadora, 
# la definicion de la lavadora
	def lavar(self,temperatura='20 C'):
		self._llenar_tanque_de_agua(temperatura)
		self._anadir_jabon()
		self._lavar()
		self._centrifugar()

# Los metodos nos dicen que puede hacer 
# la lavadora

	def _llenar_tanque_de_agua(self, temperatura):
		print(f'Llenando el tanque de agua a temperatura {temperatura}')

	def _anadir_jabon(self):
		print('Anadiendo jabon')
	
	def _lavar(self):
		print(f'Lavando')
	
	def _centrifugar(self):
		print('Centrifugando la ropa ')

# El siguinte renglon nos dice que si corremos este progrma
# va a comenzar con lo que se defino inmediatamnete despues 
if __name__=='__main__':
	lavadora = Lavadora()
#En este caso vamos a generar una instancia de lavadora 
	lavadora.lavar()

