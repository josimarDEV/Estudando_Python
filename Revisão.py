# print("hello world")  ctrl + / coloca comentario em todo o codigo celecionado
import datetime

# x = 10
# nome = 'aluno'
# nota = 8.75
# fez_inscricao = True
#
# print(x,
#       nome,
#       nota,
#       fez_inscricao)
#
# #podemos imprimir seu tipo usando a função type()
# print(f"\n{type(x),x}\n"
#       f"{type(nome),nome}\n"
#       f"{type(nota),nota}\n"
#       f"{type(fez_inscricao),fez_inscricao}")


# nome = input(str('Digite seu nome:'))
# print(f"Seja Bem Vindo!{nome}")


# operaçoes matematicas
# x+y = soma de x + y
# x-y = diferença de x e y
# x*y = produto de x e y
# x/y = quociente de x e y
# x//y = parte inteira do quociente de x e y
# x%y = resto de x/y
# abs(x) = valor absoluto de x
# pow(x,y) = x elevado a y
# x**y = x elevado a y
# ordem da resoluçao de um operação
# 1. Primeiro resolvem-se os parênteses, do mais interno para o mais externo.
# 2. Exponenciação.
# 3. Multiplicação e divisão.
# 4. Soma e subtração

# # Qual o resultado armazendo na variável operacao_1: 25 ou 17?
# operacao_1 = 2 + 3 * 5
#
# # Qual o resultado armazendo na variável operacao_2: 25 ou 17?
# operacao_2 = (2 + 3) * 5
#
# # Qual o resultado armazendo na variável operacao_3: 4 ou 1?
# operacao_3 = 4 / 2 ** 2
#
# # Qual o resultado armazendo na variável operacao_4: 4 ou 5?
# operacao_4 = 13 % 3 + 4
#
# print(operacao_1)
# print(operacao_2)
# print(operacao_3)
# print(operacao_4)

# a = 2
# b = 0.5
# c = 1
# x = input("Digite o valor de x: ")
# x = float(x)
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(x))
#
# y = a * x ** 2 + b * x + c
# print(f"O resultado de y para x = {x} é {y}.")

# Exercicio
# codigo = int(input("Digite o código da peça: "))
# valor_peca = float(input("Digite o valor da peça: "))
# qtde_peca = int(input("Digite a quantidade de peça: "))
#
# valor_total_peca = qtde_peca * valor_peca
#
# print(f"O valor total deu:{valor_total_peca}")


# #Desafio de código
# janeiro = 200
# fevereiro = 400
# marco = 600
# abril = 800
# maio = 1000
# junho = 1200
#
# c = 200 #constante
#
# mes = int(input("""
# Digite o Mês desejado para saber
# a quantidade de peças a
# ser produzidas: """))
#
# relacao = c * mes
# print(f"A quantidade de peças para o mês {mes} será {relacao}")


# Estruturas Lógicas, condicionais e de repetições em python
# operações
# a < b O valor de a é menor que b?
# a <= b O valor de a é menor OU igual que b?
# a > b O valor de a é maior que b?
# a >= b O valor de a é maior OU igual que b?
# a == b O valor de a é igual ao de b?
# a != b O valor de a é diferente do valor de b?
# a is b O valor de a é idêntico ao valor de b?
# a is not b O valor de a não é idêntico ao valor de b?

# from datetime import date   (teste)
#
# ano_nascimento = date(1988, 3, 27)
# ano_atual = date.today()
#
# print(ano_atual)
# idade = ano_atual.year - ano_nascimento.year - ((ano_atual.month, ano_atual.day) < (ano_nascimento.month, ano_nascimento.day))
# print(idade)

# #estrutura condicionais   IF, ELIF, ELSE
# a = 5         #exemplo seimples
# b = 10
#
# if a < b:
#     print("a é menor que b")
#     r = a + b
#     print(r)

# #exemplo composto
# a = 10
# b = 5
#
# if a < b:
#     print("a é menor que b")
#     r = a + b
#     print(r)
# else:
#     print("a é maior que b")
#     r = a -b
#     print(r)

# #condicional encadeada
# codigo_compra = 5111
#
# if  codigo_compra == 5222:
#     print("Comnpra à vista.")
# elif codigo_compra ==5333:
#     print("Compra à prazo no boleto.")
# elif codigo_compra == 5444:
#     print("Compra à prazo no cartão")
# else:
#     print("Código não cadastrado.")


# Estruturas Lógicas: AND, OR, NOT
# Além dos operadores relacionais, podemos usar os operadores booleanos para
# construir estruturas de decisões mais complexas.
# Operador booleano and: Esse operador faz a operação lógica E, ou seja, dada a
# expressão (a and b), o resultado será True, somente quando os dois argumentos
# forem verdadeiros.
# Operador booleano or: Esse operador faz a operação lógica OU, ou seja, dada a
# expressão (a or b), o resultado será True, quando pelo menos um dos argumentos
# for verdadeiro.
# Operador booleano not: Esse operador faz a operação lógica NOT, ou seja, dada a
# expressão (not a), ele irá inverter o valor do argumento. Portanto, se o argumento
# for verdadeiro, a operação o transformará em falso e vice-versa.


# #exemplo
# qtde_faltas = int(input("Digite a quantidade de faltas: "))
# media_final = float(input("Digite a média final: "))
#
# if qtde_faltas <= 5 and media_final >= 7:
#     print("Aluno Aprovado!")
# else:
#     print("Aluno Reprovado!")

# Obs: not tem uma prioridade mais baixa que os operadores relacionais.
# Portanto, not a == b é interpretado como: not (a == b) e a == not b gera um erro
# de sintaxe.
# Obs2: Assim como as operações matemáticas possuem ordem de precedência,
# as operações booleanas também têm. Essa prioridade obedece à seguinte
# ordem: not primeiro, and em seguida e or por último (BANIN, 2018).

# #exemplo
# a = 15
# b = 9
# c = 9
#
# print(b == c or a < b and a < c)
# print((b == c or a < b) and a < c)


# #Estrutura de repetição: WHILE, FOR
# x = 1
# while x <= 3:
#     print(x)
#     x = x + 1

# numero = 1
# while numero != 0:
#     numero = int(input("Digite um número: "))
#     if numero % 2 == 0:
#         print("Número par!")
#     else:
#         print("Número Impar!")

# #FOR exemplo
# nome = 'GUIDO'
# for c in nome:
#     print(c)

# nome = 'GUIDO'
# for i, c in enumerate(nome):
#     print(f'Posicão = {i}, valor = {c}')


# #controle de repetição com RANGE, BREAK, CONTINUE
# for x in range(5,10,2): #primeiro argumeto(5): do começo 2 argumeto(10), até 3 argumento(2) de 2 em 2
#     print(x)

# exemplo BREAK
# disciplina = "Linguagem de programação"
# for c in disciplina:
#     if c == 'a': # si achar a palavra a ele para
#         break
#     else:
#         print(c)

# #exemplo CONTINUE
# disciplina = "Linguagem de programação"
# for c in  disciplina:
#     if c == 'a':
#         continue
#     else:
#         print(c)
# No exemplo com uso do continue, perceba que foram impressas todas as letras,
# exceto as vogais "a", pois toda vez que elas eram encontradas, o continue determina
# que se pule, mas que a repetição prossiga para o próximo valor. Utilize o emulador
# para executar os códigos e crie novas combinações para explorar.


# #Desafio
# texto = """
# A inserção de comentários no código do programa é uma prática normal.
# Em função disso, toda linguagem de programação tem alguma maneira de permitir que
# comentários sejam inseridos nos programas.
# O objetivo é adicionar descrições em partes do código, seja para documentá-lo ou
# para adicionar uma descrição do algoritmo implementado (BANIN, p. 45, 2018)."
# """
#
# for i, c in enumerate(texto):
#     if c == "a" or c == 'e':
#         print(f"Vogal '{c}' encontrada, na posição {i}")

# texto = """
# A inserção de comentários no código do programa é uma prática normal.
# Em função disso, toda linguagem de programação tem alguma maneira de permitir que
# comentários sejam inseridos nos programas.
# O objetivo é adicionar descrições em partes do código, seja para documentá-lo ou
# para adicionar uma descrição do algoritmo implementado (BANIN, p. 45, 2018)."
# """
#
# vogais = 'aeiou'
# contagem = 0
# for letras in texto:
#     if letras in vogais:
#         contagem += 1
# print(f"Encontrei {contagem} vogais.")


# #Desafio IMPOSTO DE RENDA 2023
# salario = float(input("Digite seu salário: "))
#
# # i1 = 158.40
# # i2 = 370.40
# # i3 = 651.73
# # i4 = 884.96
# imposto = [158.40, 370.40, 651.73, 884.96]
# i1, i2, i3, i4 = imposto
#
# if salario <= 2112.00:
#     print("Insento de Imposto!")
# elif 2112.01 <= salario <= 2826.65:
#     print(f"Será deduzido {i1} do seu salário.")
#     print(f"Seu novo salário será de {salario - i1}")
# elif 2826.66 <= salario <= 3751.05:
#     print(f"Será deduzido {i2} do seu salário.")
#     print(f"Seu novo salário será de {salario - i2}")
# elif 3751.06 <= salario <= 4664.68:
#     print(f"Será deduzido {i3} do seu salário.")
#     print(f"Seu novo salário será de {salario - i3}")
# elif salario >= 4664.68:
#     print(f"Será deduzido {i4} do seu salário.")
#     print(f"Seu novo salário será de {salario - i4}")


# Funçoes em Python
# BUILT-IN             70 funções built in que o python possui
# abs() delattr() hash() memoryview() set()
# all() dict() help() min() setattr()
# any() dir() hex() next() slice()
# ascii() divmod() id() object() sorted()
# bin() enumerate()input() oct() staticmethod()
# bool() eval() int() open() str()
# breakpoint() exec() isinstance() ord() sum()
# bytearray() filter() issubclass()pow() super()
# bytes() float() iter() print() tuple()
# callable() format() len() property() type()
# chr() frozenset() list() range() vars()
# classmethod()getattr() locals() repr() zip()
# compile() globals() map() reversed() __import__()
# complex() hasattr() max() round()
#
# print(), para imprimir um valor na tela.
# enumerate(), para retornar a posição de um valor em uma sequência.
# input(), para capturar um valor digitado no teclado.
# int() e float(), para converter um valor no tipo inteiro ou float.
# range(), para criar uma sequência numérica.
# type(), para saber qual o tipo de um objeto (variável).

# #exemplo de uma função
#
# a = 2
# b = 1
#
# equacao = input("Digite a fórmula da equação linear (a * x + b): ")
# print(f"\nA entrada do usuário {equacao} é do tipo {type(equacao)}")
#
# for x in range(5):
#     y = eval(equacao)
#     print(f"\nResultado da equação para x = {x} é {y}")

# Funçoes definidas pelo usuário
# como criar
# def nome_funcao():
#  # bloco de comandos

# # vamos criar uma função
# def imprimir_mensagem(disciplina, curso):
#     print(f"Minha primeira função em python desenvolvida na disciplina: {disciplina}, do curso: {curso}.")
#
#
# resultado = imprimir_mensagem("Python", "ADS")
# imprimir_mensagem("Python", "ADS")
# print(resultado)

# #agora podemos atribuir um funçao como variavel
# def imprimir_mensagem(disciplina, curso):
#     return f"Minha primeira função em python desenvolvida na disciplina: {disciplina}, do curso: {curso}."
#
#
# mensagem = imprimir_mensagem("Python", "ADS")
# print(mensagem)

# #Exemplo converter mes para extenso
# def converter_mes_para_extenso(data):
#     # Lista de nomes dos meses em português
#     mes = '''janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'''.split()
#
#     # Divide a data em dia (d), mês (m) e ano (a) usando "/" como separador
#     d, m, a = data.split('/')
#
#     # Obtém o nome do mês em português com base no valor do mês (subtraindo 1 para o índice correto)
#     mes_extenso = mes[int(m) - 1]
#
#     # Retorna a data formatada como "dia de mês de ano" em português
#     return f'{d} de {mes_extenso} de {a}'
#
#
# # Solicita a entrada do usuário para o dia, mês e ano
# dia = int(input("Dia: "))
# mes = int(input("Mês: "))
# ano = int(input("Ano: "))
#
# # Chama a função e imprime a data no formato desejado
# print(converter_mes_para_extenso(f'{dia}/{mes}/{ano}'))


# FUNÇÕES COM PARÂMETROS DEFINIDOS E INDEFINIDOS
# Sobre os argumentos que uma função pode receber, para nosso estudo, vamos
# classificar em seis grupos:
# 1. Parâmetro posicional, obrigatório, sem valor default (padrão).
# 2. Parâmetro posicional, obrigatório, com valor default (padrão).
# 3. Parâmetro nominal, obrigatório, sem valor default (padrão).
# 4. Parâmetro nominal, obrigatório, com valor default (padrão).
# 5. Parâmetro posicional e não obrigatório (args).
# 6. Parâmetro nominal e não obrigatório (kwargs)

# # parametro 1
# def somar(a, b):
#     return a + b
#
#
# #r = somar(2)#si colocar um unico argumento dara erro, pois a função somar esta com 2 parametros
# r = somar(2, 3)
# print(r)

# #parametro 2
# def calcular_desconto(valor, desconto=0):## O parâmetro desconto possui zero valor default
#     valor_com_desconto = valor - (valor * desconto)
#     return valor_com_desconto
#
#
# valor1 = calcular_desconto(100) # Não aplica nenhum desconto
# valor2 = calcular_desconto(100, 0.25) # Aplica desconto de 25%
#
# print(f"\nPrimeiro valor a ser pago = {valor1}")
# print(f"\nSegundo valor a ser pago = {valor2}")

# #pode haver erro de logica
# def cadastrar_pessoa(nome, idade, cidade):
#     print("\nDados a serem cadastrados:")
#     print(f"Nome: {nome}")
#     print(f"Idade: {idade}")
#     print(f"Cidade: {cidade}")
#
#
# cadastrar_pessoa("João", 23, "São Paulo")
# cadastrar_pessoa(cidade="São Paulo",nome= "João",idade= 23)
# Com o exemplo da função "cadastrar_pessoa", fica claro como a posição dos
# argumentos, na hora de chamar a função, deve ser conhecida e respeitada, pois a
# passagem dos valores na posição incorreta pode acarretar erros lógicos.

#
# #parametro 3
# def converter_maiuscula(texto,flag_maiuscula):
#     if flag_maiuscula:
#         return texto.upper()
#     else:
#         return texto.lower()
#
#
# texto = converter_maiuscula(flag_maiuscula=True, texto="João") ## Passagem nominal de parâmetros
#
# print(texto)


# #parametro 4
# def converter_misnuscula(texto, flag_minuscula=True):
#     if flag_minuscula:
#         return texto.lower()
#     else:
#         return texto.upper()
#
#
# texto1 = converter_misnuscula(flag_minuscula=True, texto="LINGUAGEM de Programação")
# texto2 = converter_misnuscula(texto="LINGUAGEM DE PROGRAMAÇÃO")
#
# print(f"\nTexto 1 = {texto1}")
# print(f"\nTexto 2 = {texto2}")


# #parametro 5
# def imprimir_parametros(*args):
#     qtde_parametros = len(args)
#     print(f"Quantidade de parâmetros = {qtde_parametros}")
#
#     for i, valor in enumerate(args):
#         print(f"Posição = {i}, valor = {valor}")
#         #print(type(valor))
#
#
# print("\nChamada 1")
# imprimir_parametros("São Paulo", 10, 23.78, "João")
#
# print("\nChamada 2")
# imprimir_parametros(10, "São Paulo")


# # parametro 6
# def imprimir_parametros(**kwargs):
#     print(f"Tipo de objeto recebido = {type(kwargs)}\n")
#     qtde_parametros = len(kwargs)
#     print(f"Quantidade de parâmetros = {qtde_parametros}")
#
#     for chave, valor in kwargs.items():
#         print(f"variável = {chave}, valor = {valor}")
#
#
# print("\nChamada 1")
# imprimir_parametros(cidade="São Paulo", idade=33, nome="JOÃO")
#
# print("\nChamada 2")
# imprimir_parametros(desconto=10, valor=100)


# #FUNÇÕES ANÔNIMAS EM PYTHON
# z = (lambda x: x + 1) (x = 3)
# print(z)
#
# z = (lambda x, y: x + y) (x=3, y=2)
#
# print(z)

# somar = lambda x,y: x + y
# print(somar(x=5,y=3))

# # Desafio
# def valor_total_produto():
#     valor_do_produto = float(input("Digite o valor do produto: "))
#     qtde_produto = int(input("Digite a quantidade de produto: "))
#     return valor_do_produto * qtde_produto
#
#
# def tipo_do_dinheiro():
#
#     print('Qual será a moeda utilizada!')
#     print("1=Real"
#           "2=Dollar"
#           "3=Euro")
#     tipo = int(input("Digite a opção: "))
#
#     real = 1
#     dollar = 5.00
#     euro = 5.70
#
#     if tipo == 2:
#         real = dollar
#     elif tipo == 3:
#         real = euro
#
#     return real
#
#
# print("Vamos realizar sua compra.")
# total_produto = valor_total_produto()
# print(f"O total do produto é: R${total_produto:.2f}")
#
# taxa_cambio = tipo_do_dinheiro()
# total_em_real = total_produto * taxa_cambio
#
# print(f"O total em Real é: R${total_em_real:.2f}")


# resolução
# def calcular_valor(valor_prod, qtde, moeda="real", desconto=None, acrescimo=None):
#     v_bruto = valor_prod * qtde
#
#     if desconto:
#         v_liquido = v_bruto - (v_bruto * (desconto / 100))
#     elif acrescimo:
#         v_liquido = v_bruto + (v_bruto * (acrescimo / 100))
#     else:
#         v_liquido = v_bruto
#
#     if moeda == 'real':
#         return v_liquido
#     elif moeda == 'dolar':
#         return v_liquido * 5
#     elif moeda == 'euro':
#         return v_liquido * 5.7
#     else:
#         print("Moeda não cadastrada!")
#         return 0
#
#
# valor = float(input("Digite o valor: "))
# qtde = int(input("Digite a quantidade: "))
# valor_a_pagar = calcular_valor(valor_prod=valor, qtde=qtde, desconto=5)
# print(f"O valor final da conta é {valor_a_pagar}")


# #outra resolução utilizando kwargs
# def calcular_valor(valor_prod, qtde, moeda="real",
#                    **kwargs):
#     v_bruto = valor_prod * qtde
#
#     if 'desconto' in kwargs:
#         desconto = kwargs['desconto']
#         v_liquido = v_bruto - (v_bruto * (desconto / 100))
#     elif 'acrescimo' in kwargs:
#         acrescimo = kwargs['acrescimo']
#         v_liquido = v_bruto + (v_bruto * (acrescimo / 100))
#     else:
#         v_liquido = v_bruto
#
#     if moeda == 'real':
#         return v_liquido
#     elif moeda == 'dolar':
#         return v_liquido * 5
#     elif moeda == 'euro':
#         return v_liquido * 5.7
#     else:
#         print("Moeda não cadastrada!")
#     return 0
#
#
# valor_a_pagar = calcular_valor(valor_prod=32, qtde=5, desconto=5)
# print(f"O valor final da conta é {valor_a_pagar}")


# ESTRUTURAS DE DADOS EM PYTHON
# vamos dividir as estruturas de dados em objetos do
# tipo sequência, do tipo set, do tipo mapping e do tipo array NumPy. Cada grupo
# pode possuir mais de um objeto. Vamos estudar esses objetos na seguinte ordem:
# 1. Objetos do tipo sequência: texto, listas e tuplas.
# 2. Objetos do tipo set (conjunto).
# 3. Objetos do tipo mapping (dicionário).
# 4. Objetos do tipo array NumPy.

# OBJETOS DO TIPO SEQUÊNCIA
# operaçoes que podem realizar
# Operação Resultado Observação
# x in s True caso um item de s seja
# igual a x, senão False
# True caso um item de s seja igual a
# x, senão False
# s + t Concatenação de s e t Concatena (junta) duas sequências
# n * s Adiciona s a si mesmo n vezes Multiplica a sequência n vezes
# s[i] Acessa o valor guardado na
# posição i da sequência
# O primeiro valor ocupa a posição 0
# s[i:j] Acessa os valores da posição i
# até j
# O valor j não está incluído
# s[i:j:k] Acessa os valores da posição i
# até j, com passo k
# O valor j não está incluído
# len(s) Comprimento de s Função built-in usada para saber o
# tamanho da sequência
# min(s) Menor valor de s Função built-in usada para saber o
# menor valor da sequência
# max(s) Maior valor de s Função built-in usada para saber o
# maior valor da sequência
# s.count(x) Número total de ocorrência de
# x em s
# Conta quantas vezes x foi
# encontrado na sequência

# texto = "Aprendendo python na disciplina de linguagem de programação."
#
# print(f"Tamanho do texto = {len(texto)}")
# print(f"python in texto = {'python' in texto}")
# print(f"Quantidade de y no texto = {texto.count('y')}")
# print(f"As 5 primeiras letras são = {texto[0:5]}")

# texto = "Aprendendo Python na disciplina de linguagem de programação."
#
# print(texto.lower())
# print(texto.replace('i', 'xx'))
# print(texto.upper())

# texto = "Aprendendo Python na disciplina de linguagem de programação."
# print(f"texto = {texto}")
# print(f"Tamanho do texto = {len(texto)}\n")
#
# palavras = texto.split()
# print(f"palavras = {palavras}")
# print(f"Tamanho de palavras = {len(palavras)}")

# #EXERCICIO
# texto = """Operadores de String
# Python oferece operadores para processar texto (ou seja, valores de
# string).
# Assim como os números, as strings podem ser comparadas usando operadores
# de comparação:
# ==, !=, <, > e assim por diante.
# O operador ==, por exemplo, retorna True se as strings nos dois lados do
# operador tiverem o mesmo valor (Perkovic, p. 23, 2016).
# """
# texto = texto.lower()
# print(f"Tamanho do texto = {len(texto)}")
# texto1 = texto.split()
# print(f"Tamanho da lista de palavras = {len(texto1)}")
#
# print(f"Quantidade de vezes que string ou strings aparecem = {texto.count('string')}")


# LISTAS
# Em Python, as listas podem ser construídas de várias
# maneiras:
# Usando um par de colchetes para denotar uma lista vazia: lista1 = []
# Usando um par de colchetes e elementos separados por vírgulas: lista2 = ['a',
# 'b', 'c']
# Usando uma "list comprehension": [x for x in iterable]
# Usando o construtor de tipo: list()
#
# vogais = ['a', 'e', 'i', 'o', 'u']

# for x, i in enumerate(vogais):
#     print(f"Posição = {x}, valor = {i}")

# #mesmo resultado
# vogais = []
#
# vogais.append('a')
# vogais.append('e')
# vogais.append('i')
# vogais.append('o')
# vogais.append('u')
#
# for vogal in vogais:
#     print(f"posição = {vogais.index(vogal)}, valor = {vogal}")

# #testando e aplicando conceitos na lista
# frutas = ['maça', 'banana', 'uva', 'mamão', 'maça']
# notas = [8.7, 5.2, 10, 3.5]
#
# print('maça' in frutas)
# print('abacate' in frutas)
# print('abacate' not in frutas)
# print(min(frutas))
# print(max(notas))
# print(frutas.count('maça'))
# print(frutas + notas)
# print(2* frutas)

# #outro
# lista = ['Python', 30.61, 'java', 51, ['a', 'b', 20], 'maça']
#
# print(f"Tamanho da lista = {len(lista)}")
#
# for i, item in enumerate(lista):
#     print(f"Posição = {i},\t valor = {item} -----------> tipo individual = {type(item)}")
#
#
# print("\nExemplos de slices:\n")
# print("lista[1] = ", lista[1])
# print("lista[0:2] = ", lista[0:2])
# print("lista[:2] = ", lista[:2])
# print("lista[3:5] = ", lista[3:5])
# print("lista[3:6] = ", lista[3:6])
# print("lista[3:] = ", lista[3:])
# print("lista[-2] = ", lista[-2])
# print("lista[-1] = ", lista[-1])
# print("lista[4][1] = ", lista[4][1])


# texto = 'python'

# print(texto.strip()) #remove espaços
# print(texto.lstrip()) # remove espaço da esquerda
# print(texto.rstrip()) #remove espaço da direita
#
# print(texto.center(10, '*'))
# print('.'.join(texto))
#
# for letras in texto:
#     if letras == texto[-1]:
#         print(letras)
#     else:
#         print(letras + '-', end='')
# else:
#     print("Obrigado!")


# nome = "josimar gonçalves da silva"
#
# print(nome)
# nome1 = nome.title()
# nome1 = nome1.split()
# print(nome1)
#
# print()
# nome2 = nome[:7]
# print(nome2)
# sobrenome3 = nome[:-6:-1]
# sobrenome3 = sobrenome3[::-1]
# print(sobrenome3)
# sobrenome2 = nome[:-9:-7]
# sobrenome2 = sobrenome2[::-1]
# print(sobrenome2)
# sobrenome = nome[8:17]
# print(sobrenome)
#
# print(nome2 + " " + sobrenome + " " + sobrenome2 + " " + sobrenome3)

# N = int(input())
#
# while N > 0:
#     A, B = input().split()
#
#     # Verificar se B corresponde aos últimos dígitos de A
#     encaixa = True
#
#     # Comece comparando os dígitos de A e B a partir do final
#     i = len(A) - 1
#     j = len(B) - 1
#
#     while i >= 0 and j >= 0:
#         if A[i] != B[j]:
#             encaixa = False
#             break
#         i -= 1
#         j -= 1
#
#     if j >= 0:
#         encaixa = False
#
#     if encaixa:
#         print("encaixa")
#     else:
#         print("nao encaixa")
#
#     N -= 1


