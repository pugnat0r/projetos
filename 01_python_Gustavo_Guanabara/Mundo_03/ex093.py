# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depous vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o compeonato.

player = {}
gols = list()
player['Nome'] = str(input("Nome do jogador: ")).capitalize()
jogos = int(input(f"Quantas partidas {player['Nome']} jogou? "))

for i in range(0, jogos):

    gol = int(input(f"Quantos gols na partida {i}? "))
    gols.append(gol)

player['Gols'] = gols

player['Total'] = 0

for gol in gols:
    player['Total'] += gol

print("-="*30)
print(player)
print("-="*30)
print(f"O campo nome tem o valor: {player['Nome']}.")
print(f"O campo gols tem o valor: {player['Gols']}.")
print(f"O campo total tem o valor: {player['Total']}.")
print("-="*30)

print(f"O jogador {player['Nome']} jogou {jogos} partidas!")

for pos, gol in enumerate(player['Gols']):
    print(f"    => Na partida {pos}, fez {gol} gols.")

print(f"Foi um total de {player['Total']} gols.")
