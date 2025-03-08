'''
Faça um algoritmo que leia o salário de um funcionário e 
mostre seu novo salário, com 15% de aumento.
'''

# entrada
salario = float(input('Digite o salário: '))

# processamento
reajuste = salario * 1.15

# saida
print(f'O salario de {salario:,.2f} foi reajustado para {reajuste:,.2f} ')