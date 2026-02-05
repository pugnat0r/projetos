# Crie um programa  que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = list()
temp = list()

posição = 0

while True:
    
    escolha = ""
    media = 0

    temp.append(str(input("Nome: "))) 
    alunos.append(temp[:])
    temp.clear()

    for i in range(0,2):
        temp.append(float(input(f"Nota {i+1}: ")))
        media += temp[i]    

    alunos[posição].append(temp[:])    
    alunos[posição].append(media/2)
    
    while escolha == "" or escolha not in "SN":
        escolha = str(input("Quer continuar? [S/N]: ")).upper()
        
    print(escolha)
    if escolha == "N":
        break
    
    temp.clear()
    posição += 1

print(alunos)

for i in range(0, 3):
    print(type(alunos[len(alunos)-1][i]))

    print(alunos[i])
