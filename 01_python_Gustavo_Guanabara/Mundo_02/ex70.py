# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

nome_mais_cheap = ""
preço = total_compra = one_thousands = mais_cheap = 0

while True:

    escolha = nome_produto = ""

    while nome_produto == "":
        print("~"*40)
        nome_produto = str(input("Qual o nome do produto?   "))

    preço = int(input("Qual o valor?   "))

    while escolha == "" or escolha[0] not in "SsNn":
        escolha = str(input("Quer continuar?  [S/N]"))

    total_compra += preço

    if preço >= 1000:
        one_thousands += 1

    if preço <= mais_cheap or mais_cheap == 0:
        mais_cheap = preço
        nome_mais_cheap = nome_produto

    if escolha in "Nn":
        break

print("~"*40)
print(f"O total da compra foi R$ {total_compra}")
print(f"Temos {one_thousands} custando mais de R$ 1000.00")
print(f"O produto mais barato foi {nome_mais_cheap} que custa {mais_cheap}")
print("~"*40)
