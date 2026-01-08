# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = soma = 0

while True:

    números = int(input("[ 999 ] Para Sair - Digite um número: "))

    if números == 999:
        break

    soma += números
    cont += 1

print(f"A soma de todos os números: {soma}")
print(f"Foi digitados {cont} números no total!")
