# Crea una código que, dado una variable de tipo entero (que representa un año),
# sea capaz de determinar si es o no un año bisiesto

# sea divisible por 4
# no sea divible por 100
# sea divisble por 400

# numero%4 == 0
# numero%100 != 0
# numero%400 == 0

def es_bisiesto(year):
    print(year%4 == 0)
    print(year%100 != 0)
    print(year%400 == 0)

    if year%4 == 0 and (year%100 != 0 or year%400 == 0):
        print(f'{year} es bisiesto')
    else:
        print(f'{year} no es bisiesto')

es_bisiesto(2001)