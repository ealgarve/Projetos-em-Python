class opera_matriz:
    def __init__(self):
        linhas = []
        self.matriz = []
        linha = 1
        coluna = 1
        while True:    
            elemento = str(input(f'Entre com o elemento [{linha}, {coluna}] : '))
            coluna += 1
            print(f'Para encerrar a linha {linha}, digite enter!')
            if elemento == "":
                self.matriz.append(linhas)
                fim = str(input(f'Para encerrar a matriz {linha} x {len(self.matriz[0])}, digite "enter" ou "c" para continuar: '))
                if fim == 'c':
                    linha += 1
                    linhas = []
                    coluna = 1
                    continue
                else:
                    break
            else:
                linhas.append(float(elemento))
                continue

    def mostra_matriz(self):
        #print(f'Mostra matriz: {self.matriz}')
        print(f'Dimenção da Matriz: {len(self.matriz)} x {len(self.matriz[0])}')
        for linha in range(0, len(self.matriz)):
            for coluna in range(0, len(self.matriz[0])):
                print(f'a[{linha + 1}, {coluna + 1}] = {self.matriz[linha][coluna]}')

    def retorna_matriz(self):
        return self.matriz

    def soma_matriz(self, B_matriz):
        soma = self.matriz[0][0] + B_matriz[0][0]
        print(f'Em construção, mas o primeiro termo da soma é {soma}')
        #return matriz_soma

print('Entre com os elementos da Matriz A:\n')
matriz_A = opera_matriz()
print('\nEntre com os elementos da Matriz B:\n')
matriz_B = opera_matriz()
print('\nAqui esta a Matriz A\n')
matriz_A.mostra_matriz()
print('\nAqui esta a Matriz B\n')
matriz_B.mostra_matriz()
print('\nAqui esta a soma do elemento A11:\n')
matriz_A.soma_matriz(matriz_B.retorna_matriz())