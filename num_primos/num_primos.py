'''Exercício Python 52: Faça um programa que
leia um número inteiro e diga se ele é ou não um número primo.
'''
print('Lista de números primos:')
lista_primo = [1, 2, 3]
proximo = 1
while len(lista_primo) <= 19: # cria lista de 20 numeros 
    lista_primo.append(lista_primo[len(lista_primo) - 1] + proximo) # adiciona o proximo número na lista
    print('lista de primos: {}' .format(lista_primo))
    print('último termo adicionado é {}' .format(lista_primo[len(lista_primo) - 1]))
    conta = 0
    for i in range(lista_primo[len(lista_primo) - 2], lista_primo[0], -1): # testa o novo número
        if lista_primo[len(lista_primo) - 1] % lista_primo[i]  == 0: # (termo adicionado)/(demais termo)= resto 0
            conta += 1 # conta quantas divisões = 0
    if conta <= 1: # se o numero novo tem só um divisor, ele é primo e fica na lista
        print('o número {} é primo' .format(i))
        proximo += 1  # para incrementar o próximo número
    else:
        print('o número {} não é primo' .format(i))
        lista_primo.remove(lista_primo[len(lista_primo) - 1]) # se o novo número não é primo, ele cai fora
        proximo += 1
    pass
    
print(f'lista de primos: {lista_primo}')
