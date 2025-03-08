'''
Jogo de Adivinhação: O programa escolhe um número aleatório 
entre 1 e 10, e o usuário deve tentar adivinhar. O programa 
dá dicas se o número é maior ou menor.
'''

# importar o choice para selecionar o numero para adivinha
from random import choice

print('Bem vindo ao jogo de adivinhação. ')

# entrada
numero_secreto = choice([x for x in range(1, 11)])
tentativas = 0
pontos = 0

while True:
    if tentativas < 10:
        print(f'Você tem {10 - tentativas} tentativas restantes.')
    else:
        print("Suas chances acabaram...")
        break

    try:
        escolha = int(input("Escolha um número, ou digite ZERO para sair: "))

        if escolha == 0:
            print(f'Saindo do jogo...')
            break
        
        elif escolha == numero_secreto:
            print("Parabéns, você ganhou !!!")
            pontos = (10 - tentativas) * 10
            print(f"Você fez {pontos} pontos.")
            break

        elif escolha > numero_secreto:
            print("Você escolheu um número MAIOR. Tente novamente.")
        
        elif escolha < numero_secreto:
            print("Você escolheu um número MENOR. Tente novamente.")

        # depois de verificar tudo adiciona uma tentativa e segue
        tentativas += 1

    except ValueError:
        print('ERRO: Digite apenas números, ou digite 0 (ZERO) para sair.')
