# Dicas de: https://towardsdatascience.com/three-concepts-to-become-a-better-python-programmer-b5808b7abedc

# 1 - Unpacking Operators (* and **)
def desempacotar(): 
    num_list = [1, 2, 3, 4, 5]
    num_list2 = [6, 7, 8, 9]
    nova_list = [*num_list, *num_list2]
    def num_sum(n1 = 0, n2 = 0, n3 = 0, n4 = 0, n5 = 0):
        return n1 + n2 + n3 + n4 + n5

    print(f'Lista de numeros:\n{num_list}')
    print('lista de numeros desempacotados:')
    print(*num_list)
    print(f'lista de numeros desempacotados e somados:\n{num_sum(*num_list)}')
    print(f'mesclando duas listas: {nova_list}')
    print('-='*10)
    first, *middle, last = 'Algarve'
    print(f'Primeira letra: {first}\n', 'Miolo: ', *middle  , f'\nÚltima letra: {last}')


#desempacotar()

def desemp_dic():
    dicionario = {'nome' : 'Elias', 'idade' : 48, 'sexo' : 'M'}
    print(f'desempacotando um dicionário:\n{dicionario}')
    print(*dicionario)
    print(dicionario['nome'])

# desemp_dic()

# 2 - args and kwargs

def pack():
    *names, = 'pedra', 'papel', 'tesoura'
    print(names)

#pack()

def name_tuple(*argumentos):
    return argumentos

#ve_tupla = name_tuple('pedra', 'papel', 'tesoura', 'lagarto', 'spock')
#print(ve_tupla)

def name_dic(**kwargumentos):
    return kwargumentos

#ve_dic = name_dic(nome = 'Elias', sobrenome = 'Machado', sobresobrenome = 'Algarve')
#for i, n in enumerate(ve_dic):
#    print(i, *ve_dic[n], ve_dic[n])

#3. Iteration, Iterables and Iterators
def eh_iter():
    num_list = [1, 2, 3, 4, 5]
    print(dir(num_list)) # retorna os atributos validos do argumento

eh_iter()