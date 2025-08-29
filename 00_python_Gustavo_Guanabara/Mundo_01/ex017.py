
catetoC = float(input('Qual a medida do cateto oposto: '))
catetoB = float(input('Qual a medida do cateto adjacente:  '))

A = pow(catetoC, 2)+ pow(catetoB, 2)

print('A hipotenusa é {:.2f}'.format((pow(A, 1/2))))


from math import hypot

co = float(input('Qual a medida do cateto oposto: '))
ca = float(input('Qual a medida do cateto adjacente: '))
hi = hypot(co, ca)

print('A hipotenusa é {:.2f}'.format(hi))