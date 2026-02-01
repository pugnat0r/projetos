# Refazendo exercício com outra solulção:

matriz = [[], [], []]

for c in range(0, 3):
    for l in range(0, 3):
     
        matriz[c].append(int(input(f"Digite um valor para {c}, {l}: ")))

print("-="*30)

for unidade in matriz:

    print(" "*20+f"[ {unidade[0]} ] [ {unidade[1]} ] [ {unidade[2]} ]")

print("-="*30)
