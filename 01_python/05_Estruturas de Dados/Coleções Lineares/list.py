texto = input("Diga algo: ").strip()

separando_em_listas = list(texto)

print(separando_em_listas)


carros = ["Lancer", "ASX"]

for nome_do_objeto in carros:
    print(nome_do_objeto)


for indice, carro in enumerate(carros):
    print(f"{indice}:{carro}")


lista = []

lista.append(1)
lista.append("Vitim lindo")
lista.append([40, 30, 20])

print(lista)

lista.clear()

print(lista)
