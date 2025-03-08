'''
Desenvolva um programa que leia as duas notas de um aluno, 
calcule e mostre a sua média.
'''

# entrada
nota1 = float(input('Digite a nota do primeiro semestre: '))
nota2 = float(input('Digite a nota do segundo semestre: '))

# processamento
media = (nota1 + nota2) / 2

# saida
print(f'A media é de {media}')
