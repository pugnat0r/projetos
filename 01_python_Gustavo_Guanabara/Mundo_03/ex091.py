# crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from operator import itemgetter
from random import randint
from time import sleep

jogadores = dict()
ranking = list()

for i in range(1, 5):

    jogadores[f"Jogador{i}"] = randint(1, 6)

print("Valores sorteados:")
for k, v in jogadores.items():
    print(f"    O {k} tirou {v}")
    sleep(1)

print("Ranking dos jogadores: ")
raking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(raking):
    print(f"    {i+1}° Lugar: {v[0]} com {v[1]}")
    sleep(1)
