class Animal:

    def __init__(self, nome):
        self.nome = nome

    def comendo(self, alimento):
        return f'O {self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    
leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('maçã'))