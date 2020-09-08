def placar(sorteio, rodada = 1):
    if rodada == 1:
        jogador1 = jogador2 = 0
    else:
        if vencedor == nome1:
            jogador1 += 1
        print('-'*30)
        print(f'# {nome1} {jogador1} x {jogador2} {nome2} #')
        print('-'*30)

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
            vencedor = 'robo'
    else:
        vencedor = 'empate'
    return humano, maquina, vencedor

print(list(sorteio('pedra')))

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
