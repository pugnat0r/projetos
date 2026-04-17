
import time
from click import clear, pause

# Lista onde vai armazenar os jogadores, cada jogador é um dicionário com nome, quantidade de jogos, gols e total de gols.
jogadores = list()

while True:

    # Escolhas para continuar ou não o programa, caso o usuário digite algo diferente de S ou N, ele vai pedir para digitar novamente.
    escolhas = ""

    # Dicionário para armazenar os dados do jogador, onde o nome é a chave "nome", a quantidade de jogos é a chave "jogos", a quantidade de gols em cada partida é a chave "gols" e o total de gols é a chave "total".
    player = dict()
    player["nome"] = str(input("Nome do jogador: ")).capitalize()
    player["jogos"] = int(input(f"Quantas partidas {player['nome']} jogou? "))
    player["total"] = int(0)

    # Lista para armazenar a quantidade de gols em cada partida, onde cada posição da lista corresponde a uma partida e o valor é a quantidade de gols nessa partida.
    gols = list()
    # Loop para pedir a quantidade de gols em cada partida, onde o número da partida é dado pelo loop e a quantidade de gols é armazenada na lista "gols" e somada ao total de gols do jogador.
    for partida in range(0, player["jogos"]):

        gol = int(input(f"Quantos gols na partida {partida}: "))
        gols.append(gol)
        player["total"] += gol

    player["gols"] = gols

    # Adiciona o dicionário do jogador na lista de jogadores.
    jogadores.append(player)

    # Loop para pedir ao usuário se ele quer continuar ou não, onde a resposta deve ser S ou N, caso contrário, ele vai pedir para digitar novamente.
    while escolhas == "" or escolhas not in "SN":

        escolhas = str(input("Quer continuar? [S/N]: "))[0].capitalize()

    # Se o usuário escolher N, o loop principal é interrompido e o programa segue para a parte de consultas.
    if escolhas in "N":
        escolhas = ""
        break

# Loop para mostrar a tabela de jogadores, onde cada jogador é mostrado com seu código (posição na lista), nome, quantidade de gols em cada partida e total de gols.
while True:
    print()
    pause("Aperta qualquer tecla para continuar consultas.")
    clear()
    print()
    print("-="*25)
    print("cod     nome                gols           total")
    print("-="*25)
    
    # Loop para mostrar a tabela de jogadores, onde cada jogador é mostrado com seu código (posição na lista), nome, quantidade de gols em cada partida e total de gols.
    for cod, jogador in enumerate(jogadores):
        print(
            f" {cod:<7}{jogador["nome"]:<20}{str(jogador["gols"]):<17}{jogador["total"]}")
    print("-="*25)

    # Variável para armazenar o tamanho da lista de jogadores, onde o tamanho é dado pelo número de jogadores na lista menos um, para que o código do jogador seja válido.
    tamanho = len(jogadores)-1

    print()
    print("-="*25)

    # Loop para pedir ao usuário o código do jogador que ele quer ver os dados, onde o código deve ser um número inteiro e deve ser válido, caso contrário, ele vai pedir para digitar novamente.
    try:
        escolhas = int(input("Mostrar dados de qual jogador? COD: "))
    except ValueError:
        continue
    print()

    if escolhas == 999:

        clear()
        print("FINALIZANDO PROGRAMA")
        print("FINALIZANDO PROGRAMA")
        time.sleep(2)

        break
    # Se o código do jogador for inválido, ou seja, menor que 0 ou maior que o tamanho da lista de jogadores, ele vai mostrar uma mensagem de erro e pedir para digitar novamente.
    elif escolhas < 0 or escolhas > tamanho:
        print()
        print(
            f"ERRO! Não existe jogador com o código {escolhas}! Tente novamente")

    else:
        print()
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[escolhas]["nome"]}')

        print()
        for jogo, gol in enumerate(jogadores[escolhas]["gols"]):
            print(
                f"   {jogo+1}° partida {jogadores[escolhas]["nome"]} fez {gol} gols!")
