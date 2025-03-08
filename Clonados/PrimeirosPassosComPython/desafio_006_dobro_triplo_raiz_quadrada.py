'''
 Crie um algoritmo que leia um número e mostre o seu dobro, 
 triplo e raiz quadrada.
'''

# entrada 
numero = int(input('Digite um número: '))

# processamento
dobro = numero + numero
triplo = numero * 3
raiz_quadrada = numero ** 2

print(f'O dobro de {numero} é {dobro}')
print(f'O triplo de {numero} é {triplo}')
print(f'A raiz quadrada de {numero} é {raiz_quadrada}')