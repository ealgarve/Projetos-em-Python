var = 'Elias'
print(f'Imprimindo uma variável {var}', '\n', 'Imprimindo a mesma variável', var)
print('Elias', 'Machado', 'Algarve', sep='@')
print(r'Imprimindo uma \n variável {var}')
print('Imprimindo uma \n variável {var}')
text = 'Hello World'
print(text[2:5])
print(text[0:1])
print(text[10:11])
print(text.upper())
print(13//4)

lista = ['carro', 'mesa', 'cadeira', 'caneta', 'fita']
c_lista = lista
print('imprimindo listas')
print(f'lista: {lista}')
print(f'c_lista: {c_lista}')
lista[0] = 'bicicleta'
print('imprindo lista apos alterar o primeiro elemento de "lista"')
print(f'lista: {lista}')
print(f'c_lista: {c_lista}')
c_lista = lista.copy()
lista[0] = 'escova'
print('imprindo listas depois de copiar da maneira certa')
print(f'lista: {lista}')
print(f'c_lista: {c_lista}')