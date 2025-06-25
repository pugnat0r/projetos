# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# 1 para binário
# 2 para octal
# 3 para hexadecimal

from pyinterconvert import ConvClient
c = ConvClient()

num = int(input('Diga um número inteiro: '))

print('Você quer converter para qual sistema? ')
print('')

print('[ 1 ] para binário')
print('')

print('[ 2 ] para Octal')
print('')

print('[ 3 ] para Hexadecimal')
print('')

escolhas = int(input('Escolha uma das opções: '))


if escolhas == 1:
    print('')
    print('Sua escolha foi [ 1 ] Binário')
    print('')
    print('Seu número convertido em BI: {}'.format(c.DecToBin(num)))
    print('')

elif escolhas == 2:
    print('')
    print('Sua escolha foi [ 2 ] octal')
    print('')
    print('Seu número convertido em Octal: {}'.format(c.DecToOct(num)))
    print('')

elif escolhas == 3:
    print('')
    print('Sua escolha foi [ 3 ] Hexa')
    print('')
    print('Seu número convertido em Hexa: {}'.format(c.DecToHex(num)))
    print('')

else:
    print('Escolha não encontrada!')
