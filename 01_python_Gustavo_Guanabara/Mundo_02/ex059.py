# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

from time import sleep
from click import clear, pause

n1 = int(input("\nDigite o valor A: "))
n2 = int(input("\nDigite o valor B: "))

while True:

    menu = f"""\n

    Suas escolhas foram: A = {n1} e B = {n2}

    [===== MENU DE OPÇÕES =====]
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa
    """
    clear()
    print(menu)

    escolha_usuario = int(input("\nEscolha um número: "))

    if escolha_usuario == 1:
        print(f"\nA soma entre os números {n1} + {n2} é iqual a {n1+n2}")
        pause("\nAperte qualquer tecla para continuar...")

    elif escolha_usuario == 2:
        print(
            f"\nA multiplicação entre os números {n1} x {n2} é iqual a {n1*n2}")
        pause("\nAperte qualquer tecla para continuar...")

    elif escolha_usuario == 3:
        if n1 > n2:
            print(f"\nO número {n1} é maior que o número {n2}")
            pause("\nAperte qualquer tecla para continuar...")

        elif n2 > n1:
            print(f"\nO número {n2} é maior que o número {n1}")
            pause("\nAperte qualquer tecla para continuar...")
        else:
            print("\nOs dois números são iquais.")
            pause("\nAperte qualquer tecla para continuar...")

    elif escolha_usuario == 4:
        n1 = int(input("\nDigite o valor A: "))
        n2 = int(input("\nDigite o valor B: "))

    elif escolha_usuario == 5:
        print("\nFinalizando o programa...")
        sleep(2)
        clear()
        break

    else:
        print("\n Opção inválida! Tente Novamente.")
        pause("\nAperte qualquer tecla para continuar...")
