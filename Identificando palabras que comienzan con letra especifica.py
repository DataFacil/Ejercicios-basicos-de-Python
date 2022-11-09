# Muestra en la consola solo las palabras que empiecen con 's' de una frase

frase = 'Soy super responsable siempre que Sigo las instrucciones siendo sincero'
por_palabras = frase.split(' ')

for palabra in por_palabras:
    if palabra[0].lower() == 's':
        print(f'"{palabra}" empieza con la letra "s"')


