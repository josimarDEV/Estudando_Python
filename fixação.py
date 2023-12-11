####Python 3 - conceitos e aplicações#### ESTUDAR AQUI
# class Palindromo:
#     def pali(self, palavra):
#         if palavra == palavra[::-1]:
#             print("É um palíndromo!")
#         else:
#             print("Não é palíndromo!")
#
#         return palavra
#
#
# while True:
#     entrada = input("Informe uma palavra que direi se é ou não um palíndromo (ou 'sair' para encerrar): ")
#
#     if entrada.lower() == 'sair':
#         break
#     else:
#         Palindromo().pali(entrada)


# lista = [1, 2, 3, 4]
# lista.append(6)   #adicionar em uma lista
# lista[1] = 7 # trocar um elemento dentro da lista da posição 1 , pelo numero 7
# print(lista)
# cont = 0
# for x in lista:
#     if x == 3:
#         lista.append(9)
#         lista[cont] = 8
#     cont += 1
#
# if 5 in lista:
#     print("Tem")
#     lista.remove(5)
# else:
#     lista.append(5)
# lista.sort()
# print(lista)
# lista.reverse()
# print(lista)

# FIBONACCI SEQUENCE
# a, b = 0, 1
#
# while a < 100:
#     print(a, end=', ')
#     a, b = b, b + a
# print()

# controle de fluxo
# nome = 'JOSIMAR'
# if nome[0] in nome:                # só alguma coisa com o if
#     print("Encontrei a primeira letra!")
#
# for letra in nome:
#     print(letra, end=',')      # alguma coisa com o for
# # Sequencia de Fibonacci
# a, b = 0, 1
# print(a)
# print(b)
# for i in range(10):   # Lógica que pensei utilizando o range para chegar a sequência de Fibonacci
#     c = a + b
#     a = b
#     b = c
#     print(c)

# print(list(range(5, 10)))
# print(list(range(0, 10, 3)))
# print(list(range(-10, -110, -10)))

# # duas formas de chegar ao mesmo raciocinio
# a = ['mary', 'had', 'a', 'little', 'lamb']
# for x, i in enumerate(a):
#     print(x, i)
# for i in range(len(a)):
#     print(i, a[i])

# print(range(10)) # coisa que nã se deve fazer sempre utilizar com construtores

# print(sum(range(4)))

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'iguais', x, '*', n//x)
#             break
#         else:
#             print(n, 'é um número primo')

# Match
# def https_erro(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 101 | 102 | 103:
#             return "Olá mundo"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I`m a teapot"
#         case _:  # caso se nenhum corresponder entra neste caso.
#             return "Something`s wrong with the internet"
#
#
# print(https_erro(101))


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# def teste(point):
#     match point:
#         case Point(x=0, y=0):
#             print("origin")
#         case Point(x=0, y=y):
#             print(f"Y={y}")
#         case Point(x=x, y=0):
#             print(f"X={x}")
#         case Point():
#             print("Somewhere else")
#         case _:
#             print("Not a point")
#
# teste(Point('12', 0))


# from enum import Enum
#
#
# class Color(Enum):
#     RED = 'red'
#     GREEN = 'green'
#     BLUE = 'blue'
#
#
# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
#
# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")
#
# print(color)


# 4.7. Definindo funções
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()
#     return "josimar"
#
#
# fib(2000)
# f = fib
# f(100)
#
# print(fib(200)) # devolve o return


# def fib2(n):
#     resultado = []
#     a, b = 0, 1
#     while a < n:
#         resultado += [a] # mesmo que append
#         a, b = b, a + b
#     return print(resultado)
#
#
# fib2(100)


# Mais sobre funcões
# Argumentos com valor padrão
# def sim_ou_nao(perguntar, vezes=4, lembrete="Por favor Tente Novamente!"):
#     while True:
#         ok = input(perguntar)
#         if ok.lower() in ('sim', 's', 'yes'):
#             return "True"
#         if ok in ('não', 'nao', 'n', 'no'):
#             return False
#         vezes = vezes - 1
#         if vezes < 0:
#             raise ValueError('Resposta do usuário Inválido!')
#         print(lembrete)
#
#
# resultado = sim_ou_nao("Gostaria de Continuar: ")
# print(resultado)

#
# i = 5
#
#
# def f(arg=i):
#     print(arg)
#
#
# i = 6
# f()
# print(i)

# def f(a, l=[]):
#     l.append(a)
#     return l
#
#
# print(f(1))
# print(f(2))
# print(f(3))

# def f(a, L=None):
#     if L is None:   # nao acumula
#         L = []
#     L.append(a)
#     return L
#
# print(f(1))
# print(f(2))
# print(f(3))


# Argumentos nomeados
# def fruta(nome, estado='Maduro', preco=5.99, codigo=2884):
#     print(f"Seu preco = {preco}")
#     print(f"Seu nome = {nome}")
#     print(f"Seu código = {codigo}")
#     print(f"Seu estado = {estado}")
#
# fruta('Maça')
# print()
# fruta(nome='Maça')
# print()
# fruta(nome='Melancia', preco=6.99)
# print()
# fruta(preco=6.99, nome='Melancia')
# print()
# fruta('Anos', 'Meses', 'Dias')
# print()
# fruta("Milhares", estado='Verde')
#


# def args1(*args):
#     for x in args:
#         print(x)
#
#
# args1('cha', 'chave', 'chuvisco')
#

# def kawargs1(**kwargs):
#     for x, y in enumerate(kwargs.items()):
#         print(f"{x} = {y}")
#
#
# kawargs1(fruta='Maça', codigo=2884, valor=5.99)

# a = 6
# b = 7
# faltas = 3
#
# media = (a + b) / 2
# if media >=7 and faltas <=5:
#     print("Aprovado")
# else:
#     print("Reprovado")
# print(media)

# nome = "GUIDO"
# for letra in nome:
#     print(letra)

# def calcular(v1, v2=0):
#     return v1 + v2
#
# print(calcular(4))

# def calcular(*args):
#     r = sum(args)
#     for i in args:
#         r += i
#     return r
#
# print(calcular(1,4,5))


# 4.8.3. Parâmetros especiais
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#     -----------    ----------     ----------
#     |                   |                         |
#     |                Posição ou nome              |
#     |                                             - Somente nome
#     -- Posição somente


# Exemplos de funções
# def standard_arg(nome, codigo):
#     print(nome, codigo)
#
#
# def pos_only_arg(nome, codigo, /):
#     print(nome, codigo)
#
#
# def kwd_only_arg(*, nome, codigo):
#     print(nome, codigo)
#
#
# def combined_example(pos_only, /, standard, *,kwd_only):
#     print(pos_only, standard, kwd_only)
#
#
# standard_arg(codigo=194, nome="Josimar")
# pos_only_arg(194, 'Josimar')
# kwd_only_arg(nome='Josimar', codigo=194)
# combined_example('Josimar', 194, kwd_only='1994')

# def concat(*args, sep="/"):
#     return sep.join(args)
#
# print(concat("josimar", 'gonçalves', 'silva',sep=' '))

# 4.8.5. Desempacotando listas de argumentos
# coisa boba que pensei em fazer
# print("@@ Calculo de matrix 2x2 @@")
# print("Digite sua matrix, começando pela primeira linha, e segue...")
# a = [int(input()), int(input())]
# b = [int(input()), int(input())]
# determinate_a = (a[0] * b[1]) - (a[1] * b[0])
#
# print(determinate_a)

# print(list(range(3, 6)))
# args = [3, 6]
# print(list(range(*args)))

# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")
#
#
# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)

# 4.8.6. Expressões lambda
# def make_incrementor(n):
#     return lambda x: x + n
#
#
# f = make_incrementor(42)
# print(f(5))
# print(f(2))

# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)

# 4.8.7. Strings de documentação
# def my_function():
#     """Do nothing, but document it.
#
#     No, really, it doesn't do anything."""
#     pass
#
#
# print(my_function.__doc__)

# 4.8.8. Anotações de função
# def f(fruta: str, melao: str = 'Melão') -> str:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", fruta, melao)
#     return f'{fruta}' 'E'  f'{melao}'
#
#
# f('Maça')

# Estruturas de dados

# lista = [0, 5, 2, 3, 4]
# a = 6
# lista[len(lista):] = [a]
# print(lista)
# lista.insert(1, 1)
# print(lista)
# lista.remove(0)
# print(lista)
# print(lista.pop(3))
# lista.clear()
# print(lista.index(2))
# print(lista.count(2))
# print(len(lista))
# lista.copy()
# lista.sort()
# print(lista)
# lista.reverse()
# print(lista)
# print(lista)

# j = 2
# a = 3 + 4 * j
# b = 5 + 7 * j
#
# print(f"{a} menor que {b}: ", a < b)

# 5.1.1. Usando listas como pilhas
# pilha = [3, 4, 5]
# pilha.append(6)
# pilha.append(7)
# print(pilha)
# pilha.pop()
# print(pilha)
# pilha.pop(2)
# print(pilha)

# 5.1.2. Usando listas como filas

# from collections import deque
# fila = deque(['Eric', 'John', 'Michael'])
# fila.append('Terry')
# fila.append('Graham')
# print(fila)
# fila.popleft()
# fila.popleft()
# print(fila)

# 5.1.3. Compreensões de lista
# quadradados = []
# for x in range(10):
#     quadradados.append(x**2)
# print(quadradados)
# quadrados = [x**2 for x in range(10)]
# print(quadrados)

# combinacao = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combinacao.append((x,y))
#
# print(combinacao)

# combinacao = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(combinacao)

# lista = [-4, -2, 0, 2, 4]
# lista = [x * 2 for x in lista]
# print(lista)
# lista = [x for x in lista if x >= 0]
# print(lista)
# lista = [x for x in lista if x < 0]
# print(lista)
# lista = [abs(x) for x in lista]
# print(lista)
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# freshfruit = [weapon.strip() for weapon in freshfruit]
# print(freshfruit)
# lista = [(x, x**2) for x in range(6)]
# print(lista)
# vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# vec = [num for elem in vec for num in elem]
# print(vec)

# from math import pi
# lista = [str(round(pi, i)) for i in range(1, 6)]
# print(lista)

# 5.1.4. Compreensões de lista aninhadas
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# matrix = [[row[i] for row in matrix] for i in range(4)]
# print(matrix)
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
#
# print(transposed)

# matrix = list(zip(*matrix))
# print(matrix)

# 5.2. A instrução del
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print(a)
# del a[2:4]
# print(a)
# del a[:]
# print(a)
#

# 5.3. Tuplas e Sequências¶
# a = 1, 2, 3
# print(a)
# tupla = 1, 2, 3
# for x in tupla:
#     for y in range(len(tupla)):
#         a = 'b' + str(y)
#         b = a + '=' + str(x)
#         c = {b}
#         print(c)

# 5.4. Conjuntos
# fruta = {'maça', 'morango', 'mamão', 'mamão', 'laranja', 'morango'}
# print(fruta)
# print('laranja' in fruta)
# print('abacaxi' in fruta)
# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(a - b) # o que tem no a mais não tem no b
# print(a | b) # a união com b
# print(a & b)  # a interseção com b
# print(a ^ b)


# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

# 5.5. Dicionários¶
# telefone = {'jack': 4098, 'sape': 4139}
# telefone['guido'] = 4127
# print(telefone)
# print(telefone['jack'])
# del telefone['sape']
# print(telefone)
# del telefone['irv'] # retorna um erro, pois não existi essa chave
# print(telefone)
# print(list(telefone))
# print(sorted(telefone))
# print('guido' in telefone)
# print('jack' not in telefone)

# print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# dicionario = {x: x**2 for x in (2, 4, 6)}
# print(dicionario)

# print(dict(sape=4139, guido=4127, jack=4098))


# 5.6. Técnicas de iteração¶
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for x, z in knights.items():
#     print(x, z)

# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for x, y in zip(questions, answers):
#     print('What is your {0}?  It is {1}.'.format(x, y))

# for i in reversed(range(1, 10, 2)):
#     print(i)

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for x in sorted(set(basket)):
#     print(x)

# import math
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)


# 5.7. Mais sobre condições¶
# a = 3
# b = 3
# c = 4
# d = a and b or c
# print(d)

# 5.8. Comparando sequências e outros tipos¶
# print(
#     (1, 2, 3) < (1, 2, 4),
#     [1, 2, 3] < [1, 2, 4],
#     'ABC' < 'C' < 'Pascal' < 'Python',
#     (1, 2, 3, 4) < (1, 2, 4),
#     (1, 2) < (1, 2, -1),
#     (1, 2, 3) == (1.0, 2.0, 3.0),
#     (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
# )

# 6. Módulos¶
# import fibo
#
# fibo.fib(1000)
# print(fibo.fib2(100))
# print(fibo.__name__)
# fib = fibo.fib
# fib(500)

# 6.1. Mais sobre módulos¶
# from fibo import fib, fib2
# fib(300)

# from fibo import fib as fibonacci
# fibonacci(500)

# import  fibo, builtins
# a = [1, 2, 3, 4, 5]
# fib = fibo.fib
# print(dir())
# print()
# print(dir(builtins))

# 6.4.1. Importando * de um pacote¶
# 7. Entrada e Saída¶
# year = 2023
# event = 'Natal'
# print(f'O {event} de {year} vai ser muito bom!!!')

# yes_votes = 42_572_654
# novotes = 43_131_495
# percentage = yes_votes / (yes_votes + novotes)
# print("{:-9} YES votes {:2.2%}".format(yes_votes, percentage))

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print(f'{name:8} ==> {phone:8d}')

# bugs = 'roaches'
# count = 13
# area = 'Living room'
# print(f'Debugging {bugs=} {count=} {area=}')

# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')      #rjust justifica a direita
#     # Note use of 'end' on previous line                #ljust() reajusta a esquerda
#     print(repr(x*x*x).rjust(4))

# print('12'.zfill(5))
#
# print('-3.14'.zfill(7))
#
# print('3.14159265359'.zfill(5))

# # 7.2. Leitura e escrita de arquivos¶
# oi = 'Second line of the file'
# ola = " \n"
# caminho_arquivo = r'D:\Áre de Trabalho/exemplo.txt'
# with open(caminho_arquivo, 'r+') as arquivo:
#     arquivo.seek(0,2)
#     # arquivo.write(oi)
#     # arquivo.write(ola)
#     arquivo.seek(0)
#     conteudo = arquivo.read()
#     arquivo.seek(0)
#     for line in arquivo:
#         print(line, end='')
# print(conteudo)
# 7.2.1. Métodos de objetos arquivo¶

# n1 =float(3.5)
# n2 = float(input())
#
# media = (n1 + n2) / 2
#
# if media >= 5:
#     print(f'{media:.2f}Aprovada!!')
# else:
#     print(f'{media:.2f}Reprovada!!')

# nome = 'Lira'
#
#
# if nome in ['João' or 'Paulo' or 'Marcus']:
#     print('Liberado')
#
# else:
#     print('Negado')
