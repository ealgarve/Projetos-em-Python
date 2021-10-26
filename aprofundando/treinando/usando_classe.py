class teste:
    def __init__(self, name):
        self.nome = name
        self.sobrenome = input("digite seu sobrenome:")
    def imprimir(self):
        print(f'Meu nome é {self.nome} {self.sobrenome}')

a = teste('Elias')
a.imprimir()