from math import *
class quatro_operacoes:
    #a = 0
    #b = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b
    
    def multi(self):
        return self.a * self.b

    def subtracao(self):
        return self.a - self.b

    def divisao(self):
        return self.a / self.b

    def mostra(self):
        return f'os valores são A = {self.a} e B = {self.b}'

c, d = 2, 7
numeros = quatro_operacoes(c, d)
print(f'--> {c} + {d} = {numeros.soma():>6.2f}')
print(f'--> {c} - {d} = {numeros.subtracao():>6.2f}')
print(f'--> {c} x {d} = {quatro_operacoes(c, d).multi():>6.2f}')
print(f'--> {c} / {d} = {quatro_operacoes(c, d).divisao():>6.2f}')
print(sqrt(6**2 + 7**2))
print(4**2)
print(f'objeto "numeros", criado pela da classe "quatro_operacoes": {numeros.mostra()} ')