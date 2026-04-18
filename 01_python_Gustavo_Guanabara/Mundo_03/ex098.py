import time


def simples():
    print("-=" * 20)
    print("Contagem de 1 até 10 de 1 em 1")
    for i in range(1, 11):
        time.sleep(0.4)
        print(f"{i}", end=" ", flush=True)
    print("FIM!")


def complexa():
    print("-=" * 20)
    print("Contagem de 10 até 0 de 2 em 2")

    for i in range(10, -2, -2):
        time.sleep(0.4)
        print(f"{i}", end=" ", flush=True)
    print("FIM!")


def custom():
    print("Agora é sua vez de personalizar a contagem!")

    inicio = int(input('Inicio: '))
    final = int(input('Final: '))
    passo = int(input('Passo: '))

    if passo <= 0:
        passo = 1

    print("-=" * 20)
    print(f"Contagem de {inicio} até {final} de {passo} em {passo}")

    if inicio < final:
        for i in range(inicio, final+1, passo):
            time.sleep(0.4)
            print(f"{i}", end=" ", flush=True)
        print("FIM!")

    # Decrescente
    elif inicio > final:
        for i in range(inicio, final-1, -passo):
            time.sleep(0.4)
            print(f"{i}", end=" ", flush=True)
        print("FIM!")
        print()
    elif inicio == final:
        print("Não é possível contar, os números são iguais.")
        print()


# simples()
# complexa()
custom()
