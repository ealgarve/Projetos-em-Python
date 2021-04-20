linhas = []
matriz = []
linha = 1
coluna = 1
while True:    
    elemento = str(input(f'Entre com o elemento [{linha}, {coluna}] : '))
    coluna += 1
    print(f'Para encerrar a linha {linha}, digite enter!')
    if elemento == "":
        matriz.append(linhas)
        fim = str(input(f'Para encerrar a matriz {linha} x {coluna}, digite "enter" ou "c" para continuar: '))
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

print(f'Linha: {linhas}')
print(f'Matriz: {matriz}')
print(f'Dimenção da Matriz: {len(matriz)} x {len(matriz[0])}')
for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz[0])):
        print(f'a[{linha + 1}, {coluna + 1}] = {matriz[linha][coluna]}')


