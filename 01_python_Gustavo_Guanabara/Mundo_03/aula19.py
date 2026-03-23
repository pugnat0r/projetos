# pessoas = {'nome': 'vitor', 'sexo': 'M', 'idade': 24}

# pessoa1 = {'nome': 'vitor', 'sexo': 'M', 'idade': 24}
# pessoa2 = {'nome': 'Echiley', 'sexo': 'F', 'idade': 22}
# duo = []
# duo.append(pessoa1)
# duo.append(pessoa2)
# print(duo[0]['sexo'])


# print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")

# print(pessoas.keys())
# print(pessoas.items())
# print(pessoas)

# del pessoas['sexo']
# pessoas['nome'] = 'Antoneta'
# pessoas['peso'] = 100

# for k in pessoas.keys():
#     print(k)

# for v in pessoas.values():
#     print(v)

# for k, v in pessoas.items():
#     print(f"{k} = {v}")

from click import clear


brasil = list()
estado = dict()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).capitalize()
    estado['sigla'] = str(input('Sigla: ')).upper()
    brasil.append(estado.copy())

clear()
for e in brasil:
    for v in e.values():
        print(v, end=" ")
    print()
