from click import clear, pause


def menu(mensagem):

    texto_menu = f"""

    ============ PUGN4T0R Wallet ============

    [ 1 ] - Criar conta
                 
    [ 2 ] - Minha conta

    [ 3 ] - Total de clientes

    [ 0 ] - Sair

    ========================================
    {mensagem}
    >>> """
    return input(texto_menu)


def create_users(*, usuarios, total_de_usuarios, id):

    user = input("\n\n    Primeiro nome: ").title()

# -----------------------------------------------------------------------------------
    born_date = input("\n\n    Data de nascimento: ")

    if born_date.isdigit() and len(born_date) == 8:
        born_date = f"{born_date[:2]}/{born_date[2:4]}/{born_date[4:8]}"
    else:

        return usuarios, total_de_usuarios, id, "\n\n    Entre com uma data no formato certo! 13122001! \n\n"
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
    cpf = input("\n\n    CPF: ")

    if cpf.isdigit() and len(cpf) == 11:
        if any(cpf == interando["CPF"] for interando in usuarios):
            return usuarios, total_de_usuarios, id, "\n\n    CPF já cadastrado! \n\n"

    else:

        return usuarios, total_de_usuarios, id, "\n\n    Entre com um cpf no formato certo! xxxXXXxxxXX \n\n"
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
    address = input("\n\n    Qual seu estado: ").upper()
    address = f"{address[:2]}"
# -----------------------------------------------------------------------------------

    total_de_usuarios += 1

    id[cpf] = total_de_usuarios - 1

# -----------------------------------------------------------------------------------

    usuarios.append(
        {"nome": user, "born_date": born_date, "CPF": cpf,
            "address": address, "saldo": 0, "extrato": ""}
    )


# -----------------------------------------------------------------------------------
    return usuarios, total_de_usuarios, id, "\n    Conta criada com sucesso! <3\n"


def conta(clientes, id):

    cpf = input("\n    Digite seu CPF: ")
    clear()

    if cpf.isdigit() and len(cpf) == 11:
        if any(cpf == interando["CPF"] for interando in clientes):

            id_escolhido = id[f"{cpf}"]
            cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

            while True:
                clear()
                texto_menu = f"""

    ============ Minha Conta ============

    [ Cpf  ]     - {cpf}

    [ Nome ]     - {clientes[id_escolhido]["nome"]}

    [ Born ]     - {clientes[id_escolhido]["born_date"]}

    [ Endereço ] - {clientes[id_escolhido]["address"]}

    [ Agência ]  - 001

    [ ID ]       - {id_escolhido}

    ========================================
    [ SALDO ]: R$ {clientes[id_escolhido]["saldo"]}
    ========================================

    [ 1 ] Depositar
    [ 2 ] Sacar
    [ 3 ] Extrato
    [ 0 ] Voltar
    """
                print(texto_menu)

                escolha = input("    Escolha uma opção: ")

                if escolha == "1":
                    depositar(clientes, id_escolhido)

                elif escolha == "2":
                    saque(clientes, id_escolhido)

                elif escolha == "3":
                    extrato(clientes, id=id_escolhido)

                elif escolha == "0":
                    msg = "\n    Volte Sempre!\n "
                    return msg

    msg = "\n    CPF não encontrado! \n"
    return msg


def all_users(id):
    clear()
    print("    ============ Todos os Clientes ============")

    for chave, valor in id.items():

        print(f"""
    ___________________________________________
    {valor + 1}° conta
    CPF: {chave}
    ___________________________________________
                  """)

    print("    ===========================================")
    pause("    Aperte qualquer tecla para continuar! ")


def depositar(usuarios, id):

    deposito = float(input("""
    ========================================
                     
    Digitie o valor do depósito: """))

    if deposito > -1:
        usuarios[id]["saldo"] += deposito
        usuarios[id]["extrato"] += f"\n    Depósito: R$ +{deposito:.2f}"

    else:
        print("\n    Operação falhou! O valor do depósito deve ser positivo.\n")
        pause("\n    Aperte qualquer tecla para continuar! ")


def saque(usuarios, id):

    limit_saque = usuarios[id]["extrato"].count("Saque")

    saque = float(input("""
    ========================================
                     
    Digitie o valor do saque: """))

    if limit_saque < 3:
        if (0 < saque <= 500) and (saque <= usuarios[id]["saldo"]):
            usuarios[id]["saldo"] -= saque
            usuarios[id]["extrato"] += f"\n    Saque:    R$ -{saque:.2f}"

        else:
            print("""
    Operação falhou! 
    O valor do saque deve ser positivo ou ter saldo na conta!
    Não pode ser maior de R$ 500,00
    Você só pode sacar 3x ao dia!.
                  """)
        pause("\n    Aperte qualquer tecla para continuar! ")

    else:
        print("""
    Operação falhou! 
    O valor do saque deve ser positivo ou ter saldo na conta!
    Não pode ser maior de R$ 500,00
    Você só pode sacar 3x ao dia!.
                  """)
        pause("\n    Aperte qualquer tecla para continuar! ")


def extrato(usuarios, /, *, id):
    clear()
    extrato = f"""
    =============== Extrato ================
    {usuarios[id]["extrato"]}

    ========================================
    Saldo atual: {usuarios[id]["saldo"]}
    ========================================
    """
    print(extrato)
    pause("\n    Aperte qualquer tecla para continuar! ")


def main():

    clientes = []
    total_de_clientes = 0
    id = {}

    msg = "\n    Nenhuma mensagem.\n"

    while True:

        clear()
        opção = menu(msg)

        if opção == "1":
            clientes, total_de_clientes, id, msg = create_users(
                usuarios=clientes, total_de_usuarios=total_de_clientes, id=id)

        elif opção == "2":

            msg = conta(clientes, id)

        elif opção == "3":
            all_users(id)
            msg = "\n    Nenhuma mensagem.\n"

        elif opção == "0":
            clear(), print("\n    Programa finalizado! \n"), exit()

        else:
            msg = "\n    Opção inválida, tente novamente.\n"


main()
