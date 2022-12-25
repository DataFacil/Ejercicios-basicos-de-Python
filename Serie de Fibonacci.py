# Crea una función que muestre los n primeros números de la serie de fibonacci.
def fibonacci(n):
    serie = [0, 1]

    if n == 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return serie
    else:
        for num in range(2, n):
           serie.append(serie[num-1] + serie[num-2]) 
    return serie

print(fibonacci(10))