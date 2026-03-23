# Faça um programa que leia nome e média de um aluno, quardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

from click import clear


VERDE = "\033[0;32;40m"
VERMELHO = "\033[0;31;40m"
NORMAL = "\033[0;30;40m"

aluno = dict()

aluno['nome'] = str(input("Nome: ")).capitalize()
aluno['média'] = float(input("Média: "))

if aluno['média'] >= 7:
    aluno['situação'] = f"{VERDE}APROVADO{NORMAL}"
else:
    aluno['situação'] = f"{VERMELHO}REPROVADO!{NORMAL}"


clear()
print("-="*30)
print()
print(f"Nome do aluno: {aluno['nome']}")
print()
print(f"Sua média: {aluno['média']}")
print()
print(f"Sua situação: {aluno['situação']}")
print()
print("-="*30)
print()
