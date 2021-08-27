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
                num = int(input('Digite o número a ser convertido:'))
                self.dec_bin(num)
            elif opcao == '2':
                num = int(input('Digite o número a ser convertido:'))
                self.dec_hex(num)
            elif opcao == '3':
                num = int(input('Digite o número a ser convertido:'))
                self.bin_dec(num)
            elif opcao == '4':
                num = int(input('Digite o número a ser convertido:'))
                self.bin_hex(num)
            elif opcao == '5':
                num = int(input('Digite o número a ser convertido:'))
                self.hex_dec(num)
            elif opcao == '6':
                num = int(input('Digite o número a ser convertido:'))
                self.hex_bin(num)
            elif opcao in 'sS':
                break
            else:
                print('Opção inexistente. Tente novamente.')
        
    def dec_bin(self, decimal): # entra decimal e sai binário
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
            # print(f'Dividendo: {dividendo}, divisor: {divisor}, quociente: {quociente} e resto: {resto}')
            dividendo = quociente
        print(f'O núnero {decimal} e igual a {binario} em binario.')
        # return binario

    def dec_hex(self, num): # entra decimal e sai hexadecimal
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
            # print(f'Dividendo: {dividendo}, divisor: {divisor}, quociente: {quociente} e resto: {resto}')
            dividendo = quociente
        print(f'O núnero {num} e igual a {hexadecimal} em hexadecimal.')
        #return hexadecimal

    def bin_dec(self, bina): # tem que ajeitar para receber e processar o binário
        decimal = 0
        binario = reversed(bina)
        for i, e in enumerate(binario):
            decimal = decimal + e * 2**(i)
            #print(f'Elemento[{i}]: {e} * 2^{i}')
        print(f'O número {bina} é igual a {decimal} em decimal.')
        #return decimal

    def hex_dec(self, hexa):
        decimal = 0
        hexadecimal = reversed(hexa)
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
            else:
                pass
            decimal = decimal + e * 16**(i)
            #print(f'Elemento[{i}]: {e} * 2^{i}')
        print(f'O número {hexa} é igual a {decimal} em decimal.')
        #return decimal

    def hex_bin(self,hexa):
        x = self.hex_dec(hexa)
        self.dec_bin(x)
        #return self.dec_bin(x)
    
    def bin_hex(self, bin):
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
            
        #return hex
        print(f'O número {bin} é igual a {hex} em decimal.')
            

conv = conversor_base()
'''print(conv.dec_bin(42))
print(conv.dec_hex(42))
print(conv.hex_dec([2, 'A']))
print(conv.hex_bin([2, 'A']))
print(conv.bin_hex([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0]))
print(conv.bin_hex([1, 0, 1, 0, 1, 0]))
print(conv.bin_dec([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0]))'''