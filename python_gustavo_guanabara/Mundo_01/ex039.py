# Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento.

from datetime import date

spawn = int(input('Entre com a data de nascimento: '))
year = date.today().year - spawn

print('')
print(' [ 1 ] - Masculino')
print('')
print(' [ 2 ] - Feminino')
print('')
sex = int(input('Qual é o seu sexo ? '))
print('')

if sex == 1:
    if year < 18:
        print('Você ainda vai se alistar ao serviço militar!')
        print('Você vai se alistar no ano: {} '.format((18-year) + date.today().year))
        print('Falta {} anos!'.format(18 - year))
        print('Você tem {} anos'.format(year))

    elif year == 18:
        print('Você está na hora de se alistar ao serviço militar!')
        print('Você tem {} anos'.format(year))

    else:
        print('Você já passou do tempo do alistamento.')
        print('Você tem {} anos ou vai fazer esse ano!'.format(year))
        print(f'Você deveria ter se alistado há {year-18} anos!!!')

elif sex == 2:
    print('O alistamento NÃO É OBRIGATÓRIO para mulheres!! ')

else:
    print('Comando não encontrado! Sua escolha está crazy.')