class teste:
    def __init__(self, name):
        self.nome = name
        self.sobrenome = input("digite seu sobrenome:")
    def imprimir(self, nmeio):
        self.meio = nmeio
        print(f'Meu nome é {self.nome} {self.meio} {self.sobrenome}')

a = teste('Elias')
a.imprimir('Machado')