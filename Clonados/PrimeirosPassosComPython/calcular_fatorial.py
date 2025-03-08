'''
pedir um numero e calcular o fatorial
'''

# Entrada
fatorial = int(input('Digite o numero para calcular o fatorial: '))
obter_fatorial = fatorial

# processamento
resultado = 1
n = fatorial + 1 # controlar loop
for x in range(1, n):
    resultado *= obter_fatorial
    obter_fatorial -= 1

# saida
print(f'O fatorial de {fatorial} é {resultado}')