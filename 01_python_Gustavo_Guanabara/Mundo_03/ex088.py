from random import randint

from click import clear

palpites = []
number = list()

while True:
    qtd = int(input("Quantos jogos deseja?: "))

    for i in range(0, qtd):

        for n in range(0, 6):
            number.append(randint(0, 60))

        palpites.append(number[:])
        number.clear()

    if i == qtd - 1:
        break

for pos, item in enumerate(palpites):
    print(f"Seu {pos+1}° palpite: {item}")
