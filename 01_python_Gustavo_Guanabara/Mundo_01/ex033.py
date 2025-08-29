n1 = int(input('Diga um number n1 '))
n2 = int(input('Diga um number n2 '))
n3 = int(input('Diga um number n3 '))

maior = n1

if (n2 > n1) and (n2 > n3):
    maior = n2
if (n3 > n2) and (n3 > n1):
    maior = n3

print('O maior número é {}'.format(maior))

menor = n1

if (n2 < n1) and (n2 < n3):
    menor = n2
if (n3 < n2) and (n3 < n1):
    menor = n3

print('O menor número é {}'.format(menor))
