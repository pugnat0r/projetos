from random import randint
import time

palpites = []
number = list()

while True:
    qtd = int(input("Quantos jogos você quer que eu sorteie?: "))

    for i in range(0, qtd):

        for n in range(0, 6):
            #
            while True:

                n_temp = randint(1, 60)

                if n_temp not in number:
                    number.append(n_temp)
                    break

        number.sort()
        palpites.append(number[:])
        number.clear()

    if i == qtd - 1:
        break

print()
print("-"*35)
print(f"{'JOGO NA MEGA SENA':^35}")
print("-"*35)
print()

for pos, item in enumerate(palpites):
    print(f"Jogo {pos+1}: {item}")
    time.sleep(1)

print()
print(f"{'< BOA SORTE >':-^35}")
print()
