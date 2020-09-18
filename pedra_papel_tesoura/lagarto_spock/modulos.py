def placar(sorteio, rodada = 1):
    if rodada == 1:
        jogador1 = jogador2 = 0
        rodada += 1
    if sorteio[2] == 'homem':
        jogador1 += 1
    elif sorteio[2] == 'maquina':
        jogador2 += 1
    else:
        print('Algo deu Errado.')
    print('-'*30)
    print(f'Você escolheu {sorteio[0]} e a máquina escolheu {sorteio[1]}')
    print(f'Logo {sorteio[2]} venceu')
    print('-'*30)
    print(f'# Homem {jogador1} x {jogador2} Máquina #')
    print('-'*30)

from time import sleep
placar(['pedra', 'papel', 'maquina'])
sleep(1)
placar(['spock', 'lagarto', 'maquina'])
sleep(1)
placar(['perda', 'lagarto', 'homem'])

def sorteio(humano = 'papel'):
    import random
    maquina = random.choice(['pedra', 'papel', 'tesoura', 'lagarto', 'spock'])
    if maquina != humano:
        if humano == 'pedra' and (maquina == 'lagarto' or maquina == 'tesoura'):
            vencedor = 'homem'
        elif humano == 'papel' and (maquina == 'pedra' or maquina == 'spock'):
            vencedor = 'homem'
        elif humano == 'tesoura' and (maquina == 'lagarto' or maquina == 'papel'):
            vencedor = 'homem'
        elif humano == 'lagarto' and (maquina == 'spock' or maquina == 'papel'):
            vencedor = 'homem'
        elif humano == "spock" and (maquina == 'pedra' or maquina == 'tesoura'):
            vencedor = 'homem'
        else:
            vencedor = 'maquina'
    else:
        vencedor = 'empate'
    return humano, maquina, vencedor

#print(list(sorteio('pedra')))

def menu():
    print('''Digite:
[1] para "Pedra"
[2] para "Papel"
[3] para "Tesoura"
[4] para "Lagarto"
[5] para "Spock"
[S] Sair''')
    homem = str(input('Digite sua opção: ')).lower()
    if homem == '1':
        homem = 'pedra'
    elif homem == '2':
        homem = 'papel'
    elif homem == '3':
        homem = 'tesoura'
    elif homem == '4':
        homem = 'lagarto'
    elif homem == '5':
        homem = 'spock'
    elif homem == 's':
        homem = 'sair'
    else:
        if homem not in '12345s':
            homem = 'ERRO - digite uma opção correta'
    return homem
            

'''while True:
    if menu() == 'sair':
        break
    else:
        print('-'*15)
        print(menu())
        print('-'*15)'''

#placar(5, 3, 'Elias', 'Pati')
#sorteio('spock')
