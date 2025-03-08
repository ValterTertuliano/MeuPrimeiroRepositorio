# salve sua classe em JSON
# salve os dados da sua classe em json
# e depois crie novamente as instancias
# da classe com os dados salvos
# faça arquivos separados

# vamos importar o json
import json

# vamos definir um caminho para onde o arquivo vai ser salvo
CAMINHO_DO_ARQUIVO = 'desafio-json-arquivo'

# vamos iniciar uma classe pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# vamos criar algumas pessoas 
p1 = Pessoa('Valter', 30)
p2 = Pessoa('retlaV', 30)

# vamos salvar essas pessoas em uma lista
lista_pessoas = [vars(p1), p2.__dict__]

# vamos criar uma função para fazer o dump
def fazer_dump():
    # agora vamos criar o arquivo
    with open(CAMINHO_DO_ARQUIVO, 'w') as arquivo:
        json.dump(lista_pessoas, arquivo, ensure_ascii=False, indent=2)

# vamos recuperar os dados
# vou criar um novo arquivo exercicio-jason-segunda-parte

if __name__ == '__main__':
    fazer_dump()
