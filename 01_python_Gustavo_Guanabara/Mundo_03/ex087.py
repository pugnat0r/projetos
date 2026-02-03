# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.


from click import pause


matriz = [[], [], []]
Soma_Pares = 0
Soma_Terceira_Coluna = 0
Maior_Segunda_Linha = 0

for coluna in range(0, 3):
    for unidade in range(0, 3):

        matriz[coluna].append(
            int(input(f"Digite um valor para {coluna}, {unidade}: ")))

print("-="*30)
for pos, coluna in enumerate(matriz):
    print(coluna)
    pause()
    print(f"{" ":<15}" +
          f"[ {coluna[0]:^5}] [ {coluna[1]:^5} ] [ {coluna[2]:^5} ]")

    for unidade in coluna:
        if unidade % 2 == 0:
            Soma_Pares += unidade

        if pos == 1:
            if unidade > Maior_Segunda_Linha:
                Maior_Segunda_Linha = unidade

    # Soma dos números da terceira coluna
    Soma_Terceira_Coluna += coluna[2]

print("-="*30)

print(f"A soma dos valores pares é: {Soma_Pares}")
print(f"A soma dos valroes da terceira coluna é: {Soma_Terceira_Coluna}")
print(f"O maior valor da segunda linha é: {Maior_Segunda_Linha}")
