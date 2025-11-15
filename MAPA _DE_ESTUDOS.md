
watchmedo auto-restart -d . -p "*.py" -- python main.py


01 - Programação Orientada a Objetos ( POO )
02 - Conceitos de Herança
03 - Encapsulamento
04 - Polimorfismo
05 - Interfaces e Classes Abstratas
06 - Projeto, Sistema Báncario em POO

07 - Decoradores, Iteradores e Geradores
08 - Lidando com Datas, Hora e Fuso Horário
09 - Manipulando Arquivos
10 - Gerenciamento de Pacotes, Convenções e Boas práticas

11 - Banco de Dados
12 - Banco de dados Relacionais (SQL)
13 - MongoDB e Banco de Dados NoSQL
14 - Explorando Banco de Dados Relacionais com Python DB API
15 - Aplicações REST
16 - API com FastAPI, Python e DOCKER
17 - API com FastAPI, Utilizando TDD    


31/08/2025 

- Manipulando arquvios

    file = open("EXAMPLE.txt", "r")
    # fazemos algo com o arquivo.
    file.close()

    Modos de abertura [ 
        "r" -> Leitura
        "w" -> Gravação
        "a" -> Anexar
    ]

- Métodos 
    read() - Retorna todo arquivo como string
    readline() - Retorna uma linha por vez
    readlines() - Retorna todas as linha como lista


    write() - Escreve uma str
    writelines() - Escreve uma lista


- Bibliotecas para usar comandos terminal no python, 
    Import OS
    import shutil

- Bibliotecas para achar a pasta pai do seu arquivo de forma dinâmica
    from pathlib import Path
    
    ROOT_PATH = Path(__file__).parent

    os.mkdir(ROOT_PATH / "nome_da_pasta")








node js 


parei em 11 minutos : https://www.youtube.com/watch?v=hHM-hr9q4mo&t=288s

