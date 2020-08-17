# leyes aplicadas a algoritmos
# Ley de la multiplicacion 

def funcion(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

# O(n) * O(n) = O(n*n) = O(n^2)

if __name__=='__main__':
    funcion(2)