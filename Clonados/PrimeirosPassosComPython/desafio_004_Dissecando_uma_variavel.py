'''
Faça um programa que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações possiveis 
sobre ele
'''

digito = input('Digite algo: ')

print(f'Numero: {digito.isnumeric()}')
print(f'Letra: {digito.isalpha()}')
print(f'Minusculo: {digito.islower()}')
print(f'Maiusculo: {digito.isupper()}')
print(f'Numero e letra: {digito.isalnum()}')
print(f'Ponto flutuante(decimal): {digito.isdecimal()}')
print(f'ASCII: {digito.isascii()}')
print(f'Indentificador Valido: {digito.isidentifier()}')
print(f'Espaço em braco: {digito.isspace()}')
print(f'Printavel: {digito.isprintable()}')
print(f'Titulo: {digito.istitle()}')
print(f'')
print()