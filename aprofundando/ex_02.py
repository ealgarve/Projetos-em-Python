# do site: https://pense-python.caravela.club/15-classes-e-objetos/09-exercicios.html
'''
15.9 - Exercícios
Exercício 15.1
1 - Escreva uma definição para uma classe denominada Circle, com os atributos center e radius, onde center é um objeto Point e radius é um número.
'''
from math import *
class Circle:
    center = [0, 0]
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f'centro = ({self.center[0]}, {self.center[1]}), raio = {self.radius}'

    def point_in_circle(self, ponto):
        xdist = self.center[0] - ponto[0]
        ydist = self.center[1] - ponto[1]
        dist = sqrt(xdist**2 + ydist**2)
        if dist <= self.radius:
            return True
        else:
            return False

    def rectangle_in_circle(self, circulo, pontos):
        dentro = True
        cont = 0
        ret = retangulo(pontos)
        if ret.eh_retangulo() == True:
            while dentro == True and cont < len(pontos):
                if circulo.point_in_circle(pontos[cont]) == True:
                    dentro = True
                else:
                    dentro = False
                    break
                cont +=1
            return dentro
        else:
            return 'os pontos fornecidos não formam um retangulo'

class retangulo: # Verifica se os 4 pontos fornecidos formam um retangulo
    def __init__(self, pontos):
        self.pontos = pontos # [A, B, C, D]
        
    def __str__(self):
        A = self.pontos[0]
        B = self.pontos[1]
        C = self.pontos[2]
        D = self.pontos[3]
        return f'Os pontos {A}, {B}, {C}, {D}, formam um retangulo?'
        
    def eh_retangulo(self):
        A = self.pontos[0]
        B = self.pontos[1]
        C = self.pontos[2]
        D = self.pontos[3]
        distAB = sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)
        distBC = sqrt((C[0] - B[0])**2 + (B[1] - C[1])**2)
        distCD = sqrt((C[0] - D[0])**2 + (C[1] - D[1])**2)
        distDA = sqrt((D[0] - A[0])**2 + (A[1] - D[1])**2)
        if distDA == distBC and distAB == distCD:
            return True
        else:
            return False

# Retangulo
print('-='*30)
print('### Verifica se os pontos formam um retangulo ###')
rr = retangulo([[1, 2], [1, 4], [3, 4], [3, 2]])
rr_2 = retangulo([[1, 3], [4, 6], [6, 4], [3, 1]])
rr_3 = retangulo([[3, 1], [4, 6], [1, 3], [6, 4]])
print(rr, f'{"sim" if rr.eh_retangulo() else "não"}')
print(rr_2, f'{"sim" if rr_2.eh_retangulo() else "não"}')   
print(rr_3, f'{"sim" if rr_3.eh_retangulo() else "não"}')
print('-='*30)

# Circulo
print('### Verifica se um ponto esta dentro do circulo ###')
a = Circle([150, 100], 75)
print(a)
ponto = [150, 175.001]
v = a.point_in_circle(ponto)
print(f'Verificando o circulo de {a}')
print(f'O ponto ({ponto[0]}, {ponto[1]}) esta dentro do circulo: {v}')

# Retangulo dentro do circulo
print('-='*30)
print('### Verifica se os pontos formam um retangulo e se ele esta dentro do circulo')
# pontos = [[80, 100], [85,100], [150,176], [160, 100]]
pontos = [[75, 100], [150,175], [225,100], [150, 25]]
r = a.rectangle_in_circle(a, pontos)
print(f'Os pontos {pontos} estão dentro do circulo? {r}')
print('-='*30)