# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iquais

num1 = int(input('Entre com o 1° Número: '))
num2 = int(input('Entre com o 2° Número: '))

if num1 > num2:
    print('O primeiro valor é maior')
    print('{} é maior que {}'.format(num1, num2))

elif num1 < num2:
    print('O segundo valor é maior')
    print('{} é maior que {}'.format(num2, num1))

else:
    print('Não existe valor maior, os dois são iquais. ')
    print('{} é iqual {}'.format(num1, num2))
