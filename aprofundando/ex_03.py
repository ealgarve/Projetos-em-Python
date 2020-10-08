
# https://panda.ime.usp.br/pensepy/static/pensepy/13-Classes/fracoes.html
#Classes e Objetos - Indo um pouco mais fundo - Frações

def mdc(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn

    return n


class fracao:
    '''Classe que monta uma fração
    '''
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f'numerador/denominador = {self.numerador}/{self.denominador}'

    def getNum(self): # porque usar este metodo e não var.numerador? Na documentação do Python é assim <--
        return self.numerador

    def getDen(self):
        return self.denominador

    def simplifica(self):
        comum = mdc(self.numerador, self.denominador)
        self.numerador = self.numerador // comum
        self.denominador = self.denominador // comum
        return f'{self.numerador}/{self.denominador}'

f = fracao(12, 16)
print(f)
print(f.numerador)
print(f.denominador)
print(f.__doc__)
print(f.simplifica())
print(f)




