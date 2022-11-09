# Crea un programa que, dada una lista de números, muestre en pantalla el número más grande de esa lista

lista1 = [2, 300, 101, 4, 0, 500, 23, 1]

maximo = None

for elem in lista1:
    if (maximo == None or elem > maximo):
        maximo = elem


print(maximo)
print(max(lista1))