# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

maior_18 = homens = mulheres_menor_20 = 0

while True:

    print("~"*40)
    print("Cadastre uma Pessoa")
    print("~"*40)

    idade = int(input("Idade:  "))

    type_sex = str(input("Qual é seu sexo? [F/M]  ")).strip()
    while type_sex == "" or type_sex[0] not in "FfMm":
        type_sex = str(input("Qual é seu sexo? [F/M]  ")).strip()

    print("~"*40)

    new_cadastro = str(
        input("Quer cadastrar mais uma pessoa? [S/N] ")).strip()
    while new_cadastro == "" or new_cadastro[0] not in "SsNn":
        new_cadastro = str(
            input("Quer cadastrar mais uma pessoa? [S/N] ")).strip()

    if idade > 18:
        maior_18 += 1

    if type_sex in "Mm":
        homens += 1

    if type_sex in "Ff":
        if idade < 20:
            mulheres_menor_20 += 1

    if new_cadastro in "Nn":
        break

print("~"*40)
print(f"\nQuantidade de Pessoas maiores de 18 anos: {maior_18}")
print(f"\nQuantidade de Homens cadastrados: {homens}")
print(f"\nQuantidade de Mulheres menores de 20 anos: {mulheres_menor_20}")
print("\n")
print("~"*40)
