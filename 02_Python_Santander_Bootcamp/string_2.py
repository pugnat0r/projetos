nome = "Vitor"
idade = 23
profissao = "programador"
linguagem = "Python"

dados = {"nome": "Vitor", "idade": 23}
saldo = 45.435

print("Meu nome é: %s e minha idade é: %d" % (nome, idade))

print("Meu nome é: {} e minha idade é: {}".format(nome, idade))
print("Meu nome é: {0} e minha idade é: {1}".format(nome, idade))

print("Meu nome é: {nome} e minha idade é: {idade}".format(
    nome=nome, idade=idade))
print("Meu nome é: {name} e minha idade é: {age}".format(name=nome, age=idade))
print("Meu nome é: {nome} e minha idade é: {idade}".format(**dados))

print(f"Meu nome é: {nome} e minha idade é: {idade}")
print(f"Meu nome é: {nome} e minha idade é: {idade} Saldo: {saldo:.2f}")
print(f"meu nome é: {nome} e minha idade é: {idade} Saldo {saldo:10.1f}")
