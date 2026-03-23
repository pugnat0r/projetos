# Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

player = {}

player['Nome'] = str(input("Nome: ")).capitalize()
player['Idade'] = date.today().year - int(input("Ano de Nascimento: "))
player['CTPS'] = int(input("Carteira de trabalho ( 0 não tem ): "))

while True:
    if player['CTPS'] == 0:
        break
    else:
        player['Contratação'] = int(input("Ano da contratação: "))
        player['Salário'] = float(input("Salário: R$ "))

    if date.today().year - player['Contratação'] >= 35:
        player['Aposentadoria'] = player['Idade']
        break
    else:
        player['Aposentadoria'] = (
            35 - (date.today().year - player['Contratação'])) + player['Idade']
        break

print("-="*30)
for k, v in player.items():
    print(f"  - {k} tem o valor {v}")
print()
