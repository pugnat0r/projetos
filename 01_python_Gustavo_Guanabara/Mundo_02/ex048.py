# Faça um programa que calcule  a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

n = 0

for c in range(1, 501, 2):
    print(c)
    if c % 3 == 0:
        n += c
print(
    f'A soma de todos os números ímpares múltiplos de 3 entre 1 e 500 é {n}.')
