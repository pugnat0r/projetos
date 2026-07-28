# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: Inicio, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# de 1 até 10 de 1 em 1
# de 10 até 0, de 2 em 2
# Uma contagem personalizada.

import time


def contador(inicio, final, passo):

    if passo == 0:
        passo = 1

    elif passo < 0:
        passo *= -1

    print("-=" * 20)
    print(f"Contagem de {inicio} até {final} de {passo} em {passo}")

    # Crescente
    if inicio < final:
        for i in range(inicio, final+1, passo):
            time.sleep(0.1)
            print(f"{i}", end=" ", flush=True)
        print("FIM!")

    # Decrescente
    elif inicio > final:
        for i in range(inicio, final-1, -passo):
            time.sleep(0.1)
            print(f"{i}", end=" ", flush=True)
        print("FIM!")
        print()
    elif inicio == final:
        print("Não é possível contar, os números são iguais.")
        print()


contador(1, 10, 1)
contador(10, 0, 2)

print("Agora é sua vez de personalizar a contagem!")

inicio = int(input('Inicio: '))
final = int(input('Final: '))
passo = int(input('Passo: '))

contador(inicio, final, passo)
