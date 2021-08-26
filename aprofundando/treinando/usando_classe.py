class teste:
    def __init__(self, name):
        self.nome = name
    def imprimir(self):
        print(f'Meu nome é {self.nome}')

a = teste('Elias')
a.imprimir()