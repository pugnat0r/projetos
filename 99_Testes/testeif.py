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
            mensagem = f"\nDepósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}\n\n========================================\n"
        else:
            mensagem = "Operação falhou! O valor do depósito deve ser positivo.\n"

    elif escolha == "2":
        saque = float(input("Digite o valor do saque: "))

        if numero_saques > NUMERO_SAQUES:
            print("Você já atingiu o limite de saques diários. São apenas 3 por dia!")

       #elif limite_saque_valor:
            print(
                "Você já atingiu o limite de saque diário. O valor máximo é de R$ 500,00!")

       # elif limite_saldo:
            saldo -= saque
            estrato += f"Saque: R$ {saque:.2f}\n"
            mensagem = f"Saque realizado com sucesso! Saldo R$ {saldo:.2f}\n\n========================================\n"

        else:
            mensagem = "Operação falhou! Você não tem saldo suficiente.\n"
        print("Hello Wolrd")
