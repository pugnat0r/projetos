# Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas.
# No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos.


pessoas = []
somar_da_idades = 0
olderest = ""
media_idade = 0
contador = 3000
mulheres_menos_de_20 = 0

for c in range(1, 5):

    print(f"----- {c}° PESSOA -----")

    user = str(input("Nome: ")).strip()
    born_date = int(input("Ano de nascimento: "))
    print(f"{2025 - born_date} anos")
    sex = str(input("Sex: ")).strip()

    pessoas.append(
        {"nome": user, "born_date": born_date, "sex": sex, }
    )


for c in range(0, 4):

    somar_da_idades += 2025 - pessoas[c]["born_date"]

    if pessoas[c]["born_date"] < contador and pessoas[c]["sex"].lower() == "m":
        contador = pessoas[c]["born_date"]
        olderest = pessoas[c]["nome"]

    if pessoas[c]["sex"].lower() == "f" and (2025 - pessoas[c]["born_date"]) < 20:
        mulheres_menos_de_20 += 1

print("A média de idade do grupo é {:.1f} anos.".format(somar_da_idades / 4))

print(f"O homem mais velho é {olderest}")

print(
    f"Tem um total de {mulheres_menos_de_20} mulheres com menos de 20 anos de idade.")
