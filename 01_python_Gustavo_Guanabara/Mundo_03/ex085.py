# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.


valores = [[], []]  # valores[0] = pares | valores[1] = impares

for i in range(0, 7):
    valor = int(input(f"Digite o {i+1}° valor: "))

    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()

print(f"Os valores pares digitados foram: {valores[0]}")
print(f"Os valores ímpares digitados foram: {valores[1]}")
