from math import cos,sin,tan,radians
an = float(input('Diga um angulo: '))
cos = cos(radians(an))
sen = sin(radians(an))
tan = tan(radians(an))

print('Coseno: {:.2f} \nSeno: {:.2f} \nTangente: {:.2f}'.format(cos,sen,tan))
