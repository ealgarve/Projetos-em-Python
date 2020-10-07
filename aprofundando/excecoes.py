def ex_01():
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        except KeyboardInterrupt:
            sair = str(input('Vc usou o teclado para inerromper o programa./nDeseja ralmente sair? [s/n]')).lower().strip()[0]
            if sair == 's':
                break

def ex_02(): # funcionamento do tratamento de exceção entre classes
    class B(Exception):
        pass

    class C(B):
        pass

    class D(C):
        pass

    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")

def ex_03():
    while True:
        try:
            x = int(input('Inteiro entre 5 e 10?'))
            if 5 <= x <= 10:
                print('Vamos seguir em frente...')
            else:
                raise NameError('O número não esta entre 5 e 10.')
                continue
        except ValueError as err:
            print('erro: valor invalido --> ', err)
        except NameError:
            print('O número não esta entre 5 e 10, tente outra vez!')
            # raise # faz sair fora do loop
        else:
            print('...seguindo com o programa.')
            print('fim do programa')
            break

ex_03()

class Error(Exception): # não entendi como funciona
    """Base class for exceptio
    ns in this module."""
    pass

class ErroDeEntrada(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class ErroDeTransicao(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message