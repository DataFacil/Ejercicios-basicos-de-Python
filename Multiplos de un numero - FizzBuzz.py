# Haz un programa que muestre los números del 1 al 100. Cuando el número sea múltiplo de 3, que diga "Pelao" en vez del número. Si el número es múltiplo de 5,
# que diga "Coding" en vez del número. Y si el número es múltiplo de 3 y de 5, que diga "Pelao Coding" en vez del número.

for i in range(1, 101):
    if i%3 == 0 and i%5 == 0:
        print('Pelao Coding')
    elif i%3 == 0:
        print('Pelao')
    elif i%5 == 0:
        print('Coding')
    else:
        print(i)