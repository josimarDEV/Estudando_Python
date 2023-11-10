# class Cachorro:   #__init__ metodo construtor
#     def __int__(self, nome, cor, acordado=True):
#         self.nome = nome
#         self.cor = cor
#         self.acordado = acordado
#
#
# #__del__ metodo destrutor
#
# class Cachorro:   #__init__ metodo construtor
#     def __del__(self):
#         print("Destruindo a instância")
#
# c = Cachorro()
# del c

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e Preto", False)
    print(c.nome)


c = Cachorro("Chappie", "Amarelo")
c.falar()
criar_cachorro()
