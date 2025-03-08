import string

# aqui conseguimos uma string com todas as letras do alfabeto
todas_as_letras = string.ascii_letters
print(todas_as_letras)
print()

# tambem podemos pegar apenas as letras maiusculas
print(string.ascii_uppercase)
print()

# tambem podemos pegar apenas as letras minusculas
print(string.ascii_lowercase)
print()

# tambem podemos pegar todos os numeros
print(string.digits)
print()

# tambem podemos pegar todos os caracteres de pontuação
print(string.punctuation)
print()

# até mesmo a representação de espaços em branco 
print(repr(string.whitespace))
print()

# tambem podemos usar scape com a biblioteca string e a bibliota re
import re
print(re.escape(string.punctuation))
print()

# ela possui os metodos de string, como upper, lower, title, strip, split, replace e etc.
# alem disso para varias dessas funções não é necesssario importar a biblioteca

