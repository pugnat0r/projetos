def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("_________________________________________________")
        print("Valor sacado! ")
        print("Retire  o seu dinheiro na boca do caixa. ")
        print("Obrigado por ser nosso cliente, tenha um bom dia! ")
        print("_________________________________________________")
    else:
        print("_________________________________________________")
        print("Saldo insuficiente! ")
        print("Tente novamente com um valor menor. ")
        print("Obrigado por ser nosso cliente, tenha um bom dia! ")
        print("_________________________________________________")


def depositar(valor):
    saldo = 500
    saldo += valor


print("_________________________________________________")
print("")
sacar(float(input("Digite o valor que deseja sacar: ")))

