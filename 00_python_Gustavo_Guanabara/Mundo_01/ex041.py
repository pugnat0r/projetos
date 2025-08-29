# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date

year = int(input('Qual ano você nasceu? '))
age = date.today().year - year

print(f'Você tem {age} anos')

if age <= 9:
    print('Sua categoria é: MIRIM')

elif 14 >= age:
    # age >= 9 and age < 14:
    print('Sua categoria é: INFANTIL')

elif 19 >= age:
    # age >= 14 and age < 19:
    print('Sua categoria é JUNIOR')

elif 20 >= age:
    # age >= 19 and age < 20:
    print('Sua categoria é SÊNIOR')

else:
    print('Sua categoria é MASTER')
