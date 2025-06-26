from math import trunc

n1 = float(input('Diga um número quebrado: '))
n2 = trunc(n1)

print('Seu número é {} \nSua parte inteira é {}'.format(n1, n2))