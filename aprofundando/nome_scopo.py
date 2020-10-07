def escopo_principal():
    '''Nome e scopo?
    '''
    def escopo():
        global nome
        nome = 'Elias'
    
    nome = 'Pedro'
    escopo()
    print(f'O nome é {nome}')

nome = 'Pati'
escopo_principal()
print(escopo_principal.__doc__)
