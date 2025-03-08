'''
Strings são cercadas por aspas simples ou duplas
podemos exibir elas com a função print()

'''
print('Isso é um texto')

# podemos salvar textos em variaveis
texto = 'Esse texto esta guardado'
print(texto)

#podemos usar aspas simples dentro de aspas duplas e vice versa
print('Meu nome é "Valter". ')
print("Meu nome é 'Valter'. ")

# ou podemos escapar as aspas
print('Meu nome é \'Valter\'. ')

'''Strings são matrizes'''

# vamos pegar a primeira letra do texto acima
print(texto[0])

# como são matrizes podemos percorrer elas com um loop
for x in 'percorrendo o texto':
    print(x)

# podemos descobrir quantos caracteres temos nessa matriz
print('Tamanho do texto: ', len(texto)) # a função len diz quantos items tem em uma matriz

# podemos verificar caracteres 
print('esta' in texto) # retorna true

# podemos usar blocos if tambem
if "texto" in texto:
    print('Estou no texto')
else:
    print('Não estou no texto')

