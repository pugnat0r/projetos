# Faça um programa que tenha uma lista chamada números e duas funções chamadas
# sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# A segunda função  vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.


from random import randint

números = []


def sorteia(lst):

    for c in range(0, 5):
        numrandom = randint(1, 100)
        lst.append(numrandom)

    print(f"A lista de todos os números random: {lst}")


def somaPar(lst):

    sumtemp = 0
    números_pares = []
    for p in lst:
        if p % 2 == 0:
            números_pares.append(p)
            sumtemp += p
    print(f"Números pares: {números_pares}")
    print(f"A soma do números pares: {sumtemp}")


sorteia(números)
somaPar(números)
