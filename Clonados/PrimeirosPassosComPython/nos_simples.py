class nos:
    def __init__(self, dados):
        self.dados = dados
        self.prox = None

# definindo os nós
node_A = nos('A')
node_B = nos('B')
node_C = nos("C")

# vinculando os nós
node_A.prox = node_B # nó A aponta para o B
node_B.prox = node_C # nó B aponta para o C

# chamando os nós
lista_de_nos = node_A
while lista_de_nos:
    print(lista_de_nos.dados, end=" -> ") # exibe os dados dos nos
    lista_de_nos = lista_de_nos.prox # aponta para o proximo endereço
print('Fim')