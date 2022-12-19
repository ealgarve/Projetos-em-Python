from itertools import count
import re
from turtle import pos


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


def exercicio_73():
    times = ('Bahia', 'Brusque', 'Chapecoense', 'CRB', 'Criciúma', 'Cruzeiro', 'CSA', 'Guarani', 'Atlético Mineiro', 'Botafogo', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Santos', 'Inter SM', 'Grêmio', 'Inter', 'Brasil de Pelotas', 'Guarani')
    print(f'Os 5 primeiros times são: {times[:5]}')
    print(f'Os 4 últimos times são: {times[-4:]}')
    print(f'Em ordem alfabetica: {sorted(times)}')
    print(f'Time [{times[times.index("Chapecoense")]}]: {times.index("Chapecoense") + 1}ª posição')

#exercicio_73()

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

def exericicio_74():
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

#exericicio_74()

def exercicio_75():
    '''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
        A) Quantas vezes apareceu o valor 9.
        B) Em que posição foi digitado o primeiro valor 3.
        C) Quais foram os números pares.'''
    
    tnum = (int(input(f'Digite um número: ')), int(input(f'Digite um número: ')), int(input(f'Digite um número: ')), int(input(f'Digite um número: ')))
       

    print(f'Tupla números: {tnum}')

    print(f'O numero 9 apareceu {tnum.count(9)}')
    if 3 in tnum:
        print(f'Em que posição apareeu o numero 3: {tnum.index(3) + 1}')
    else:
        print(f'O núero 3 não esta na tupla.')
    print(f'Os números pares são: ', end='')
    for n in tnum:
        if n % 2 == 0:
            print(n, end=' ')

#exercicio_75()

listagem = ('Lápis', 3.25, 'Caderno', 14.5, 'Caneta', 4, 'Mochila', 125.9)
print(40*'-')
print(f'{"LISTA DE COMPRAS":^40}')
print(40*'-')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(listagem[pos])