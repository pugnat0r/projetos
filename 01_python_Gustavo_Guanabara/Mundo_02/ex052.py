
n = int(input("Digite um número: "))

contador = 0

for c in range(1, n + 1):
    if n % c == 0:
        contador += 1

if contador != 2:
    print(f"{n} não é primo")
elif contador == 2:
    print(f"{n} é primo")
