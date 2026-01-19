num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(4) if 4 in num else print("O valor 4 não foi encontrado na lista.")

print(num)
print(f"Essa lista tem {len(num)} elementos.")

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f"{v}...")


for c in range(0, 5):
    valores.append(int(input('Digite um número: ')))

print("separação entre for's")
for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}")
print("fim da lista")


a = [2, 3, 4, 7]
b = a  # Essa linha vai fazer uma ligação entre as listas
b = a[:]  # Essa linha vai criar uma copia com os elementos da lista A

b[2] = 8  # Essa alteração n vai mudar na lista mãe

print(a)
print(b)
