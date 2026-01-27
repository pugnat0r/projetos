RESET = '\033[0m'
VERDE = '\033[32m'
VERMELHO = '\033[31m'

numeros = []
maior = []
menor = []

for c in range(0, 5):
    numeros.append(int(input(f"Digite um valor para a Posição {c}: ")))

maior = [max(numeros)]
menor = [min(numeros)]

for indice, valor in enumerate(numeros):
    if valor == maior[0]:
        maior.append(indice)
    if valor == menor[0]:
        menor.append(indice)

print('=-'*30)

print("Você digitou os valores [ ", end="")
for i in numeros:
    if i == maior[0]:
        print(f"{VERDE}{i}{RESET}, ", end="")
    elif i == menor[0]:
        print(f"{VERMELHO}{i}{RESET}, ", end="")
    else:
        print(f"{i}, ", end="")
print("]")

print(
    f"O {VERDE}maior{RESET} valor digitado foi {VERDE}{maior[0]}{RESET} nas posições ", end="")
for i in maior[1:]:
    print(f"{i}... ", end="")
print()

print(
    f"O {VERMELHO}menor{RESET} valor digitado foi {VERMELHO}{menor[0]}{RESET} nas posições ", end="")
for i in menor[1:]:
    print(f"{i}... ", end="")
print()
