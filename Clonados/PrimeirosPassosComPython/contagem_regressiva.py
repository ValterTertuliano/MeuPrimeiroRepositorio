'''
criar um contador regressivo
'''

import time # comando sleep para controlar a contagem
import os # comando os para limpar a tela do terminal

# para limpar a tela e exibir apenas o contador
os.system('cls')

for x in range(10, 0, -1):
    print(x)
    time.sleep(1)
    os.system('cls')

print('Contador chegou ao fim')