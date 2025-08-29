from random import randint
from time import sleep

pontos = 0
jogadas = 0
while pontos <= 10:

        number = 1,2,3,4,5
        certa = randint(1, 5)

        print('Você acertou:',pontos,'vezes, e já jogou',jogadas,'vezes')
        entrada = int(input('Diga um Number entre 1 e 5!!! Tente a Sorte!!!!\n'))

        print('PROCESSANDO...')
        sleep(3)

        print('certa', certa)

        if entrada == certa and certa <= 5:
                print('ACERTOUUUUUUUUUUUUUUUUUUUUUUUUUU')
                pontos = pontos + 1
                jogadas = jogadas + 1
        else:
                print('ERROUUUUUUUUUUUUUUUUUUUUUUUUUUUU')
        print('.')
        print('.')
        print('.')
        print('.')
        print('.')
        print('.')
        print('.')
        print('.')
        print('.')
        print('.')
        print('.')
        print('.')
        jogadas = jogadas + 1
