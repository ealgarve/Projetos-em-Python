class Complexo:
    def __init__(self, parteReal, parteImaginaria):
        self.r = parteReal
        self.i = parteImaginaria

'''z = Complexo(3.0, -4.5)
print(f'Parte Real = {z.r}\nParte Imaginária = {z.i}')'''

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)
print('-'*5)
for i in 'golf':
    print(len('golf'))

