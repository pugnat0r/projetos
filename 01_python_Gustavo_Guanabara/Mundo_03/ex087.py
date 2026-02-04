# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.


matriz = [[], [], []]
Soma_Pares = Soma_Terceira_Coluna = Maior_Segunda_Linha = 0

for linha in range(0, 3):
    for unidade in range(0, 3):

        matriz[linha].append(
            int(input(f"Digite um valor para {linha}, {unidade}: ")))

print("-="*30)
for pos, linha in enumerate(matriz):
  
    print(f'{" ":<15}[ {linha[0]:^5}] [ {linha[1]:^5} ] [ {linha[2]:^5} ]')

    for unidade in linha:

        # Soma dos números pares
        if unidade % 2 == 0:
            Soma_Pares += unidade

        # Maior valor da segunda linha
        if pos == 1:
            if unidade > Maior_Segunda_Linha:
                Maior_Segunda_Linha = unidade

    # Soma dos números da terceira coluna
    Soma_Terceira_Coluna += linha[2]

print("-="*30)

print(f"A soma dos valores pares é: {Soma_Pares}")
print(f"A soma dos valroes da terceira coluna é: {Soma_Terceira_Coluna}")
print(f"O maior valor da segunda linha é: {Maior_Segunda_Linha}")
