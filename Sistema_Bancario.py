import time
# com def
menu = int(input("""
======BANCO SILVA======
     [1]-CADASTRO
     [2]-CADASTRAR CONTA CORRENTE
     [3]-DEPOSITAR
     [4]-SACAR
     [5]-EXTRATO
     [6]-EXIBIR USUÁRIOS
     [7]-SAIR
=======BEM VINDO=======    
"""))

extrato = []
lista_de_usuarios = []
conta_corrente = []
saldo = 0
numero_saques = 0
LIMITE_SAQUE = 3
numero_da_conta = 1  # Número da primeira conta disponível

# Um dicionário que mapeia o número da conta para o ID do usuário
contas_por_numero = {}


def realizar_deposito():
    global saldo
    valor = float(input("Valor a ser depositado: R$ "))
    if valor > 0:
        print(f"Saldo atual: \033[034mR${saldo:.2f}\033[m")
        print(f"Foram depositados: \033[032mR${valor:.2f}\033[m em sua conta!")
        saldo += valor
        print(f"Novo saldo: \033[035mR${saldo:.2f}\033[m\n")
        extrato.append(f"Depósíto: \033[032mR${valor:.2f}\033[m")
    else:
        print("\nERRO: Valor de depósito inválido. Tente novamente!\n")
    return valor, saldo


def realizar_saque():
    global saldo
    global numero_saques
    limite = 500
    limite_saques = 3
    valor = float(input("Digite o valor a ser sacado: "))
    if valor > 0:
        if numero_saques == limite_saques:
            print("\033[031mLIMITE de saque atingido.\033[m Retorne amanhã.")
        elif valor > limite:
            print("\033[031mLIMITE de R$500\033[m por saque.")
        else:
            print("Saque realizado com sucesso!")
            print(f"Saldo atual: \033[034mR${saldo:.2f}\033[m")
            print(f"Você sacou: \033[031mR${valor:.2f}\033[m")
            saldo -= valor
            print(f"Novo saldo: \033[035mR${saldo:.2f}\033[m\n")
            extrato.append(f"Saque:    \033[031mR${valor:.2f}\033[m")
            numero_saques += 1
    else:
        print("\nNão foi possível realizar o saque. Verifique seu saldo e o valor de saque.\n")
    return valor, saldo, numero_saques


def ver_extrato():
    global extrato
    if len(extrato) == 0:
        print("Não foram realizados movimentações!")
    for item in extrato:
        print(f"Operação: {item}")


def cadastrar_usuario():
    nome = str(input("Informe seu nome: "))
    sobrenome = str(input("Informe seu sobrenome: "))
    idade = str(input("Informe sua idade: "))

    email = str(input("Informe seu email: "))
    for usuario in lista_de_usuarios:
        if usuario['Email'] == email:
            print("Email já cadastrado!")
            return

    cpf = str(input("Informe seu CPF: "))
    for usuario in lista_de_usuarios:
        if usuario['CPF'] == cpf:
            print("CPF já está cadastrado. Verifique com nosso Gerente.")
            return

    print("\nInforme o seu endereço.")
    rua = str(input("Informe sua Rua: "))
    numero = str(input("Informe o número de sua residência: "))
    bairro = str(input("Informe seu Bairro: "))
    cidade_sigla = str(input("Informe sua cidade/estado (sigla): "))

    usuario = {
        'Nome': nome,
        'Sobrenome': sobrenome,
        'Idade': idade,
        'Email': email,
        'CPF': cpf,
        'Rua': rua,
        'Numero': numero,
        'Bairro': bairro,
        'Cidade': cidade_sigla
    }
    lista_de_usuarios.append(usuario)
    print("\nUsuário cadastrado com Sucesso")


def exibir_usuarios():
    print("\nUsuários Cadastrados:")
    for usuario in lista_de_usuarios:
        print("Nome:", usuario['Nome'])
        print("Sobrenome:", usuario['Sobrenome'])
        print("Idade:", usuario['Idade'])
        print("Email:", usuario['Email'])
        print("CPF:", usuario['CPF'])
        print()


def cadastrar_conta_corrente():
    agencia = '0001'
    global numero_da_conta
    usuario_id = len(lista_de_usuarios)

    while True:
        numero_conta = str(numero_da_conta)
        if numero_conta not in contas_por_numero:
            corrente = {
                'Agência': agencia,
                'Número da conta': numero_conta,
                'ID do Usuário': usuario_id
            }
            conta_corrente.append(corrente)
            contas_por_numero[numero_conta] = usuario_id
            print('\nConta cadastrada com sucesso')
            numero_da_conta += 1
            break
        else:
            numero_da_conta += 1


def corrente():
    for conta in conta_corrente:
        print("Agência:", conta['Agência'])
        print("Conta:", conta['Número da conta'])
        print()


while True:
    if menu == 1:
        cadastrar_usuario()
    elif menu == 2:
        cadastrar_conta_corrente()
    elif menu == 3:
        realizar_deposito()
    elif menu == 4:
        realizar_saque()
    elif menu == 5:
        ver_extrato()
    elif menu == 6:
        exibir_usuarios()
    elif menu == 7:
        corrente()
    elif menu == 8:
        print("Saindo do sistema do Banco Silva. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")

    print("""
======BANCO SILVA======
     [1]-CADASTRO
     [2]-CADASTRAR CONTA CORRENTE
     [3]-DEPOSITAR
     [4]-SACAR
     [5]-EXTRATO
     [6]-EXIBIR USUÁRIOS
     [7]-EXIBIR CONTAS
     [8]-SAIR
=======BEM VINDO=======    
""")
    menu = int(input("Escolha uma opção: "))
