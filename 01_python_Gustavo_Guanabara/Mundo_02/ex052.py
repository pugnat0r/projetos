
n = int(input("Digite um número: "))

contador = 0

print("\n")

for c in range(1, n + 1):
    if n % c == 0:
        print(f"\033[32m{c} ", end=" ")
        contador += 1
    else:
        print(f"\033[31m{c} ", end=" ")


if contador == 2:
    print(f"\033[0m\n\n{n} é primo, foi divisível {contador} vezes\n")
else:
    print(f"\033[0m\n\n{n} não é primo, foi divisível {contador} vezes\n")
