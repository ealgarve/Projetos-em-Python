from random import randint

lista = []
for i in range(0, 100):
    lista.append(randint(0, 100))

lista_2 = [87, 89 ,3 ,5 ,2 ,78 ,82]
lista_3 = ['casa', 'carro', 'cachorro', 'mesa', 'cadeira', 'sofa', 'televisão', 'telefone']
'''for i, coisa in enumerate(lista_3):
    if 3 < i < 6:
        print(f'[{i}] --> {coisa}')'''

for i, coisa in enumerate(lista):
    if 82 < i < 92:
        print(f'--> {lista[coisa]}')

#print(lista)
