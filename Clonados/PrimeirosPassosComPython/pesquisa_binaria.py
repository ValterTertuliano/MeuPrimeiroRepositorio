'''Com a pesquina binaria conseguimos realizar em 20 etapas o seu pior caso
considerando uma lista de 100 milhões de elementos'''

def pesquisa_binaria(lista, valor):
    # Definindo os limites inferior e superior
    esquerda = 0
    direita = len(lista) - 1
    etapas = 0
    while esquerda <= direita:
        etapas += 1
        # Encontrar o ponto médio
        meio = (esquerda + direita) // 2
        valor_meio = lista[meio]

        # Caso o valor do meio seja o que procuramos
        if valor_meio == valor:
            print(f'Etapas: {etapas}')
            return meio
        
        # Se o valor procurado for menor, movemos para a metade esquerda
        elif valor_meio > valor:
            direita = meio - 1
        
        # Se o valor procurado for maior, movemos para a metade direita
        else:
            esquerda = meio + 1

    # Se não encontrarmos o valor, retornamos -1
    print(f'Etapas {etapas}')
    return None

# Exemplo de uso
lista_ordenada = [x for x in range(100_000_001)]
valor_procurado = len(lista_ordenada) - 1

resultado = pesquisa_binaria(lista_ordenada, valor_procurado)

if resultado:
    print(f"Valor encontrado no índice: {resultado}")
else:
    print("Valor não encontrado.")
