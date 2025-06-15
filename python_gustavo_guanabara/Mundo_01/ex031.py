km = int(input('Qual a distancia da sua viagem? '))

if km <= 200:
    preço = km*0.50
    print('R$ 0.50 Por cada km')
    print('Sua passagem é: R$',preço)
else:
    preço = km*0.45
    print('R$ 0.45 por cada km')
    print('Sua passagem é: R$',preço)
