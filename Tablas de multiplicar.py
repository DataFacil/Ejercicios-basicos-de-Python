# Crea un programa que despliegue en pantalla las tablas de multiplicar del 1 al 10, de manera ordenada alineada.
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end='\t')
    print()