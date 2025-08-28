class Bicicleta:
    # Método construtor para inicializar os atributos da classe
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Biiiiiiiiiiiiiiii")

    def parar(self):
        print("A bicicleta parou")

    def correr(self):
        print("A bicicleta está correndo")

    # Para mostrar os dados e valores da classe podemos criar um método str
    # Dessa forma quando criarmos novos valores ou parametros não precisamos add manualmente.

    # Representação legível do objeto
    def __str__(self):
        # self.__class__.__name__ || Obtém o nome da classe
        # self.__dict__ || Obtém os atributos do objeto
        # self.__dict__.items() || Obtém os itens (chave-valor) do dicionário de atributos
        # f'{chave}={valor}' for chave, valor in self.__dict__.items() || List comprehension que transforma cada par em uma string
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# Instanciando um objeto da classe Bicicleta
b1 = Bicicleta("vermelho", "mountain bike", 2025, 5000)

# Chamando os métodos da classe
b1.parar()
b1.correr()
b1.buzinar()

# Mostrando os atributos da bicicleta
print(b1.cor, b1.ano)
