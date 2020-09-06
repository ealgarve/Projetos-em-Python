def placar(jogador1 = 0, jogador2 = 0, nome1 = 'homem', nome2 = 'máquina'):
    print('-'*30)
    print(f'# {nome1} {jogador1} x {jogador2} {nome2} #')
    print('-'*30)

def sorteio(humano = 'papel'):
    import random
    maquina = random.choice(['pedra', 'papel', 'tesoura', 'lagarto', 'spock'])
    if maquina != humano:
        if humano == 'pedra' and (maquina == 'lagarto' or maquina == 'tesoura'):
            print(f'Humano escolheu [{humano}] X Máquina escolheu [{maquina}]')
            print('Humano venceu.')
        elif humano == 'papel' and (maquina == 'pedra' or maquina == 'spock'):
            print(f'Humano escolheu [{humano}] X Máquina escolheu [{maquina}]')
            print('Humano venceu')
        elif humano == 'tesoura' and (maquina == 'lagarto' or maquina == 'papel'):
            print(f'Humano escolheu [{humano}] X Máquina escolheu [{maquina}]')
            print('Humano venceu')
        elif humano == 'lagarto' and (maquina == 'spock' or maquina == 'papel'):
            print(f'Humano escolheu [{humano}] X Máquina escolheu [{maquina}]')
            print('Humano venceu')
        elif humano == "spock" and (maquina == 'pedra' or maquina == 'tesoura'):
            print(f'Humano escolheu [{humano}] X Máquina escolheu [{maquina}]')
            print('Humano venceu')
        else:
            print(f'Humano escolheu [{humano}] X Máquina escolheu [{maquina}]')
            print('Máquina Venceu')
    else:
        print(f'Humano escolheu [{humano}] X Máquina escolheu [{maquina}]')
        print('Houve um empate')


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
            

while True:
    if menu() == 'sair':
        break
    else:
        print('-'*15)
        print(menu())
        print('-'*15)

#placar(5, 3, 'Elias', 'Pati')
#sorteio('spock')
