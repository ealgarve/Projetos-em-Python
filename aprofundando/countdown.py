import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hour, mins = divmod(mins, 60)
        timer = f'{hour:0>2d}:{mins:0>2d}:{secs:0>2d}'
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
            
    if t == 0:
        print(f'00:00:00')
    else:
        print(f'{hour:0>2d}:{mins:0>2d}:{secs:0>2d}')
    print('Fim do Tempo')

def countup(t):
    counter = 0
    while counter < t:
        mins, secs = divmod(counter, 60)
        hour, mins = divmod(mins, 60)
        timer = f'{hour:0>2d}:{mins:0>2d}:{secs:0>2d}'
        print(timer, end="\r")
        time.sleep(1)
        counter += 1
            
    if t == 0:
        print(f'00:00:00')
    else:
        print(f'{hour:0>2d}:{mins:0>2d}:{secs:0>2d}')
    print('Fim do Tempo')

t = input('Entre com o tempo em segundos: ')

countdown(int(t))
countup(int(t))