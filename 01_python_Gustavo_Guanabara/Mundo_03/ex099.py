# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*núm):

    print("="*40)
    ultimo = núm[0]
    for i in núm:
        if i > ultimo:
            ultimo = i
    print(f"Você enviou {len(núm)} números para analisar!")
    print(núm)
    print(f"O maior foi {ultimo}")


maior(1, 3, 5, 110)

maior(100, 3, 4, 5, 6)

maior(2, 4, 5, 1000, 3, 6, 1, 0)

maior(-1, -3, -4, -6, -10)
