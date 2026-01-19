números = []
maior = []
menor = []

for c in range(0, 5):
    números.append(int(input(f"Digite um valor para a Posição {c}: ")))

maior = [max(números)]
menor = [min(números)]

for indice, valor in enumerate(números):
    if valor == maior[0]:
        maior.append(indice)

    if valor == menor[0]:
        menor.append(indice)

print('=-'*30)


print(f"Você digitou os valores ", end="")
print("[ ", end="")
for i in números:
    if i == maior[0]:
        print(f"\033[0;32;40m{i}\033[0;30;40m, ", end="")
    elif i == menor[0]:
        print(f"\033[0;31;040m{i}\033[0;30;40m, ", end="")
    else:
        print(f"{i}, ", end="")

print("]")

print(
    f"O \033[0;32;40mmaior\033[0;30;40m valor digitado foi \033[0;32;40m{maior[0]}\033[0;30;40m nas posições ", end="")
for i in maior[1:]:
    print(f"{i}... ", end="")
print("")

print(
    f"O \033[0;31;040mmenor\033[0;30;40m valor digitado foi \033[0;31;040m{menor[0]}\033[0;30;40m nas posições ", end="")
for i in menor[1:]:
    print(f"{i}... ", end="")
print("")
print('')
