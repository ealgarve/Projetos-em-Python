'''Exercício Python 45: Crie um programa que
faça o computador jogar Jokenpô com você.
'''
import random
import time
import emoji
import unicodedata

print('Jogo "Pedra, Papel e Tesoura"')  
# mao = str(input('Digite sua opção: ')).lower()
mao = '5'
while mao != '0':
    print('''Digite:
[1] para "Pedra"
[2] para "Papel"
[3] para "Tesoura"
[S] Sair''')
    mao = str(input('Digite sua opção: ')).lower()
    if mao == '1':
        mao = 'pedra'
    elif mao == '2':
        mao = 'papel'
    elif mao == '3':
        mao = 'tesoura'
    elif mao == 's':
        break
    print('PEDRA')
    time.sleep(1)
    print('PAPEL')
    time.sleep(1)
    print('TESOURA!!!')
    time.sleep(1)
    sorteio = random.choice(['pedra', 'papel', 'tesoura'])
    if sorteio != mao:
        if (sorteio == 'pedra' and mao != 'papel') or (sorteio == 'papel' and mao != 'tesoura') or (sorteio == 'tesoura' and mao != 'pedra'):
            print("-="*19)
            print(emoji.emojize(' :computer:', use_aliases=True), '{} - você: {}' .format(sorteio, mao))
            print(emoji.emojize('Eu, o :computer:, venci!', use_aliases=True))
            print("-="*19)
            #time.sleep(3)
        else:
            print("-="*19)
            print('Computador: {} - Você: {}' .format(sorteio, mao))
            print('Você venceu, parabéns!')
            print("-="*19)
        #time.sleep(3)            
        pass
    else:
        print("-="*19)
        print('Empatamos! Ambos escolhemos {}' .format(sorteio))
        print("-="*19)
        #time.sleep(3)