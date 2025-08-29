dia = float(input('Quantos dias? '))
km = float(input('Quantos km rodados? '))

print('Você deve pagar R${:.2f}'.format(dia*60+km*0.15))
