nome = str(input('Qual é o seu nome completo? ')).strip()
# strip tira os espaços

listas = nome.split()
# split transforma o nome em uma lista, por palavras
juntas = ''.join(listas)
# join junta tudo, faz uma concatenação

print(nome.upper())
print(nome.lower())

print('Seu nome tem um total de {} letras!'.format(len(juntas)))

# Len é para ler a quantidade de letras que tem em uma palavra

print('Seu primeiro nome tem um total de {} letras!'.format(len(listas[0])))
