class hello_world:
    # Método construtor
    def __init__(self):
        self.nome = " "
    # Método de saudação

    def saudação(self):
        print(f"Olá, mundo! {self.nome}")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# Instanciando objetos da classe
Saudação_1 = hello_world()
Saudação_2 = hello_world()

# Atribuindo nomes aos objetos
Saudação_1.nome = "Alice"
Saudação_2.nome = "Echiley"

# Chamando o método de saudação
Saudação_1.saudação()
Saudação_2.saudação()

print(Saudação_1, Saudação_2)
