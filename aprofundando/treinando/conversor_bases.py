#  dividendo|divisor
#  _______   --------
#  resto      quociente  
class conversor_base:
    def __init__(self):
        print('Oi, eu sou o construtor.')
        
    def dec_bin(self, decimal):
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
        #print(f'O núnero {decimal} e igual a {binario} em binario.')
        return binario

    def dec_hex(self, num):
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
        #print(f'O núnero {num} e igual a {hexadecimal} em hexadecimal.')
        return hexadecimal

    def bin_dec(self, bina):
        decimal = 0
        binario = reversed(bina)
        for i, e in enumerate(binario):
            decimal = decimal + e * 2**(i)
            #print(f'Elemento[{i}]: {e} * 2^{i}')
        #print(f'O número {bina} é igual a {decimal} em decimal.')
        return decimal

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
        #print(f'O número {hexa} é igual a {decimal} em decimal.')
        return decimal

    def hex_bin(self,hexa):
        x = self.hex_dec(hexa)
        return self.dec_bin(x)
    
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
            
        return hex
        #print(f'Hex fatiado: {hex}')
            

conv = conversor_base()
print(conv.dec_bin(42))
print(conv.dec_hex(42))
print(conv.hex_dec([2, 'A']))
print(conv.hex_bin([2, 'A']))
print(conv.bin_hex([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0]))
print(conv.bin_hex([1, 0, 1, 0, 1, 0]))
print(conv.bin_dec([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0]))