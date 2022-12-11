# Construye una funcion que muestre en una secuencia de Collatz, partiendo del numero dado como argumento

def collatz(n):

    while n != 1:
        print(n, end = ', ')

        if n % 2 != 0:
            n = 3 * n + 1

        else:
            n = n // 2

    print (n)


collatz(3)

        