'''
Faça um algoritmo que leia o preço de um produto e mostre seu 
novo preço, com 5% de desconto.
'''

# entrada
preco_produto = float(input('Digite o preço do produto: '))

# processamento
desconto = preco_produto - (preco_produto * 0.05)

# saida
print(f'Preço com desconto: {desconto:,.2f}')