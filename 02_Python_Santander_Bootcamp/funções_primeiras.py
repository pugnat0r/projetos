# Palavra reservada para função def

def exibir_mensagem():
    print("Hello World!")


def exibir_mensagem_2(nome):
    print(f"{nome}!")


def exibir_mensagem_3(nome="Vitor"):
    print(f"{nome}")


exibir_mensagem()
exibir_mensagem_2(nome="vitor")
exibir_mensagem_3()
exibir_mensagem_3(nome="Echiley")
