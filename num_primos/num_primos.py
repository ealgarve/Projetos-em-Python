'''Exercício Python 52: Faça um programa que
leia um número inteiro e diga se ele é ou não um número primo.
Conceito:
Um número é classificado como primo se ele é maior do que um e é
divisível apenas por um e por ele mesmo. Apenas números naturais
são classificados como primos.
'''
primos = []
div = 0
primos_de_verdade = []
for n in range(1, 100):
    for p in range(1, 100):
        if n % p == 0:
            div += 1
    if div == 2:
        primos.append(n)
    div = 0            
 
print('='*30, end='=>>>')        
print(f'\nlista de {len(primos)} primos: {primos}')
print('='*30, end='=>>>') 