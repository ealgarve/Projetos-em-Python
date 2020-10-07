'''Exercícios de Classes do site:
https://wiki.python.org.br/ExerciciosClasses
==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==
1 - Classe Bola: Crie uma classe que modele uma bola:
    a - Atributos: Cor, circunferência, material
    b - Métodos: trocaCor e mostraCor'''
import os
class Bola:
    cor = ''
    circunferencia = 0
    material = ''
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self):
        os.system('cls')
        print('### Alterar a cor da Bola ###')
        self.cor = str(input('Digite uma nova cor para a bola: '))
        print('Informações inseridas com sucesso.')
        os.system('pause')
    
    def info(self): # mostraCor() --> mostra a cor da Bola e tudo mais
        os.system('cls')
        print('### Informações sobre a Bola ###')
        print(f'--> Cor da Bola......: {self.cor}')
        print(f'--> Circunferência...: {self.circunferencia}')
        print(f'--> Material.........: {self.material}')
        os.system('pause')

    def menu(self):
        os.system('cls') or None
        print('### Menu da Bola ###')
        print('1 - Entrar com as caracteristicas da Bola.')
        print('2 - Informações da Bola')
        print('3 - Trocar a cor da Bola')
        print('4 - Sair')
        opc = input('Digite uma opção: ')
        return opc

hora = Bola('brurro quando chove', 123, 'panela')
ret = hora.menu()
while True:
    if ret == '1':
        os.system('cls')
        print('### Caracteristicas da Bola ###')
        cor = str(input('Qual a cor da Bola? '))
        circunferencia = float(input('Qual a circunferência da Bola? '))
        material = str(input('Qual é o material da Bola? '))
        hora = Bola(cor, circunferencia, material)
        print('Informações inseridas com sucesso.')
        os.system('pause')
    elif ret == '2':
        hora.info()
    elif ret == '3':
        hora.trocaCor()
    elif ret == '4':
        break
    else:
        print('Opção inexistente.')
        os.system('pause')
    ret = hora.menu()

os.system('cls') or None
print('programa finalizado')