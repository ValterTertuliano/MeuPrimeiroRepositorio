'''
Classificação de Notas: Peça uma nota ao usuário e exiba 
"Aprovado" se a nota for maior ou igual a 7, "Recuperação" se 
for entre 5 e 7, e "Reprovado" se for abaixo de 5.
'''

# entrada
nota = float(input('Digite a nota: '))

# processamento e saída
if nota >= 7:
    print('Aprovado')
elif 5 <= nota < 7:
    print('Recuperação')
else:
    print('Reprovado')