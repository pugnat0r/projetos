# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
import time


def maior(*núm):

    print("="*40)
    print("Analisando os valores...")
    print(f"Você enviou {len(núm)} números para analisar!")
    if len(núm) == 0:
        print("O maior valor informado foi 0. ")
        return
    ultimo = núm[0]
    for i in núm:
        time.sleep(0.1)
        print(i, end=" ", flush=True)
        if i > ultimo:
            ultimo = i
    print("")
    print(f"O maior foi {ultimo}")


maior(1, 3, 5, 110)

maior(100, 3, 4, 5, 6)

maior(2, 4, 5, 1000, 3, 6, 1, 0)

maior(-1, -3, -4, -6, -10)

maior()
