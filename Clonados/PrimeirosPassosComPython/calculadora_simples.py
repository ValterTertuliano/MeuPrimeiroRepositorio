'''
Calculadora simples apenas demonstrar 
conhecimento na sintaxe basica do python
'''

''' Entradas '''
# pedir numero 1
num1 = float(input('Digite um número: '))

# pedir numero 2
num2 = float(input('Digite um segundo número: '))

''' Processamento '''
# somar valores
somar = num1 + num2

# subtrair valores
subtrair = num1 - num2

# multiplicar valores
multiplicar = num1 * num2

# dividir valores
dividir = num1 / num2

''' Saidas '''
# exibindo os valores das operações
print(f'\nA soma de {num1} + {num2} é igual a {somar}')
print('\nA subtração de {} - {} é igual a {}'.format(num1, num2, subtrair))
print('\nA multiplicação de ', num1, ' x ', num2, 'é igual a ', multiplicar)
print(f'\nA divisão de {num1} / {num2} é {dividir}')

