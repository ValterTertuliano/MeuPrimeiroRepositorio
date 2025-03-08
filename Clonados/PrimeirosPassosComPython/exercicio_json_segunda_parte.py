import json

from exercicio_json import CAMINHO_DO_ARQUIVO, Pessoa

# vamos carregar o arquivo json que salvamos no modulo que importamos
with open(CAMINHO_DO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])


    

