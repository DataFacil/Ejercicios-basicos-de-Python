# Crea una función que reciba como argumento los valores de un cateto "a" y un cateto "b" de un
# triángulo rectángulo y retorne el valor de la hipotenusa

def pitagoras(cat1, cat2):
    return (cat1**2 + cat2**2)**(1/2)

print(pitagoras(3,4))