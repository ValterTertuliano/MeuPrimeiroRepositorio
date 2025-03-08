'''
peça para o usuario:
quantos reais quer converter
a cotação do dolar
'''

# entrada
real = float(input('Quantos REAIS deseja converter: '))
dolar = float(input('Qual o valor do DOLAR: '))

# processamento
total = real * dolar

# saida
print(f'{real:,.2f} reais é igual {total:,.2f} dolares !!!')