import requests

def obter_usuarios():
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        # Fazendo a requisição GET para a URL da API
        resposta = requests.get(url)
        # Verificando se o status da resposta é 200 (sucesso)
        resposta.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão. Verifique sua internet.")
    except requests.exceptions.Timeout:
        print("A requisição demorou muito e foi interrompida.")
    except requests.exceptions.RequestException as err:
        print(f"Ocorreu um erro: {err}")
    else:
        # A resposta é um JSON, vamos convertê-la para um objeto Python (lista de dicionários)
        usuarios = resposta.json()
    
        # Iterando sobre os usuários e exibindo os detalhes basicos
        for usuario in usuarios:

            print(f"ID: {usuario['id']}\nNome: {usuario['name']}, \nE-mail: {usuario['email']}, \nTelefone: {usuario['phone']}, \nEndereço: {usuario['address']['city']}\n")

# Chamando a função
obter_usuarios()
