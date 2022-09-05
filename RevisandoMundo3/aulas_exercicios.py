import re


def aula_16():
    lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
    #lanche[2] = 'sorvete' # a tupla é imutável
    print(lanche)
    for c in lanche:
        print(f'Eu vou comer {c}')

    for cont in range(0, len(lanche)):
        print(f'Eu vou comer [{cont}] {lanche[cont]}')

    for num, coisa in enumerate(lanche):
        print(f'Eu vou comer [{num}] {coisa}')

    print(sorted(lanche))    

#aula_16()

def exercicio_72():
    numeros = ('zero', 'um', 'dois', 'três', 'quato', 'cinco', 'seis', 'sete', 'oito', 'nove')
    
    while True:
        num = int(input(f'Digite um número entre 0 e 9: '))
        if 0 <= num <= 9:
            print(f'Você digitou o numero {num}: {numeros[num]}')
            repetir = str(input(f'tecle s para sair ou enter para continuar'))
            if repetir == 's':
                break 
        print(f'tente outra vez: ')
        

#exercicio_72()


def exercicio_72():
    times = ('Bahia', 'Brusque', 'Chapecoense', 'CRB', 'Criciúma', 'Cruzeiro', 'CSA', 'Guarani', 'Atlético Mineiro', 'Botafogo', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Santos', 'Inter SM', 'Grêmio', 'Inter', 'Brasil de Pelotas', 'Guarani')
    print(f'Os 5 primeiros times são: {times[:5]}')
    print(f'Os 4 últimos times são: {times[-4:]}')
    print(f'Em ordem alfabetica: {sorted(times)}')
    print(f'Time [{times[times.index("Chapecoense")]}]: {times.index("Chapecoense") + 1}ª posição')

#exercicio_72()

def maxnum(numero):
    max = numero[0]
    for i, num in enumerate(numero):
        if num >= max:
            max = num
    return max

def minnum(numero):
    min = numero[0]
    for i, num in enumerate(numero):
        if num <= min:
            min = num
    return min

def exericio_73():
    '''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

    from random import randint
    numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
    
    print(numeros)
    print(f'Os valores sorteados foram: ', end='')
    for n in numeros:
        print(f'{n}', end=' ')
    print(f'\nO maior valor é {max(numeros)}')
    print(f'O maior valor é {maxnum(numeros)}')
    print(f'O menor valor é {min(numeros)}')
    print(f'O menor valor é {minnum(numeros)}')

exericio_73()