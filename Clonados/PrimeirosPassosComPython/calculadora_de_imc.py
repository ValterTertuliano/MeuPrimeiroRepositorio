'''
vamos pedir para o usuario:
peso e altura
e retornar o IMC
'''

# entrada
peso = float(input('Quantos kilos tem: '))
altura = float(input('Digite a altura: '))

# processamento
imc = peso / (altura ** 2 )

# saida 
print(f'Seu IMC é de {imc:,.2f}')