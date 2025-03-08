# Variaveis são containeres para armazenar valores de dados
# o python não tem um comando para declarar uma variavel
# sendo ela criada no momento que voce atribui algum valor
# a ela

variavel = 5 # a variavel tem um numero do tipo inteiro
print(variavel) # vamos ver o valor que esta guardado dentro dessa variavel

# podemos mudar o tipo de dado de uma variavel depois que ela é 
# declarada
variavel = 'Não é mais numero, e sim uma string(texto)'
print(variavel)# esse tipo de mudança não causará erro

# mas por algum motivo é possivel que agente possa especificar 
# o tipo de dado de uma variavel
x, y, z = str(3), int(3), float(3) 
# nessa linha criamos 3 variaveis
'''
str(3) é passado para x, int(3) para y e float(3) para z
agora podemos verificar os tipos de dados na variavel
'''
print(type(x), x) # class string
print(type(y), y) # class int
print(type(z), z) # class float

# o python é sensitivecase, ele diferencia maiusculas de minusculas
# por exemplo:
casa = 'casa'
Casa = 'asac'
print(casa, Casa, '--> isso pode gerar erros, fique atento')
