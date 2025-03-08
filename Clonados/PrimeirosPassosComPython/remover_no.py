class Nos:
    def __init__(self, dados):
        self.dados = dados
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    # metodo para exibir a lista linkada
    def exibir_lista(self):
        elemento = self.head
        print('\n[', end='')
        while elemento:
            print(f'{elemento.dados} ', end='')
            elemento = elemento.proximo
        print("]")

    # metodos para inserir nos
    def inserir_no_inicio(self, dados):
        novo_no = Nos(dados)
        novo_no.proximo = self.head
        self.head = novo_no

    def inserir_no_final(self, dados):
        
        # criar novo nó
        novo_no = Nos(dados) 

        # se a lista estiver vazia
        if self.head is None:
            self.head = novo_no
            return # encerra a função

        # inicia um ponteiro para percorrer as listas linkadas
        nos = self.head

        # enquanto o nó não apontar para None
        while nos.proximo is not None:
            nos = nos.proximo # movemos o ponteiro para o proximo no

        # atualizamos o ultimo nó para receber o novo  elemento no final da lista
        nos.proximo = novo_no

        # definimoss o proximo do novo nó como None por padrão
        novo_no.proximo = None

    def inserir_qualquer_posicao(self, dados, posicao):
        novo_no = Nos(dados)
        
        # verificar se a lista esta vazia ou se a posição é 1
        if self.head is None or posicao == 1:
            novo_no.proximo = self.head
            self.head = novo_no
            return # fim 
        
        # definir ponteiro para percorrer a lista
        elemento_atual = self.head

        # Percorre a lista até a posição anterior à desejada ou até o final
        for _ in range(posicao - 2):  # "-2" para parar no nó anterior à posição
            if elemento_atual is None:  # Caso a posição seja além do tamanho atual
                break
            elemento_atual = elemento_atual.proximo
                
        # Caso a posição seja maior que o tamanho da lista, insere no final
        if elemento_atual is None:
            print("Posição além do tamanho atual da lista. Inserindo no final.")
            elemento_atual = self.head
            while elemento_atual.proximo is not None:
                elemento_atual = elemento_atual.proximo
            elemento_atual.proximo = novo_no
            return

        # Insere o novo nó na posição desejada
        novo_no.proximo = elemento_atual.proximo
        elemento_atual.proximo = novo_no       
    
    # metodos para deletar Nós
    def deletar_primeiro_no(self):
        if self.head is None:
            return # encerra a função a lista esta vazia
        self.head = self.head.proximo

    def deletar_ultimo_no(self):
        lista_linkada = self.head
        
        if self.head is None or self.head.proximo is None:
            return # encerra a função
        
        while lista_linkada.proximo.proximo is not None:
            lista_linkada = lista_linkada.proximo
        lista_linkada.proximo = None


if __name__ == "__main__":
    lista_encadeada = ListaEncadeada()
    lista_encadeada.inserir_no_inicio('A')
    lista_encadeada.inserir_no_inicio('B')
    lista_encadeada.inserir_no_inicio('C')
    lista_encadeada.inserir_no_inicio('D')

    lista_encadeada.exibir_lista()

    lista_encadeada.deletar_primeiro_no()
    lista_encadeada.deletar_ultimo_no()
    lista_encadeada.exibir_lista()
    
    lista_encadeada.inserir_no_final('E')
    lista_encadeada.inserir_qualquer_posicao("F", 2)
    lista_encadeada.exibir_lista()
    