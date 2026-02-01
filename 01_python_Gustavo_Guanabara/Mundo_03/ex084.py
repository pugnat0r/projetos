# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves

pessoas = list()
pessoa = list()
pesadas = leves = 0


while True:
    pessoa.append(str(input("Nome: ").capitalize()))
    pessoa.append(int(input("Peso: ")))

    if pessoa[1] > pesadas:
        pesadas = pessoa[1]
    if pessoa[1] < leves or leves == 0:
        leves = pessoa[1]

    pessoas.append(pessoa[:])
    pessoa.clear()

    escolhas = ""
    while escolhas == "" or escolhas not in "SN":
        escolhas = str(input("Quer continuar? [S/N]: ")[0].upper())

    if escolhas in "N":
        break

print(f"Ao todo, você cadastrou {len(pessoas)} pessoas.")

print(f"O maior peso foi de {pesadas}Kg. Peso de ", end="")
for pesos in pessoas:
    if pesos[1] == pesadas:
        print(f"[{pesos[0]}] ", end="")
print()

print(f"O menor peso foi de {leves}Kg. Peso de ", end="")
for pesos in pessoas:
    if pesos[1] == leves:
        print(f"[{pesos[0]}] ", end="")
print()
