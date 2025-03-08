'''
Tabuada: Crie um programa que receba um número do usuário e 
exiba sua tabuada de multiplicação (de 1 a 10).
'''
# entrada
num = int(input('Digite uma tabuada: '))

# processamento e saida
for x in range(11):
    print(f'{num} x {x} = {num * x}')