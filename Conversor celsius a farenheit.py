def conversor():
    temp = input('Ingrese la temperatura con la respectiva unidad ')
    unidad = temp[-1].upper()
    grados = float(temp[:-1])

    if unidad == 'C':
        temp_conv = float(round(grados * (9/5) + 32, 1))
        print(f'{grados}°{unidad} es equivalente a {temp_conv}°F')
    
    else:
        temp_conv = float(round((grados - 32) * (5/9)))
        print(f'{grados}°{unidad} es equivalente a {temp_conv}°C')

conversor()