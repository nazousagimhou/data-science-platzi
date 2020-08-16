import time

def factorial(n):
    respuesta = 1
    while n > 1:
        respuesta *=n
        n -= 1
    return respuesta


def factorial_re(n):
    if n==1:
        return 1
    return n * factorial_re(n-1)


if __name__=='__main__':
    n= 20000000

comienzo = time.time()
#print(factorial(n))
final = time.time()
print(final- comienzo)

comienzo = time.time()
#print(factorial_re(n))
final = time.time()
print(final- comienzo)




