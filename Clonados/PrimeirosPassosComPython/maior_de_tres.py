'''
peça 3 numeros para o usuario e exiba o maior
'''

# entrada
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))

# processsamento
lista = []
lista.append(num1)
lista.append(num2)
lista.append(num3)
lista = sorted(lista, reverse=True)

# saida
print(f'O maior numero é o {lista[0]}')