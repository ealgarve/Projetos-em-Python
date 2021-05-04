class minha_classe():
    '''Revisitando classes no Python'''
    def __init__(self, nome, nome_do_meio, sobrenome):
        self.nome = nome
        self.nome_do_meio = nome_do_meio
        self.sobrenome = sobrenome
    num = 1234
    def minha_funcao(self):
        return 'hello world'
    def mostra_construtor(self):
        return f'{self.sobrenome}, {self.nome} {self.nome_do_meio}' 

print(minha_classe.minha_funcao(self='hemm!!'))
x = minha_classe('Elias', 'Machado', 'Algarve')
print(x.__doc__)
print(x.minha_funcao())
print(x.mostra_construtor())
