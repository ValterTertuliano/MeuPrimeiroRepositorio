# Seção 1: Manipulação de Dados
# Problema 1: Filtrando dados de uma lista de dicionários
# Você tem uma lista de dicionários que representam usuários, onde 
# cada dicionário contém as chaves nome, idade, e cidade. Seu 
# objetivo é filtrar todos os usuários com mais de 30 anos que 
# vivem na cidade de São Paulo.

usuarios = [
    {"nome": "Ana", "idade": 28, "cidade": "Rio de Janeiro"},
    {"nome": "Carlos", "idade": 34, "cidade": "São Paulo"},
    {"nome": "Beatriz", "idade": 42, "cidade": "São Paulo"},
    {"nome": "Daniel", "idade": 19, "cidade": "Brasília"},
    {"nome": "Eduarda", "idade": 31, "cidade": "São Paulo"}
]

# Implemente sua solução aqui

# Compreensões de lista são mais rápidas e eficientes para operações simples
filtrados = [x for x in usuarios if x["cidade"] == "São Paulo" and x['idade'] >= 30]

# loop for tradicional - pode ser ligeiramente mais lento que a compreensão de lista
filtrados2 = []

for x in usuarios:
    if (x['idade'] >= 30) and (x['cidade'] == "São Paulo"):
        filtrados2.append(x)


print('Compreensão de lista')
print(filtrados)
print('Com "for" tradicional')
print(filtrados2)