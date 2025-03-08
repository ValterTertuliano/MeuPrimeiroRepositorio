# vamos fazer um programa que soma dois valores
# validação de Erro foi opcional

num1 = input("Digite 1° numero: ")
num2 = input("Digite 2° numero: ")

try:
    somar = float(num1) + float(num2)
except ValueError:
    print('ERRO: Digite apenas numeros.')
else:
    print('A soma de {} com {} é {}'.format(num1, num2, somar))