# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

fator = int(input("\nDigite um número para calcular o seu fatorial: "))

print("")
print(f"O fatorial do número\n{fator}! = {fator} x ", end="")

if fator != 0:
    resultado = fator * (fator - 1)
    fator -= 1

while fator > 0:

    print(f"{fator}", end="")

    fator -= 1

    if fator != 0:
        resultado = resultado * fator

    if fator >= 1:
        print(" x ", end="")


print(f" = {resultado}")
