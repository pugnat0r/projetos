class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe...")

    def falar(self):
        print(f"Au Au Au...")


def criar_cachorro():  # Criando uma função para instanciar a classe

    c = Cachorro("Mia", "Branca", True)  # Instanciando a classe Cachorro

    print(c.nome)  # Acessando os atributos da classe


c = Cachorro("Pandora", "Preta", False)  # Instanciando a classe Cachorro

c.falar()  # Chamando o método falar da classe Cachorro


del c  # Deletando a instância da classe Cachorro
print("Hello World")
