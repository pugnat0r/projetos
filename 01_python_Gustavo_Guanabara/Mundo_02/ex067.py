# Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.


from click import pause, clear


while True:
    clear()

    print("~"*40)
    print("\nDigite um valor negativo para sair!\n")

    print("~"*40)
    number = int(input("Quer ver a tabuada de qual valor: "))
    print("~"*40)

    if number < 0:
        break

    cont = 1

    while cont < 11:

        print(f"\n{number} x {cont} = {number*cont}")

        cont += 1

    if cont == 11:
        pause("\nAperta qualquer tecla para colocar um novo número!")

print("\nPrograma finalizado!\n")
