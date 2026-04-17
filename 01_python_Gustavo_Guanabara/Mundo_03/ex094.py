# Crie um programa que leia nome, sexo, e idade de várias pessoas.
# Guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A - Quantas pesoas foram cadastradas
# B - A média de idade do grupo
# C - Uma lista com todas as mulheres
# D - Uma lista com todas as pessoas com idade acima da média.

pessoas = list()
media = 0
allwoman = list()
oldperson = list()


while True:

    escolhas = ""

    p = dict()
    p["nome"] = str(input("Nome: "))

    while escolhas == "" or escolhas not in "MF":
        escolhas = str(input("Sexo: [M/F] "))[0].upper()
        p["sexo"] = escolhas

        if escolhas not in "MF":
            print("ERRO! Por favor, digite apenas M ou F.")

    p["idade"] = int(input("Idade: "))

    pessoas.append(p)

    escolhas = ""

    while escolhas == "" or escolhas not in "SN":

        escolhas = str(input("Quer continuar? [S/N] ")).upper()

        if escolhas not in "SN":
            print("ERRO! Responda apenas S ou N.")

    if escolhas == "N":
        break


for temp_pessoas in pessoas:
    media += temp_pessoas["idade"]

    if temp_pessoas["sexo"] in "F":
        allwoman.append(temp_pessoas["nome"])

media = media / len(pessoas)

for temp_pessoas in pessoas:
    if temp_pessoas["idade"] > media:
        oldperson.append(
            f"Nome: {temp_pessoas["nome"]}, {temp_pessoas["idade"]} anos")

print(pessoas)
print("-="*30)
print(f"- O grupo tem {len(pessoas)} pessoas.")
print(f"- A média de idade é de {media} anos")
print("- As mulheres cadastradas foram: ", end="")
for mulheres in allwoman:
    print(f"{mulheres} -> ", end="")
print()
print(f"- Lista de pessoas que estão acima da média de idade:")
print(f"""
    {oldperson}
      """)
