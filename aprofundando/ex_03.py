
# https://panda.ime.usp.br/pensepy/static/pensepy/13-Classes/fracoes.html
#Classes e Objetos - Indo um pouco mais fundo - Frações

def mdc(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

def sameFraction(f1,f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())


class fracao:
    '''Classe que monta uma fração
    '''
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f'{self.numerador}/{self.denominador}'

    def getNum(self): # porque usar este metodo e não var.numerador? Na documentação do Python é assim <--
        return self.numerador

    def getDen(self):
        return self.denominador

    def simplifica(self):
        comum = mdc(self.numerador, self.denominador)
        self.numerador = self.numerador // comum
        self.denominador = self.denominador // comum
        #return f'{self.numerador}/{self.denominador}'
    
    def __add__(self, parcela):
        num = parcela.getNum()
        den = parcela.getDen()
        numera = self.numerador * den + self.denominador * num 
        denomin = self.denominador * den
        MDC = mdc(numera, denomin)
        return fracao(numera // MDC, denomin // MDC)


print('-='*40)
f = fracao(12, 16)
print(f)
print(f.numerador)
print(f.denominador)
print(f.__doc__)
print(f)
f.simplifica()
print(f)
print('-='*40)

outra = fracao(124, 248)
print(f'A fração {outra},')
# outra.simplifica()
print(f'simplificada fica {outra}')
print('-='*40)

mais = fracao(124, 248)
print(outra is mais)
m = outra # igualdade rasa
print(outra is m)
print('-='*40)
print(outra is mais)
print(sameFraction(outra, mais)) #igualdade profunda
print('-='*40)
a = fracao(256, 4096)
b = fracao(32, 1024)
res = a.__add__(b)
print(f'Soma de a = {a} e b = {b} --> {res}')
print('-='*40)
print(a + b)