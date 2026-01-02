# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

soma = contador = 0

while True:
    numbers = int(input("Digite um número inteiro [999 para parar]: "))

    if numbers == 999:
        break
    soma += numbers
    contador += 1

print(f"\n A soma de todos os números foi: {soma}\n")
print(f" Você digitou {contador} números!\n")
