import datetime
from click import clear

Ano_atual = datetime.datetime.now().year

adultos = 0
jovens = 0

for c in range (1, 8):
    age = int(input(f"Digite o ano de nascimento da {c}° pessoa: "))
    idade = Ano_atual - age

    if idade >=18:
        adultos += 1
    elif idade <18:
        jovens += 1
    clear()


print(f"Total de pessoas maiores de idade: {adultos}")
print(f"Total de pessoas menores de idade: {jovens}")