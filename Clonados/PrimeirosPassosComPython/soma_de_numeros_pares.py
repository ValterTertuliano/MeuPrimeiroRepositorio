'''
Soma de Números Pares: Crie um loop que some todos os números 
pares de 1 a 100.
'''


# primeiro teste
somar_numeros_pares = 0
for x in range(0, 101, 2):
    # print(x)
    somar_numeros_pares += x

print(somar_numeros_pares)

# segundo teste
lista_de_pares = sum([x for x in range(0, 101, 2)])
print(lista_de_pares)

