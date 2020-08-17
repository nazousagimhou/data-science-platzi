# Buscar un elemento en una lista del tamano que se nos aisgne,
# recorremos toda la laista y comparamos el valor dado con cada elemento 
# en la lista para saber si el elemento dado esta en la lsita. 

import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    
    return match

if __name__=='__main__':
    tamano_de_lista = int(input('De que tamano sera tu lista? '))
    objetivo = int(input('Que numero quieres encontrar ? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo}{" esta" if encontrado else " no esta"} en la lsita')