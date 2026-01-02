# Crie um prograama que leia vários números inteiros pelo teclado.
# No final, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contador = soma = maior = menor = 0

# contador = 0
# soma = 0

# maior = 0
# menor = 0

while True:

    escolha = int(input("\nDigite um número: "))

    soma += escolha
    contador += 1

    if escolha > maior:
        maior = escolha

    if escolha < menor or menor == 0:
        menor = escolha

    continuar = input("\nQuer continuar? [S/N]: ")

    if continuar in "Nn":
        break  
    elif continuar in "Ss":
        continue
    else:
        print("Opção inválida! Encerrando o programa.")
        break

print(f"\nQuantidade de números digitados: {contador}")
print(f"\nMedia: {soma / contador}")
print(f"\nMaior valor: {maior}")
print(f"\nMenor valor: {menor}")
