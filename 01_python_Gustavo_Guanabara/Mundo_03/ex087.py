# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [ [], [], [] ]
PAR = 0
Terceira_Coluna = 0
Maior_Segunda_Linha = 0

for coluna in range(0, 3):
    for linha in range(0, 3):

        matriz[coluna].append(int(input(f"Digite um valor para {coluna}, {linha}: ")))

print("-="*30)


cont = 0
for unidade in matriz:
    print(" "*20+f"[ {unidade[0]} ]  [ {unidade[1]} ]  [ {unidade[2]} ]")

    cont += 1

    if unidade % 2 == 0:
        PAR += unidade

    Terceira_Coluna += unidade[2]
    
    if cont == 2:
        if 
    
print("-="*30)
