import random
from click import clear
clear()

maior = menor = 0

números_random = (random.randint(1, 10), random.randint(
    1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

print('^~'*15)
for c in range(0, 5):
    print(f' {números_random[c]} | ', end="")

    if números_random[c] > maior:
        maior = números_random[c]

    if números_random[c] < menor or menor == 0:
        menor = números_random[c]
print("")
print("~^"*15)

print(f"\nO maior número foi: {maior}")
print(f"\nO maior número foi: {menor}\n")
