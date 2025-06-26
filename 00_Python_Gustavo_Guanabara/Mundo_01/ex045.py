# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from winsound import PlaySound

jokenpô = ['Papel', 'Tesoura', 'Pedra']

maquina = random.choice(jokenpô)

player = str(input('Escolha: Papel, Tesoura, Pedra: ')).capitalize()

print(f'Jogada do Player: {player}')
print(f'Jogada da Maquina: {maquina}')

if (player == 'Pedra') and (maquina == 'Tesoura'):
    print('Player Win')

elif (player == 'Tesoura') and (maquina == 'Papel'):
    print('Player Win')

elif (player == 'Papel') and (maquina == 'Pedra'):
    print('Player Win')

elif (player == maquina):
    print('IMPATE!!!!')

else:
    print('MAQUINA WiN')


