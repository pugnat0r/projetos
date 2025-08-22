import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def menu(mensagem):
    clear()
    texto = f"""
    ============== MENU ==============

    [1] Escolher mensagem
    [2] Sair

    Mensagem atual: {mensagem}

    ==================================
    => """
    return input(texto)


def escolher_mensagem():
    clear()
    print("""
    =========== ESCOLHER MENSAGEM ===========
    
    [1] "Seja bem-vindo ao sistema!"
    [2] "Você é incrível, continue assim!"
    [3] "Hoje é um ótimo dia para aprender Python!"

    =========================================
    """)
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        return "Seja bem-vindo ao sistema!"
    elif escolha == "2":
        return "Você é incrível, continue assim!"
    elif escolha == "3":
        return "Hoje é um ótimo dia para aprender Python!"
    else:
        return "Opção inválida. (mensagem anterior mantida)"


def main():
    mensagem_atual = "Nenhuma mensagem escolhida ainda."

    while True:
        opcao = menu(mensagem_atual)

        if opcao == "1":
            mensagem_atual = escolher_mensagem()
        elif opcao == "2":
            print("\nSaindo... até logo!")
            break
        else:
            mensagem_atual = "Opção inválida! Tente novamente."


# Executa o programa
main()
