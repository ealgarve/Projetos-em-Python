# Classes e Objetos - Fundamentos
# https://panda.ime.usp.br/pensepy/static/pensepy/13-Classes/classesintro.html
# C:\Users\ealga\Documents\ProjetosGitHub\Projetos-em-Python\aprofundando\Classes e Objetos - Fundamentos.pdf
from math import sqrt
import os

class Point:    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return sqrt(self.x**2 + self.y**2)

    def __str__(self): #sem este modulo p = Point(2, 4); print(p) --> resultaria em <__main__.Point object>
        return f'({self.x}, {self.y})'

    def halfway(self, target):
        Xm = (self.x + target.x) / 2
        Ym = (self.y + target.y) / 2
        return Point(Xm, Ym)

    def distancia(self, alvo):
        xdif = self.x - alvo.x
        ydif = self.y - alvo.y
        return sqrt(xdif**2 + ydif**2)

    def reflect_x(self):
        x = self.x
        y = - self.y
        return Point(x, y)

    def slope_from_origin(self):
        try:
            return self.y / self.x
        except ZeroDivisionError:
            print('Deu erro: Divisão por zero em inclinação em relação a origem.')

    def slope_a_b(self, b):
        return (self.y - b.y) / (self.x - b.x)

    def get_line_to(self, b):
        m = (self.y - b.y) / (self.x - b.x)
        c = self.y -m * self.x
        return m, c

    def centro(self):
        '''Dados quatro pontos sobre uma circunferência, encontre o ponto centro da circunferência. 
        '''
        pass

os.system('cls')
print('A classe dos pontos:')
ax = 1 # float(input('Entre com o ponto [ax]: '))
ay = 2 # float(input('Entre com o ponto [ay]: '))
a = Point(ax, ay)
bx = 3 # float(input('Entre com o ponto [bx]: '))
by = 4 # float(input('Entre com o ponto [by]: '))
b =Point(bx, by)
print(f'Distância até a origem do ponto a({ax}, {ay}): {a.distanceFromOrigin():.2f}')
print(f'Distância até a origem do ponto b({bx}, {by}): {b.distanceFromOrigin():.2f}')
print(f'Distância entre a({ax}, {ay}) e b({bx}, {by}): {a.distancia(b):.2f}')
print(f'O ponto médio entre a({ax}, {bx}) e b({bx}, {by}): {a.halfway(b)}')
print(f'Ponto a({ax}, {ay}), refletido no eixo X: {a.reflect_x()}')
print(f'Ponto b({bx}, {by}), refletido no eixo X: {b.reflect_x()}')
print(f'Inclinação da reta formada entre o ponto a({ax}, {ay}) e a origem: {a.slope_from_origin()}')
print(f'Inclinação da reta formada entre o ponto a({ax}, {ay}) e b({bx}, {by}): {a.slope_a_b(b)}')
print(f'Equação da reta formada pelos pontos a({ax}, {ay}) e b({bx}, {by}): Y = {a.get_line_to(b)[0]}.X + {a.get_line_to(b)[1]}')

