'''
Faça um programa que leia um número Inteiro e mostre na tela 
o seu sucessor e seu antecessor.
'''

# entrada 
numero = int(input('Informe um número: '))

# processamento
antes = numero - 1
depois = numero + 1

# saida
print(f'O antecessor de {numero}: {antes}')
print(f'O sucessor de {numero}: {depois}')