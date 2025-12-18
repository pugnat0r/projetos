# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

pesada = 0
leve = 0

for c in range(1, 6):
    n = int(input(f"Digite o peso da {c}° pessoa em kg: "))

    if n > pesada or pesada == 0:
        pesada = n

    if n < leve or leve == 0:
        leve = n

print(f"A pessoa mais pesada pesa {pesada}kg")
print(f"A pessoa mais leve pesa {leve}kg")
