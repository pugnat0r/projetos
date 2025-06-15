m = float(input('Quantos metros? '))

print('{:_^100}'.format('Para dam'))
print('{:.1f} dam'.format(m/10))

print('{:_^100}'.format('Para hm'))
print('{:.2f} hm'.format(m/100))

print('{:_^100}'.format('Para km'))
print('{:.3f}'.format(m/1000))

print('{:_^100}'.format('Para cm'))
print('{:.0f} cm'.format(m*100))

print('{:_^100}'.format('Para mm'))
print('{:.0f} mm'.format(m*1000))

print('{:_^100}'.format('Para dm'))
print('{:.1f} dm'.format(m*10))
