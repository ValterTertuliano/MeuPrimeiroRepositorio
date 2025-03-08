'''
Crie um programa que leia quanto dinheiro uma pessoa tem na 
carteira e mostre quantos dólares ela pode comprar.
'''

# entrada
carteira = float(input('Informe quantos reais voce tem: '))
cotacao = float(input('Informe a cotação da moeda: '))

# processamento
conversao = carteira / cotacao

# saida
print(f'Com {carteira:,.2f} Reais, você pode comprar {conversao:,.2f} dolares')
