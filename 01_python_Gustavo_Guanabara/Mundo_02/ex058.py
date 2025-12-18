# Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from time import sleep
import random

escolha_da_maquina = random.randint(0, 10)
tentativas = 0

print("Estou pensando...")
sleep(4)
print("...em um número entre 0 e 10.")
sleep(2)
print("Será que você consegue adivinhar qual é?")

while True:

    palpites = int(input("\nDigite seu palpite: "))
    tentativas += 1

    if palpites == escolha_da_maquina:
        print(
            f"\nParabens você acertou o número {escolha_da_maquina} com {tentativas} tentativas!")
        break
    else:
        print("\nNúmero incorreto. Tente novamente!")

    if palpites < escolha_da_maquina:
        print("\nO número é maior.")
    else:
        print("\nO número é menor.")
