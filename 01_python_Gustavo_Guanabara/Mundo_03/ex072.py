from click import clear


números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# entrada_user = 21

# while entrada_user < 0 or entrada_user > 20:
#     print("Entre 0 -> 20 ")
#     entrada_user = int(input("Digite um número: "))

while True:
    clear()
    entrada_user = int(input("Digite um número entre 0 e 20: "))

    if 0 <= entrada_user <= 20:
        print("~"*30)
        print(f"\nVocê digitou o {números[entrada_user]}\n")
        print("~"*30)

    e = ""

    while e == "" or e not in "SsNn":
        e = input(
            "Número inválido. Deseja tentar novamente? [S/N] ").strip()[0]

    if e in "Nn":
        print("Programa encerrado. Até mais!")
        break
