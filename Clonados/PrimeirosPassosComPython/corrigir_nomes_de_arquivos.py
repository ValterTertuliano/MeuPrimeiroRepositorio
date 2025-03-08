import os

# pegar o caminho da pasta 
CAMINHO_DA_PASTA = "C:\\Users\\valte\\Desktop\\Python\\livro - automatizar tarefas massantes com python\\parte I - basico da programação python"

for x in os.listdir(CAMINHO_DA_PASTA):
    
    # concatenar o caminho do arquivo com o nome da pasta
    caminho_completo = os.path.join(CAMINHO_DA_PASTA, x)

    # verificar se o caminho se refere a um arquivo
    if os.path.isfile(caminho_completo):

        # se for vamos corrigir o erro de nomenclatura dos arquivos
        formatar = x.replace('-', '_')

        # vamos modificar o caminho original pelo caminho com a correção feita
        caminho_formatado = os.path.join(CAMINHO_DA_PASTA, formatar)

        # agora podemos renomear o arquivo com segurança
        os.rename(caminho_completo, caminho_formatado)