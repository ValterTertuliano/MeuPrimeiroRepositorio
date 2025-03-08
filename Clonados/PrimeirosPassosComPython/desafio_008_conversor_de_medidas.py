'''
Escreva um programa que leia um valor em metros e o exiba 
convertido em centímetros e milímetros.
'''

# entrada
metros = float(input('Informe Metragem: '))

# processamento
centimetros = metros * 100
milimetros = centimetros * 10

# saida
print(f'{metros:,.2f} metros tem {centimetros} centimetros')
print(f'{metros:,.2f} metros tem {milimetros} milimetros')