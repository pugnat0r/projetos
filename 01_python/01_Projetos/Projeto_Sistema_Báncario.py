from click import clear


saldo = 0
extrato = ""
saque = 0

limite = 500
numero_saques = 0
NUMERO_SAQUES = 3

mensagem = ""

menu = f"""

============ PUGN4T0R Wallet ============

    [ 1 ] - Depositar

    [ 2 ] - Sacar

    [ 3 ] - Extrato

    [ 0 ] - Sair

========================================
"""

while True:
    clear()
    escolha = input(menu + mensagem + "Escolha uma opção: ").strip()
    print(escolha)

# Depositar

    if escolha == "1":
        deposito = float(
            input("========================================\nDigitie o valor do depósito: "))

        if deposito > -1:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            mensagem = f"\nDepósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}\n\n========================================\n"

        else:
            mensagem = "\nOperação falhou! O valor do depósito deve ser positivo.\n\n========================================\n"

# Sacar

    if escolha == "2":
        saque = float(
            input("========================================\nDigite o valor do saque: "))

        if numero_saques >= NUMERO_SAQUES:
            mensagem = f"\nQuantidade de saques atigindo por hoje! 03 de 03 ! Tente novamente amanhã ! Saldo atual: R$ {saldo:.2f}\n\n========================================\n"

        elif (saque <= limite):
            if saque < 0:
                mensagem = f"\nSaque não pode ser um valor negativo ! Saldo atual: R$ {saldo:.2f}\n\n========================================\n"
            elif saque <= saldo:
                saldo -= saque
                numero_saques += 1
                extrato += f"Saque: R$ {saque:.2f}\n"
                mensagem = f"\nSaque realizado com sucesso! Saldo atual: R$ {saldo:.2f}\n\n========================================\n"
            else:
                mensagem = f"\nOperação falhou! Saldo insuficiente!! ! Saldo atual: R$ {saldo:.2f}\n\n========================================\n"
        else:
            mensagem = f"\nSaque maior que o Limite de R$ 500,00 ! Saldo atual: R$ {saldo:.2f}\n\n========================================\n"

# Extrato

    if escolha == "3":
        mensagem = f"\n=============== EXTRATO ================\n\n{extrato} \n\nSaldo Atual: R$ {saldo:.2f}\n\n========================================\n"
