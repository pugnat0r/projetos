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
    escolha = input(menu + mensagem + "Escolha uma opção: ")
    
    if escolha == "1":
        deposito = float(input("Digitie o valor do depósito: "))
        if deposito > -1:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            mensagem = f"""
Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}\n
========================================
"""
        else:
            mensagem = "Operação falhou! O valor do depósito deve ser positivo.\n"

    elif escolha == "2":
        saque = float(input("Digite o valor do saque: "))

        limite_saque_diário = numero_saques < NUMERO_SAQUES
        limite_saque_valor = saque <= limite
        limite_saldo = saque <= saldo

        if limite_saque_diário:
            print()
