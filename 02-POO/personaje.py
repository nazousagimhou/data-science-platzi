class Personaje:

#Esto es el contructor del personaje
    def __init__(self, rol, nombre, vida, ataque):
#Estos son los atributos de nuestra clase personaje
        self.rol = rol 
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
    
    def recibir_danio(self, personaje):
        self.vida = self.vida - personaje.ataque
        if self.vida > 0:
            print(f'Has recibido daño de tu relaccion {personaje.nombre}, pero sigues viva') 
        else:
            self.vida = 0 
            print(f'Has muerto')
    
    def imprimir_valores(self):
        print('----------------------------------------------------------------------')
        print(f'Rol: {self.rol}')
        print(f'Nombre: {self.nombre}')
        print(f'Vida: {self.vida}')
        print(f'Ataque: {self.ataque}')
        print('----------------------------------------------------------------------')

    
class Protagonista(Personaje):

    def __init__(self, nombre, ataque):
        super().__init__('Protagonista', nombre, 100, ataque)  

class Antagonista(Personaje):

    def __init__(self, ataque):
        super().__init__('Antagonista', 'Toxiturbia', 200, ataque)

#El metodo imprimir valores en la sub clase Antagonista ha sido modificado 
# para solo motrar algunos valores del metodo de la super calse Personaje
# Es un ejemplo de polimorfismo     
    def imprimir_valores(self):
        print('----------------------------------------------------------------------')
        print(f'Nombre: {self.nombre}')
        print(f'Ataque: {self.ataque}')
        print('----------------------------------------------------------------------')


if __name__ == '__main__':
    heroina = Protagonista(nombre = 'Rei', ataque = 50)
    relacion = Antagonista(ataque = 70)

    heroina.recibir_danio(relacion)
    heroina.imprimir_valores()
    relacion.imprimir_valores()
    
    heroina.recibir_danio(relacion)
    
