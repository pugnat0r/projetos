# O programa vai perguntar o valor da casa, o sálario do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do sálario ou então o empréstimo será negado.

casaValor = float(input('Qual o valor da casa? '))

salarioValor = float(input('Qual o seu sálario? '))

anos = float(input('Em quantos anos você deseja pagar? '))


limit = salarioValor*0.30
parcela = (casaValor/anos)/12


if (parcela <= limit):
    print('Você está dentro do valor aceitável')
    print('')
    print('Você foi aprovado!!!!')
    print('')
    print('Sua parcela mensal ficou R$ {:.2f}'.format(parcela))
    print('')


else:
    print('')
    print('Você não foi aprovado!!!!!')
    print('')
    print('Sua parcela mensal ficaria R$ {:.2f}'.format(parcela))
    print('')
    print('Você consegue financiar apenas valores abaixo de R$ {:.2f}'.format(limit))
    print('')
