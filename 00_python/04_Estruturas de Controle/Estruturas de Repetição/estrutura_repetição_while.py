from click import clear


opção = -1

while opção != 0:

    print("___________________________")
    print()
    print("[1] Sacar \n[2] Extrato \n[0] Sair ")
    print("___________________________")
    opção = int(input("Opção: "))

    if opção == 1:
        clear()
        print("___________________________")
        print()
        print("Saque realizado com sucesso!")

    elif opção == 2:
        clear()
        print("___________________________")
        print()
        print("Exibindo extrato...")

else:
    clear()
    print("___________________________")
    print()
    print("Saindo do sistema...")
    print("___________________________")
