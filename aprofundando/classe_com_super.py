class Pai(object):
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
  
  
class Filha(Pai):
    def __init__(self, peso, altura, cabelo):
        super().__init__(peso, altura) # herança do construtor
        self.cabelo = cabelo # pode ter também um novo parametro

    def mostra(self):
        print(f'Meu peso é {filhota.peso:_>11.2f} kg', end='\n')
        print(f'Minha altura é {filhota.altura:_>7.2f} m', end='.\n')
        print(f'A cor do meu cabelo é {filhota.cabelo}.')

filhota = Filha(73.216, 1.7, "castanho")
filhota.mostra()

