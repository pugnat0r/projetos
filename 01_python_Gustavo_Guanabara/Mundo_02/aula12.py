nome = str(input('Qual é o seu nome? ')).capitalize()


if nome == 'Gustavo':
    print('Que nome maravilhosooo')

elif nome == 'Pedro' or nome == 'Vitor' or nome == 'Marcos':
    print('Seu nome é bem popular no Brasil.')

elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')

else:
    print('Seu nome é bem normal!')


print('Tenha um bom dia, {}!'.format(nome))
