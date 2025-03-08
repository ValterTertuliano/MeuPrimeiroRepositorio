'''
 Faça um programa que leia a largura e a altura de uma parede 
 em metros, calcule a sua área e a quantidade de tinta 
 necessária para pintá-la, sabendo que cada litro de tinta 
 pinta uma área de 2 metros quadrados.
'''

# entrada
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
litro_de_tinta = 2

# processamento
area = largura * altura
quantidade_de_tinta = area / litro_de_tinta

# saida
print(f'A area de {area:,.2f} m², precisa de {quantidade_de_tinta:,.2f} litros de tinta.')