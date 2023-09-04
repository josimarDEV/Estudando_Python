import time

menu = int(input("""
======BANCO SILVA======
     [1]-DEPÓSITO
     [2]-SACAR
     [3]-EXTRATO
     [4]-SAIR
=======BEM VINDO=======    
"""))

saldo = 2500.0
qtde_saque = 0
LIMITES_SAQUES = 3
extrato = []


def realizar_deposito(valor, saldo):
    if valor > 0:
        time.sleep(1)
        print(f"Saldo atual: R$ {saldo:.2f}")
        time.sleep(1)
        print(f"Foram depositados: R$ {valor:.2f} em sua conta!")
        saldo += valor
        time.sleep(2)
        print(f"Novo saldo: R$ {saldo:.2f}\n")
        extrato.append(f"Depósíto: R$ {valor:.2f}")
    else:
        print("\nERRO: Valor de depósito inválido. Tente novamente!\n")


def realizar_saque(saque, saldo):
    if 0 < saque <= saldo:
        time.sleep(1)
        print("Saque realizado com sucesso!")
        time.sleep(1)
        print(f"Saldo atual: R$ {saldo:.2f}")
        time.sleep(2)
        print(f"Você sacou: R$ {saque:.2f}")
        saldo -= saque
        print(f"Novo saldo: R${saldo:.2f}\n")
        extrato.append(f"Saque: R$ {saque:.2f}")
    else:
        print("\nNão foi possível realizar o saque. Verifique seu saldo e o valor de saque.\n")


while True:
    if menu == 1:
        deposito = float(input("Valor a ser depositado: R$ "))
        realizar_deposito(deposito, saldo)
        if deposito > 0:
            saldo += deposito
    elif menu == 2:
        saque = float(input("Valor a ser sacado: R$ "))
        if saque > saldo:
            print(f"Não foi possível realizar o saque! Verifique seu Saldo e Tente novamente!")
        elif saque <= 500:
            if qtde_saque < LIMITES_SAQUES:
                qtde_saque += 1
                realizar_saque(saque, saldo)
                if saque > 0:
                    saldo -= saque
            else:
                print("\nLimite de saque atingido!\nRetorne outro dia!")
        else:
            print("Limite máximo de R$ 500 por transação!")
    elif menu == 3:
        if len(extrato) == 0:
            print("Não foram realizados movimentações!")
        else:
            for item in extrato:
                time.sleep(1)
                print(f"Operação: {item}")
    elif menu == 4:
        print("Saindo do sistema do Banco Silva. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")

    time.sleep(2)
    print("""
    ======BANCO SILVA======
         [1]-DEPÓSITO
         [2]-SACAR
         [3]-EXTRATO
         [4]-SAIR
    =======BEM VINDO=======    
    """)
    menu = int(input("Escolha uma opção: "))
