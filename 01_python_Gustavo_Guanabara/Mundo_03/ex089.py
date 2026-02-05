# Crie um programa  que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
from time import sleep
from click import clear

alunos = list()
temp = list()

posição = 0

while True:

    escolha = ""
    media = 0

    temp.append(str(input("Nome: ")))
    alunos.append(temp[:])
    temp.clear()

    for i in range(0, 2):
        temp.append(float(input(f"Nota {i+1}: ")))
        media += temp[i]

    alunos[posição].append(temp[:])
    alunos[posição].append(media/2)

    while escolha == "" or escolha not in "SN":
        escolha = str(input("Quer continuar? [S/N]: ")).upper()

    if escolha == "N":
        break

    temp.clear()
    posição += 1

while True:
    clear()
    print("-="*20)
    print("No. NOME                 MÉDIA")
    print("_"*40)

    for ind, aluno in enumerate(alunos):
        print(f"{ind+1}" + f"   {aluno[0]:<8}{aluno[2]:>18.1f}")

    print("_"*40)

    escolha = int(input("Mostrar notas de qual aluno? (0 Interrompe): "))

    if escolha == 0:
        print("-="*20)
        print("Finalizando o programa! Obrigado por usar!")
        print("-="*20)
        sleep(2)
        print(".")
        print(".")
        print(".")
        sleep(3)
        print("Todos os direitos reservados: Pugnat0r (copyright)")
        break

    for ind, aluno in enumerate(alunos):
        if ind == escolha-1:
            print("_"*40)
            print(f"{f'Notas de {aluno[0]}':^40}")
            print("-"*40)

            print()
            for ind, nota in enumerate(aluno[1]):
                print(f"{ind+1}° Bimestre: {nota}")
            print()

    escolha = " "
    while escolha not in "S/N":
        escolha = str(input("Quer ver nota de outro aluno? [S/N]: ")).upper()

    if escolha in "N":
        print("-="*20)
        print("Finalizando o programa! Obrigado por usar!")
        print("-="*20)
        sleep(2)
        print(".")
        print(".")
        print(".")
        sleep(3)
        print("Todos os direitos reservados: Pugnat0r (copyright)")
        break
