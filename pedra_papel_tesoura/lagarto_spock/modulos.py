def placar_(sorteio):
        global pontos_h
        global pontos_m
        print('-'*30)
        print(f'Você escolheu {sorteio[0]} e a máquina escolheu {sorteio[1]}')
        print(f'Logo {sorteio[2]} venceu')
        print('-'*30)
        if sorteio[2] == 'homem':
            pontos_h += 1
        elif sorteio[2] == 'maquina':
            pontos_m += 1
        print(f'# Homem {pontos_h} x {pontos_m} Máquina #')
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
            vencedor = 'maquina'
    else:
        vencedor = 'empatou'
    return humano, maquina, vencedor


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
            

