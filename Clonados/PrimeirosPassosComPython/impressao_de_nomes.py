'''
peça um nome para o usuario:
imprima ele 5 vezes 
cada vez em uma linha nova
'''

# entrada
nome = input('Digite um nome: ')

# processamento e saida com compreensão de lista
print()
[print(nome) for x in range(5)]