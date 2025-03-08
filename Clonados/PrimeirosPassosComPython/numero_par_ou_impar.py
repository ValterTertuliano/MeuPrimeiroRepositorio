'''
Pedir um numero para o usuario e informar se é par ou impar
'''

'''Entrada'''
# pedir um numero para o usuario
num = float(input('Digite um numero: '))

'''Processamento'''
# verificar se o numero é par
if num % 2 == 0:
    print('O numero {} é PAR',format(num))
else:
    print(f'O numero {num} é IMPAR')