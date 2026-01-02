# Pergunte um número e calcule a sequência de fibonacci


print("-------------[Sequência de Fibonacci]-------------")

n = int(input("\nQuantos termos deseja ver?: "))

controlador = 0

fibonacci = [0, 1,]


while controlador < n:

    if controlador >= 2:

        ultimo = fibonacci[-1]
        penultimo = fibonacci[-2]

        fibonacci.append(ultimo+penultimo)

    print(
        f"\nVALOR DA POSIÇÃO NA LIST [{controlador}] - n°{controlador+1} = {fibonacci[controlador]}")

    controlador += 1

print("\n")
