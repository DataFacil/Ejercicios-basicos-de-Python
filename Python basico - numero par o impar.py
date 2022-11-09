# Cree una función que reciba como argumento un número, y retorne True si es un número par o False si es impar

def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(es_par(200))
print(es_par(99))