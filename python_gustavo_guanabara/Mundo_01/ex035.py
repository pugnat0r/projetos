a = float(input('Diga qual é o lado A: '))
b = float(input('Diga qual é o lado B: '))
c = float(input('Diga qual é o lado C: '))

if b - c < a and a < b + c:
    if a - c < b and b < a + c:
        if a - b < c and c < a + b:
            print('Verdadeiro! Essas medidas podem formar um trianguinho')
        else:
            print('Esses valores não podem formar um trianguinho')
    else:
        print('Esses valores não podem formar um trianguinho')
else:
    print('Esses valores não podem formar um trianguinho')

