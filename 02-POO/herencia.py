class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
#La clase Cuadrado extiende al rectangulo 
class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)
# super nos permite tener una referencia directa
# de la super clase de la extencion 

if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=5)
    print(rectangulo.area())
# este es el archivo que se ejecuta directamente 
# desde la consola
    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())
