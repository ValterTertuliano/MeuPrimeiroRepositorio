'''
Contagem de Vogais: Peça uma palavra ao usuário e conte 
quantas vogais (a, e, i, o, u) ela possui.
'''

# manualmente
def contar_na_mao():

    contador = {
        'a':0,
        'e':0,
        'i':0,
        'o':0,
        'u':0,
    }

    texto = input( '''
                Aqui pode escrever qualquer texto
                ''')

    for x in texto.lower():
        if x in contador:
            contador[x] += 1

    for x, y in contador.items():
        print(f'Vogal: {x} Repetições: {y}')


contar_na_mao()

# automaticamente
# from collections import Counter

# entrada 
# texto = input('digite qualquer coisa')
# contar_letras = Counter(texto)
# print(f'A vogal A:')
# print(f'apareceu {contar_letras['a']} MINUSCULAS')
# print(f'apareceu {contar_letras['A']} MAIUSCULAS')

# print(f'A vogal E:')
# print(f'apareceu {contar_letras['e']} MINUSCULAS')
# print(f'apareceu {contar_letras['E']} MAIUSCULAS')

# print(f'A vogal I:')
# print(f'apareceu {contar_letras['o']} MINUSCULAS')
# print(f'apareceu {contar_letras['O']} MAIUSCULAS')

# print(f'A vogal O:')
# print(f'apareceu {contar_letras['o']} MINUSCULAS')
# print(f'apareceu {contar_letras['O']} MAIUSCULAS')

# print(f'A vogal U:')
# print(f'apareceu {contar_letras['u']} MINUSCULAS')
# print(f'apareceu {contar_letras['U']} MAIUSCULAS')