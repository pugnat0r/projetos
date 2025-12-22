# Refaça o desafio 051, lendo o primeiro termo e a razão de um PA
# Mostrando os 10 primeiros termos da progressão usando a estrutura while

t = int(input("Digite o primeiro termo: "))
r = int(input("Digite a Razão "))

resultado = t
controlador = 1

while controlador < 11:

    print(f"a{controlador}: = {resultado}")

    resultado += r
    controlador += 1
