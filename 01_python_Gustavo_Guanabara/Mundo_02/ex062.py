# Melhore o desafio 61 perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos

from time import sleep


t = int(input("Digite o primeiro termo: "))
r = int(input("Digite a Razão "))

resultado = t
controlador = 1
passo = 10

print("")

while controlador <= passo:

    print(f"\na{controlador}: = {resultado}")

    resultado += r
    controlador += 1

    if controlador > passo:
        mais = int(input("\nDeseja mostrar mais termos?: "))

        passo += mais

        if mais == 0:
            print("\nFinalizando programa! ")
            sleep(2)
            break
