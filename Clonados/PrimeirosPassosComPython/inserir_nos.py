class nos:
    def __init__(self, dados=None):
        self.dados = dados # armazena o valor do nó
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self):
        self.cabeca = None # inicio da lista

    def exibir_lista(self):
        elemento_atual = self.cabeca

        print('Lista Encadeada Simples - SLL')
        while elemento_atual is not None:
            print(elemento_atual.dados) # exiba o valor que esta no nó
            elemento_atual = elemento_atual.proximo # avança para o proximo endereço

    def adicionar_no_inicio(self, novo_dado):
        novo_no = nos(novo_dado) # cria um novo Nó com o valor fornecido
        novo_no.proximo = self.cabeca # faz o novo nó apontar para o nó atual no inicio da lista
        self.cabeca = novo_no # troca o nó inicial pelo novo


lista1 = ListaEncadeadaSimples()
lista1.cabeca = nos('A')

elemento2 = nos('B')
elemento3 = nos('C')

lista1.cabeca.proximo = elemento2
elemento2.proximo = elemento3

lista1.adicionar_no_inicio('D')
lista1.exibir_lista()