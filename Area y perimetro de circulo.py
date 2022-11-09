# Crea una función que reciba como argumento el valor del radio de un círculo, y retorne su
# perímetro y su área

from math import pi

def circulo(radio):
    perimetro = 2 * pi * radio
    area = pi * radio**2
    print(f'Para un circulo de radio {radio}, el perimetro es {round(perimetro, 2)} cms y su area es {round(area, 2)} cms cuadrados')

circulo(10)