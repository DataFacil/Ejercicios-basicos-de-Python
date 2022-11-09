# Crea una funcion que dadas una cierta cantidad de notas, sea capaz de calcular
# el promedio de esas notas

def promedio(*elem):
    return sum(elem)/len(elem)

print(promedio(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))