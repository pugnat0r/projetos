# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.


valores = []

while True:
    escolha = ""

    valores.append(int(input("Digite um valor: ")))

    while escolha == "" or escolha not in "SsNn":
        escolha = str(input(f"Quer continuiar? [S/N]: "))

    if escolha in "Nn":
        break

valores.sort(reverse=True)

print('=-'*30)
print(f"A quantidade de números digitados:   {len(valores)}")
print('')
print(f"A lista Ordenada Decrescente:   {valores}")
print('')

for ind, val in enumerate(valores):
    if val == 5:
        print(f"O número 5 foi digitado e está na posição  {ind}")
if 5 not in valores:
    print('O número 5 não foi digitado....')

print("")
