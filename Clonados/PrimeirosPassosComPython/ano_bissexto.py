'''
vamos pedir pro usuario informar um ano
vamoss dizer se é bissexto ou não
'''

# entrada
ano = int(input('Digite um ano: '))

# processamento
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    # saida
    print(f'O ano de {ano} é BISSEXTO' )
else:
    # saida
    print(f'O ano de {ano} NÃO É BISSEXTO')