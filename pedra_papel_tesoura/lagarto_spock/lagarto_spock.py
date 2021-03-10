'''Exercício Python 45: Crie um programa que
faça o computador jogar Jokenpô com você.
'''

def placar(sorteio):
        global pontos_h
        global pontos_m
        global rodada
        print('-'*30)
        print(f'Rodada {rodada}')
        print(f'Você escolheu {sorteio[0]} e a máquina escolheu {sorteio[1]}')
        print(f'Logo {sorteio[2]} venceu')
        print('-'*30)
        if sorteio[2] == 'homem':
            pontos_h += 1
        elif sorteio[2] == 'maquina':
            pontos_m += 1
        print(f'# Homem {pontos_h} x {pontos_m} Máquina #')
        print('-'*30)

from time import sleep
from modulos import *
rodada = 1
pontos_h = 0
pontos_m = 0
while True:
    #print(f'Rodada {rodada}')
    placar(sorteio(menu()))
    print('-'*30)
    sleep(1)
    if rodada == 3 or menu() == 'sair': 
        break
    rodada += 1    


'''from time import sleep
placar(['pedra', 'papel', 'maquina'])
sleep(1)
placar(['spock', 'lagarto', 'maquina'])
sleep(1)
placar(['perda', 'lagarto', 'homem'])'''