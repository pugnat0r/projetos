saldo = 2000
cheque_especial = 450


print("_______________________________")
print((""))
print(" [ 1 ] - Conta Universitária")
print(" [ 2 ] - Conta Normal")
print((""))
print("_______________________________")
tipo_conta = int((input("Digite o tipo de conta: ")))


if tipo_conta == 1:  # Conta Universitária
    print("_______________________________")
    print("")
    print("Saldo:", saldo)
    print("")
    print("_______________________________")
    saque_valor = int(input("Digite o valor do saque: "))

    if saldo >= saque_valor:
        print("_______________________________")
        print("Saque realizado com sucesso!")
        print(f"Saldo atual: {saldo - saque_valor}")
        print("_______________________________")
    else:
        print("_______________________________")
        print("Saldo insuficiente para realizar o saque.")
        print(f"Saldo atual: {saldo}")
        print("_______________________________")


elif tipo_conta == 2:  # Conta Normal

    print("_______________________________")
    print("")
    print("Saldo:", saldo)
    print("Saldo cheque especial:", cheque_especial)
    print("")
    print("_______________________________")
    saque_valor = int(input("Digite o valor do saque: "))

    if saldo + cheque_especial >= saque_valor:

        if saldo - saque_valor < 0:
            print("_______________________________")
            print("Saque realizado com sucesso!")
            print(
                f"Saldo cheque especial: {saldo + cheque_especial - saque_valor}")
            print("_______________________________")
            print("")

        else:
            print("_______________________________")
            print("Saque realizado com sucesso!")
            print(f"Saldo atual: {saldo - saque_valor}")
            print("_______________________________")
            print("")
    else:
        print("_______________________________")
        print("Saldo insuficiente para realizar o saque.")
        print(f"Saldo atual: {saldo}")
        print(f"Saldo cheque-especial: {cheque_especial}")
        print("_______________________________")

else:
    print("_______________________________")
    print("Opção inválida, tente novamente.")
    print("_______________________________")
    exit()
