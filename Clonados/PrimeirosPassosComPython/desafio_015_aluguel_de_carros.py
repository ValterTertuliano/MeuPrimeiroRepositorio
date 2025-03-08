'''
Escreva um programa que pergunte a quantidade de Km 
percorridos por um carro alugado e a quantidade de dias pelos 
quais ele foi alugado. Calcule o preço a pagar, sabendo que o 
carro custa R$60 por dia e R$0,15 por Km rodado.
'''

# entrada
dia = int(input('Quantos dias com o carro: '))
km = float(input('Quantos Kilometros rodado: '))
preco_dia = 60
preco_km = 0.15

# processamento
pagar_aluguel = (dia * preco_dia) + (km * preco_km)

# saida
print(f'O aluguel do carro ficou {pagar_aluguel:,.2f} reais ')
