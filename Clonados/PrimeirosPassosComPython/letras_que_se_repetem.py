"""
Este programa recebe uma frase e identifica as letras que mais se repetem.
Ele exibe quantas vezes cada letra aparece e lista as 5 letras mais frequentes.
Além disso, conta o número total de caracteres no texto, ignorando os espaços em branco.

Autor: Valter Sergio Ribeiro Teruliano
Data: 23/10/1994
"""

# Entradas

# Pedir texto para o usuario
texto = input('''
              Digite qualquer Texto: \n
              ''')

# Dicionário vazio, para armazenar as letras e as repetições
letras_repetidas = {}

# Variável para contar o número total de caracteres, incluindo espaços
total_caracteres = 0

# Processamento
for x in texto.lower():
    total_caracteres += 1  # Incrementa o total de caracteres
    
    # Se o caractere não estiver no dicionário e não for um espaço
    if x not in letras_repetidas.keys():
        if not x.isspace():  # Ignora espaços em branco
            letras_repetidas[x] = 1  # Adiciona a letra ao dicionário com valor inicial 1
    else:
        letras_repetidas[x] += 1  # Incrementa o valor caso a letra já esteja no dicionário

# Exibe o dicionário com as letras e suas respectivas contagens
print("Dicionário de letras e suas frequências:")
print(letras_repetidas)

# Ordena o dicionário pelo valor (número de repetições) em ordem decrescente
dicionario = dict(sorted(letras_repetidas.items(), key=lambda x: x[1], reverse=True))

# Exibe o dicionário ordenado
print("\nDicionário ordenado por frequências:")
print(dicionario)

# Exibindo as 5 letras que mais se repetem
cont = 0
print("\nAs 5 letras mais frequentes:")
for x, y in dicionario.items():
    if cont >= 5:
        break
    else:
        cont += 1
    print(f'A letra "{x.upper()}" apareceu {y} vezes.')

# Exibe o número total de caracteres no texto (incluindo espaços)
print(f'\nO texto tem {total_caracteres} caracteres (incluindo espaços).')
