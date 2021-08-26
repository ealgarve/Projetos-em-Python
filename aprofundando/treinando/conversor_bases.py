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
        print(f'O núnero {decimal} e igual a {binario} em binario.')

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
        print(f'O núnero {num} e igual a {hexadecimal} em hexadecimal.')

    def bin_dec(self, bina):
        decimal = 0
        binario = reversed(bina)
        for i, e in enumerate(binario):
            decimal = decimal + e * 2**(i)
            #print(f'Elemento[{i}]: {e} * 2^{i}')
        print(f'O número {bina} é igual a {decimal} em decimal.')

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

conv = conversor_base()
conv.dec_bin(42)
conv.dec_hex(42)
conv.bin_dec([1, 0, 1, 0, 1, 0])
conv.hex_dec([2, 'A'])