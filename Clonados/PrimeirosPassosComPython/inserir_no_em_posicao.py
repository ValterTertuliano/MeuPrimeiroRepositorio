class No:
    def __init__(self, dados):
        self.dados = dados
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self):
        self.cabeca = None

    def imprimir_lista(self):
        elemento_atual = self.cabeca

        print('Lista encadeada: ')
        while elemento_atual is not None:
            print('Dados: ', elemento_atual.dados)
            elemento_atual = elemento_atual.proximo

    def inserir_apos(self, no_na_posicao, novo_dado):
      if no_na_posicao is None:
         print("O nó especificado está ausente")
         return
      
      novo_no = No(novo_dado)       # Cria um novo nó com o dado fornecido
      novo_no.proximo = no_na_posicao.proximo # Novo nó aponta para o próximo do nó especificado
      no_na_posicao.proximo = novo_no # Atualiza o nó especificado para apontar para o novo nó

# Exemplo de uso da lista encadeada
lista1 = ListaEncadeadaSimples()
lista1.cabeca = No("A")
elemento2 = No("B")
elemento3 = No("C")

# Conectando os elementos na lista
lista1.cabeca.proximo = elemento2
elemento2.proximo = elemento3

# Inserindo um novo nó após o segundo nó (elemento2) com o valor "D"
lista1.inserir_apos(lista1.cabeca.proximo, "D")
lista1.imprimir_lista()