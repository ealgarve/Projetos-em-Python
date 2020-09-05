def placar(jogador1 = 0, jogador2 = 0, nome1 = 'homem', nome2 = 'máquina'):
	print('-'*30)
	print(f'# {nome1} {jogador1} x {jogador2} {nome2} #')
	print('-'*30)
	
def sorteio(humano = 'papel'):
	    maquina = random.choice(['pedra', 'papel', 'tesoura'])
    if maquina != humano:
    	if máquina == 'pedra' and humano != 'papel':
    		print('máquina venceu')
    	else:
    		print('humano venceu')
    else:
    	print('houve um empate')
	
placar(5, 3, 'Elias', 'Pati')