# Crea un programa que permita identificar si un string es o no un pangrama (que tiene todas las letras del alfabeto)

def es_pangrama(frase):
    abecedario = ['hola', 'chao']
    for letra in abecedario:
        if letra not in frase.lower():
            return False
    return True


print(es_pangrama('Benjamín pidió una de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.'))