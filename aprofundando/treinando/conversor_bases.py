#  dividendo|divisor
#  _______   --------
#  resto      quociente  
class conversor_base:
    def __init__(self):
        print('Oi, eu sou o construtor.')
        while True:
            print('Escolha a sua converção')
            print('[1] Decimal para Binário')
            print('[2] Decimal para Hexadecimal')
            print('[3] Binário para Decimal')
            print('[4] Binário para Hexadecimal')
            print('[5] Hexadecimal para Decimal')
            print('[6] Hexadecimal para Binário')
            print('[S] Sair')
            opcao = str(input('Digite a opção desejada: '))
            if opcao == '1':
                num = int(input('Digite o número a ser convertido: ').upper())
                print(f'O núnero {num} e igual a {self.dec_bin(num)} em binario.')
            elif opcao == '2':
                num = int(input('Digite o número a ser convertido: ').upper())
                print(f'O núnero {num} e igual a {self.dec_hex(num)} em hexadecimal.')
            elif opcao == '3':
                num = int(input('Digite o número a ser convertido: ').upper())
                print(f'O número {num} é igual a {self.bin_dec(num)} em decimal.')
            elif opcao == '4':
                num = int(input('Digite o número a ser convertido: ').upper())
                print(f'O número {num} é igual a {self.bin_hex(num)} em decimal.')
            elif opcao == '5':
                num = str(input('Digite o número a ser convertido: ').upper())
                print(f'O número {num} é igual a {self.hex_dec(num)} em decimal.')
            elif opcao == '6':
                num = str(input('Digite o número a ser convertido: ').upper())
                print(f'O número {num} é igual a {self.hex_bin(num)} em binário.')
            elif opcao in 'sS':
                break
            else:
                print('Opção inexistente. Tente novamente.')
        
    def dec_bin(self, decimal): # [1] decimal para binário
        binario = []
        divisor = 2
        decimal = int(decimal)
        dividendo = decimal
        while True:
            resto = dividendo % divisor
            quociente = dividendo//divisor
            binario.insert(0,resto)
            if quociente == 0:
                break
            dividendo = quociente
        
        return binario

    def dec_hex(self, num): # [2] decimal para hexadecomal
        hexadecimal = []
        divisor = 16
        num = int(num)
        dividendo = num
        while True:
            resto = dividendo % divisor
            quociente = dividendo//divisor
            if 10 <= resto <= 15:
                if resto == 10:
                    resto = 'A'
                elif resto == 11:
                    resto = 'B'
                elif resto == 12:
                    resto = 'C'
                elif resto == 13:
                    resto = 'D'
                elif resto == 14:
                    resto = 'E'
                elif resto == 15:
                    resto = 'F'
                else:
                    resto = 'erro'
            hexadecimal.insert(0,resto)
            if quociente == 0:
                break
            dividendo = quociente
        return hexadecimal

    def bin_dec(self, bina): # [3] binário para decimal
        decimal = 0
        binario = reversed(self.int_bin(bina))
        for i, e in enumerate(binario):
            decimal = decimal + e * 2**(i)
        return decimal

    def hex_dec(self, hexa): # [5] hexadecomal para decomal
        
        decimal = 0
        hexadecimal = reversed(self.str_hex(hexa))
        for i, e in enumerate(hexadecimal):
            if e == 'A':
                e = 10
            elif e == 'B':
                e = 11
            elif e == 'C':
                e = 12
            elif e == 'D':
                e = 13
            elif e == 'E':
                e = 14
            elif e == 'F':
                e = 15
            elif e in '0123456789':
                e = int(e)
            else:
                pass
            decimal = decimal + e * 16**(i)
        return decimal

    def hex_bin(self,hexa): # [6] hexadecimal para binário
        x = self.hex_dec(hexa)
        y = self.dec_bin(x)
        return y
    
    def bin_hex(self, bina): # [4] binário para hexadecimal
        bin = self.int_bin(bina)
        hex = []
        for i in range(len(bin)):
            fatia = bin[-4:]
            while len(fatia) < 4:
                fatia.insert(0, 0)
            if fatia == [0, 0, 0, 0]:
                fatia = 0
            elif fatia == [0, 0, 0, 1]:
                fatia = 1
            elif fatia == [0, 0, 1, 0]:
                fatia = 2
            elif fatia == [0, 0, 1, 1]:
                fatia = 3
            elif fatia == [0, 1, 0, 0]:
                fatia = 4
            elif fatia == [0, 1, 0, 1]:
                fatia = 5
            elif fatia == [0, 1, 1, 0]:
                fatia = 6
            elif fatia == [0, 1, 1, 1]:
                fatia = 7
            elif fatia == [1, 0, 0, 0]:
                fatia = 8
            elif fatia == [1, 0, 0, 1]:
                fatia = 9
            elif fatia == [1, 0, 1, 0]:
                fatia = 'A'
            elif fatia == [1, 0, 1, 1]:
                fatia = 'B'
            elif fatia == [1, 1, 0, 0]:
                fatia = 'C'
            elif fatia == [1, 1, 0, 1]:
                fatia = 'D'
            elif fatia == [1, 1, 1, 0]:
                fatia = 'E'
            elif fatia == [1, 1, 1, 1]:
                fatia = 'F'
            else:
                print('deu erro na conversão 4bits para hexa')
            hex.insert(0, fatia)
            del bin[-4:]
            if bin == []:
                break
            
        return hex
            
    def int_bin(self, inteiro):
        fatiado = []
        lista = list(str(inteiro))
        for i in range(len(lista)):
            fatiado.append(int(lista[i]))
        return fatiado

    def str_hex(self, hex):
        fatiado = []
        lista = list(str(hex))
        for i in range(len(lista)):
            fatiado.append(str(lista[i]))
        return fatiado


#conv = conversor_base()

def agrupa4():
    separado = []
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while len(lista) > 0:
        fatia = lista[-4:]
        while len(fatia) < 4:
            fatia.insert(0, 0)
        separado.insert(0, fatia)
        del lista[-4:]
    print(separado)   
    print(f'Elemento: {separado[3][2]}') 
    #while len(separado) > 0:
    for i, e in enumerate(separado):
        for j, c in enumerate(separado[i]):
            print(f'Elemento {i}, {j} = {c}')
    print(separado)

agrupa4()
