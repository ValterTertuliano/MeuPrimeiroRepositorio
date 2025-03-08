'''
converter celsius para fahrenheit
'''

'''Entrada'''
# pedir celsius para o usuario
celsius = float(input('Informe a temperatura em Celsius: '))

'''Processamento'''
# processamento
fahrenheit = (celsius * (9/5)) + 32

'''Saida'''
# Exibir o resultado
print(f'A temperatura de {celsius}° Celsius\nEquivale a {fahrenheit}° Fahrenheit')
