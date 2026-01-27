# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


valores = []

while True:

    escolhas = ""

    print("=-"*30)
    valor = int(input("Digite um valor: "))

    if valor not in valores:
        print("=-"*30)
        print("Valor adicionado com sucesso...")
        print("=-"*30)
        valores.append(valor)
        valores.sort()
    else:
        print("Valor duplicado! Não vou adicionar...")

    while escolhas == "" or escolhas[0] not in "NnSs":
        escolhas = str(input("Quer continuar? [S/N]: "))

    if escolhas in "Nn":
        break

print("=-"*30)
print(f"Sua lista de valores: {valores}")
