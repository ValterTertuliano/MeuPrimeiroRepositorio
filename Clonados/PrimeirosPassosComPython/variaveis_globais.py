''' 
Variaveis globais:
São variaveis que são criadas fora de uma função

'''

# podemos usar variaveis globais e usar elas em funções
x = 'global'

def variavel_global():
    print(f'Temos a variavel : {x}')

variavel_global()

# porem se a função tiver uma variavel local
# com o mesmo nome da global o codigo vai ter outra reação
# E a função vai receber a variavel dentro do escopo( local )

y = 'Global'
def variavel_local():
    y = 'local'
    print(f'A variavel y dentro da função é local : {y}')

variavel_local()
print(f'A variavel y fora da função: {y}')

# podemos criar uma variavel global dentro de uma função
def criar_global():
    global z
    z = 'Global criada dentro de uma função'

criar_global()
print('Acessando a variavel global criada dentro da função:\n' + z)

# podemos mudar o valor de uma variavel global dentro de uma função
# usando a mesma palavra chave global
# vamos mudar a variavel z que tem um texto grande
def mudar_global():
    global z
    z = 'alterada'

mudar_global()
print(f'O novo valor de z: {z}')