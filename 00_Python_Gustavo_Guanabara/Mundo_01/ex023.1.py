num = int(input('Diga um numero'))

print('Seu número tem {} dezenas '.format(num // 1 % 10))
print('Seu número tem {} centenas'.format(num // 10 % 10))
print('Seu número tem {} centenas'.format(num // 100 % 10))
print('Seu número tem {} milhar'.format(num // 1000 % 10))
