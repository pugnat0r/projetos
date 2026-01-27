# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

from ctypes.wintypes import PINT


valores = []
valores_pares = []
valores_impares = []

while True:

    valores.append(int(input(f"Digite um valor: ")))

    escolha = ""
    while escolha == "" or escolha not in "SN":
        escolha = str(input("Quer continuar? [S/N]: ")).upper()[0]

    if escolha in "N":
        break

for valor in valores:
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)


print(f"Lista completa: {valores}")
print(f"Lista valores pares: {valores_pares}")
print(f"Lista valores ímpares {valores_impares}")
