import sqlite3
from datetime import datetime
from time import sleep

# com banco de dados funcional, porém incompleto, falta polimento e algumas estruturas de decisões
con = sqlite3.connect('Sistema_Bancario_2.0.db')
con.row_factory = sqlite3.Row  # Utilizar a classe sqlite3.Row
cursor = con.cursor()

# Verifica se a tabela já existe antes de criar
cursor.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='clientes';
""")

if not cursor.fetchone():
    # Cria a tabela somente se ela não existir
    cursor.execute("""CREATE TABLE "clientes" (
        "NOME" TEXT,
        "CPF" TEXT,
        "DATA DE NASCIMENTO" TEXT,
        "ENDEREÇO" TEXT
    );""")

cursor.execute("""
SELECT name FROM sqlite_master WHERE  type='table' AND name = 'contas';
""")

if not cursor.fetchone():
    cursor.execute("""CREATE TABLE "contas" (
    "CLIENTE" TEXT,
    "CPF" TEXT,
    "SALDO" FLOAT,
    "NÚMERO" INT,
    "AGÊNCIA" TEXT,
    "BANCO" TEXT
    );""")

cursor.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='historico';
""")

if not cursor.fetchone():
    # Cria a tabela 'historico' somente se ela não existir
    cursor.execute("""CREATE TABLE "historico" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "conta_id" INTEGER,
        "tipo" TEXT,
        "valor" FLOAT,
        "data_hora" TEXT,
        FOREIGN KEY (conta_id) REFERENCES contas(NÚMERO)  -- Modificado para referenciar a coluna correta
    );""")


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def adicionar_conta(self, conta):
        pass


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_de_nascimento, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_de_nascimento = data_de_nascimento


class Conta:
    def __init__(self, cliente):
        self._cliente = cliente


class Historico:
    def __init__(self, conta_id):
        self._conta_id = conta_id
        self._transacoes = []

    def adicionar_transacao(self, tipo, valor):
        data_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        transacao = (self._conta_id, tipo, valor, data_hora)
        # Adiciona a transação à tabela 'historico' no banco de dados
        cursor.execute("INSERT INTO historico (conta_id, tipo, valor, data_hora) VALUES (?, ?, ?, ?)",
                       (self._conta_id, tipo, valor, data_hora))
        con.commit()

    def get_transacoes(self):
        cursor.execute("SELECT * FROM historico WHERE conta_id=?", (self._conta_id,))
        transacoes = cursor.fetchall()
        return transacoes


class ContaCorrente(Conta):
    def __init__(self, historico, cliente, numero, agencia='0001', limite=500, limite_saques=3, banco="1414"):
        self._historico = historico
        self._numero = numero
        self._saldo = 0
        self._agencia = agencia
        self._limite = limite
        self._limite_saques = limite_saques
        self._banco = banco
        super().__init__(cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero(self):
        return self._numero

    def registrar_transacao(self, tipo, valor):
        if tipo in ('DEPOSITO', 'SAQUE'):
            if tipo == 'SAQUE' and valor > self._saldo + self._limite:
                print("Saldo insuficiente para saque.")
                return
            self._saldo += valor if tipo == 'DEPOSITO' else -valor
            self._historico.adicionar_transacao(tipo, valor)
            print(f"Transação registrada: {tipo} de R${valor:.2f}. Novo saldo: R${self._saldo:.2f}")
        else:
            print("Tipo de transação inválido.")


def verificar_cliente(cpf, clientes):
    cursor.execute("SELECT * FROM clientes WHERE CPF=?", (cpf,))
    cliente = cursor.fetchone()
    return cliente if cliente else None


# ...

def verificar_conta(cpf, contas):
    cursor.execute("SELECT * FROM contas WHERE CPF=?", (cpf,))
    conta_info = cursor.fetchone()

    if conta_info:
        numero_conta = conta_info['NÚMERO']
        agencia = conta_info['AGÊNCIA']
        saldo = conta_info['SALDO']
        cliente_nome = conta_info['CLIENTE']

        cliente = verificar_cliente(cpf, contas)
        historico_conta_corrente = Historico(numero_conta)  # Use o número da conta como conta_id
        conta_corrente = ContaCorrente(historico_conta_corrente, cliente=cliente['nome'], agencia=agencia,
                                       numero=numero_conta)
        conta_corrente._saldo = saldo  # Defina o saldo diretamente
        conta_corrente._numero = numero_conta  # Defina o número da conta

        return conta_corrente

    return None


# ...


def cadastrar_conta(contas, clientes):
    cpf = input("Informe o CPF do cliente: ")
    cpf = cpf.replace(".", "").replace('-', "")
    cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    cliente = verificar_cliente(cpf, clientes)
    conta = verificar_conta(cpf, contas)

    if conta:
        print("Conta já cadastrada com esse CPF!!!")
    else:
        if not cliente:
            print("Cliente não encontrado para associar à conta.")
            return

        numero = len(contas) + 1
        agencia = '0001'
        banco = '1414'

        historico_conta_corrente = Historico(numero)  # Agora, o número da conta é usado como conta_id
        conta_corrente = ContaCorrente(historico_conta_corrente, cliente=cliente['nome'])

        contas.append(conta_corrente)

        print("Conta criada com sucesso!!!")
        cursor.execute("INSERT INTO contas (CLIENTE, CPF, SALDO, NÚMERO, AGÊNCIA, BANCO) VALUES (?, ?, ?, ?, ?, ?)",
                       (cliente['nome'], cpf, conta_corrente.saldo, numero, agencia, banco))

        con.commit()


def cadastrar_cliente(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cpf = cpf.replace(".", "").replace('-', "")
    cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    contagem_cpf = len(cpf)
    if contagem_cpf == 14:
        cliente = verificar_cliente(cpf, clientes)

        if cliente:
            print("CPF já cadastrado!!!")
            return

        else:

            nome = str(input("Informe seu nome completo: ")).title()
            print("Informe sua data de nascimento!")
            dia = input("DIA: ")
            mes = input("MÊS: ")
            ano = input("ANO: ")

            data_de_nascimento = f"{dia}/{mes}/{ano}"

            print("Informe seu endereço!")
            rua = input("RUA: ")
            numero = input("NÚMERO: ")
            bairro = input("BAIRRO: ")
            cidade = input("CIDADE: ")
            estado = input("SIGLA DO ESTADO: ")
            endereco = f"{rua}, nº[{numero}], {bairro}--{cidade}/{estado}".upper()

            cliente = PessoaFisica(nome=nome, cpf=cpf, data_de_nascimento=data_de_nascimento, endereco=endereco)

        clientes.append(cliente)

        print("Cliente Criado com sucesso!!!")
        cursor.execute("INSERT INTO clientes (NOME, CPF, \"DATA DE NASCIMENTO\", ENDEREÇO) VALUES (?, ?, ?, ?)",
                       (nome, cpf, data_de_nascimento, endereco))

        con.commit()
    else:
        print("CPF INVÁLIDO! MODELO=(000.000.000-00)")


def mostrar_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    for cliente in clientes:
        print(
            f"Nome: \033[31m{cliente['NOME']}\033[m, CPF: \033[31m{cliente['CPF']}\033[m, Data de Nascimento: \033[31m{cliente['DATA DE NASCIMENTO']}\033[m, "
            f"Endereço: \033[31m{cliente['ENDEREÇO']}\033[m\n")


def mostrar_historico(clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cpf = cpf.replace(".", "").replace('-', "")
    cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    cliente = verificar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não possui histórico.")
        return

    conta_corrente = verificar_conta(cpf, contas)
    if not conta_corrente:
        print("Conta não encontrada para mostrar o histórico.")
        return

    historico = Historico(conta_corrente.numero)
    transacoes = historico.get_transacoes()

    print(f"Histórico de transações para a conta {conta_corrente.numero}:")

    for transacao in transacoes:
        print(
            f"Data e Hora: {transacao['data_hora']}, Tipo: {transacao['tipo']}, Valor: R${transacao['valor']:.2f}")

    print("\n")


def sacar(clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cpf = cpf.replace(".", "").replace('-', "")
    cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    cliente = verificar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado para associar à conta.")
        return

    else:
        valor = float(input("Informe o valor a ser Sacado: "))
        conta_corrente = verificar_conta(cpf, contas)
        if not conta_corrente:
            print("Conta não encontrada para realizar depósito!")
            return

        if valor > 0:
            novo_saldo = conta_corrente.saldo
            novo_saldo = novo_saldo - valor

            cursor.execute("UPDATE contas SET SALDO=? WHERE CPF=?",
                           (novo_saldo, cpf))
            con.commit()

            conta_corrente.registrar_transacao("SAQUE", valor)

        else:
            print("Não pode Sacar uma quantia zerada, ou negativa...")


def depositar(clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cpf = cpf.replace(".", "").replace('-', "")
    cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    cliente = verificar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado para associar à conta.")
        return

    conta_corrente = verificar_conta(cpf, contas)
    if not conta_corrente:
        print("Conta não encontrada para realizar depósito!")
        return

    else:
        valor = float(input("Informe o valor a ser Depositado: "))
        if valor > 0:
            novo_saldo = conta_corrente.saldo
            novo_saldo = novo_saldo + valor

            cursor.execute("UPDATE contas SET SALDO=? WHERE CPF=?",
                           (novo_saldo, cpf))
            con.commit()

            conta_corrente.registrar_transacao("DEPOSITO", valor)
        else:
            print("Não pode Depositar uma quantia zerada, ou negativa...")


def deletar_conta():
    cpf = input("Informe o CPF do cliente: ")
    cpf = cpf.replace(".", "").replace('-', "")
    cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    conta_id_para_deletar = cpf
    print(f"Conta ID {conta_id_para_deletar} deletada com sucesso.")
    cursor.execute("DELETE FROM contas WHERE CPF=?", (cpf,))
    con.commit()


def deletar_cliente():
    cpf = input("Informe o CPF do cliente: ")
    cpf = cpf.replace(".", "").replace('-', "")
    cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    cliente_id_para_deletar = cpf
    print(f"Cliente ID {cliente_id_para_deletar} deletada com sucesso.")
    cursor.execute("DELETE FROM clientes WHERE CPF=?", (cpf,))
    con.commit()


def menu():
    titulo = "Banco Silva"
    opcoes = ["CADASTRO", "CD-CONTA", "DEPOSITAR", "SACAR", "CLIENTES", "HISTÓRICO","DELETAR CLIENTE", "DELETAR CONTA", "SAIR"]

    # Calcula o comprimento máximo entre o título e as opções
    comprimento_maximo = max(len(titulo), max(len(opcao) for opcao in opcoes))
    x = '-'
    # Gera o cabeçalho do menu
    print(f"{'-' * (comprimento_maximo + 26)}")
    print(f"-    {titulo.center(comprimento_maximo + 19)} {x.ljust(0)}")

    # Gera as opções do menu
    for i, opcao in enumerate(opcoes, start=1):
        print(f"-{' ' * 10}[{i}]-{opcao.ljust(comprimento_maximo + 9)} {x.ljust(0)}")

    print(f"{'-' * (comprimento_maximo + 26)}")


def main():
    clientes = []
    contas = []
    while True:
        menu()
        opcao = int(input('-->'))
        if opcao == 1:
            cadastrar_cliente(clientes)
        elif opcao == 2:
            cadastrar_conta(contas, clientes)
        elif opcao == 3:
            depositar(clientes, contas)
        elif opcao == 4:
            sacar(clientes, contas)
        elif opcao == 5:
            mostrar_clientes()
        elif opcao == 6:
            mostrar_historico(clientes, contas)
        elif opcao == 7:
            deletar_cliente()
        elif opcao == 8:
            deletar_conta()
        elif opcao == 9:
            print("\033[34mSaindo do Sistema\033[m", end='')
            for x in range(8):
                print('\033[31m.', end='')
                sleep(0.7)
            break



main()

con.close()
