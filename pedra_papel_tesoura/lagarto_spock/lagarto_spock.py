'''Exercício Python 45: Crie um programa que
faça o computador jogar Jokenpô com você.
'''
import random
import time
import emoji
import unicodedata
from modulos import *
saida = ''
print('Jogo "Pedra, Papel e Tesoura"') 
while saida != 'sair':  
    saida = menu()  
    sorteio(saida)
