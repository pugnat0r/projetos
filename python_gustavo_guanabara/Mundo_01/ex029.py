vel = int(input('Qual a sua velocidade?'))

if vel <= 80:
    print('Você está dentro do limite de velocidade!!!!')
    print('Parabéns!!')
else:
    multa = (vel - 80)*7
    print('Você está acima do limete de velocidade!!!!!')
    print('Sua multa é no valor de R$ {:.2f} REAIS'.format(multa))