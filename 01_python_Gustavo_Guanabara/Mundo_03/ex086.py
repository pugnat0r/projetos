# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado!
# No final, mostre a matriz na tela. com a formatação correta.


matriz = [], [], []
linha = list()

for c in range(0, 3):

    for l in range(0, 3):

        valor = int(input(f"Digite um valor para [{c}, {l}]: "))
        linha.append(valor)

    for unidade in linha:

        matriz[c].append(unidade)

    linha.clear()


print("-=" * 30)
print(f"{"Matriz":_^60}")

for unidade in matriz:

    print(" "*20+f"[ {unidade[0]} ]  [ {unidade[1]} ]  [ {unidade[2]} ]")

print("-=" * 30)
