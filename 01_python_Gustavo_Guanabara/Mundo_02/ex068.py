# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder
# Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

import random
from click import clear, pause

user_type = ""
win = pc_number = soma = 0

while True:
    clear()

    pc_number = random.randint(1, 10)

    print("=-" * 20)
    print(f"Vamos jogar Par ou Ímpar  | Pontuação: {win}")
    print("=-" * 20)

    user_number = int(input("\nEscolha um número 1-10: "))

    user_type = ""
    while user_type == "" or user_type not in "PI":
        user_type = str(input("\nPar ou Ímpar? [P/I]")).upper().strip()[0]


    print(f"\nVocê jogou: {user_number}")
    print(f"\nA máquina jogou: {pc_number}")

    soma = user_number + pc_number

    if (soma % 2) == 0:

        print(f"\nA soma entre {user_number} + {pc_number} = {soma} [ PAR ]")

        if user_type == "P":
            win += 1
            print("\nParabéns +1 ponto!!\n")
        else:
            break

    elif (soma % 2) != 0:

        print(f"\nA soma entre {user_number} + {pc_number} = {soma} [ ÍMPAR ]")

        if user_type == "I":
            win += 1
            print("\nParabéns +1 ponto!!\n")
        else:
            break

    pause("Aperte qualquer tecla para continuar...")


print(f"\nVocê PERDEU!  Com {win} vítorias")
