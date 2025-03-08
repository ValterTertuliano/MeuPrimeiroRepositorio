# todo comentario começa com  -- > #
# ele é usado para explicar o codigo, ao mesmo tempo deixando
# o codigo mais legivel
# tambem podemos colocar comentarios no final da linha

print('Apenas para teste') # o python ignora os comentarios
# tambem podemos usar eles para impedir que linhas de codigo
# sejam executadas
# x = 10 --> como esta comentado essa declaração não vai ser feita

# o python não tem uma sintaxe para comentarios multilinhas como
# java e C, mas podemos usar 3 aspas( duplas ou simples) 
# para isso

'''
o python ignora literais de string que não são atribuidas a 
uma variavel, ou seja se voce precisar declarar variaveis com
textos bem longos, ou com uma estrutura um pouco maior podemos 
fazer isso usando essa tecnica. 
OBS:
literais de string é uma sequencia de caracteres(letras, simbolos, 
numeros, etc.)

Esses literais de string são imutaveis, qualquer operação que 
pareça modificar uma string na verdade esta criando uma nova string

'''
print("""
      Executando esse codigo
      vamos observar que 
      temos algumas linhas
      para fazer elas sem aspas triplas
      precisariamos de um comando
      print para cada linha 
      interessante, facilita muito
      e não precisamos ficar
      print
      print
      print 
      o tempo todo""")
