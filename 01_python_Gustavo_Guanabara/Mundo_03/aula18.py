galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(str(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

print(galera)


galera1 = [["Pedro", 25], ["Maria", 19], ["João", 32]]

for pessoa in galera1:
    print(f"{pessoa[0]} tem {pessoa[1]} anos de idade.")
