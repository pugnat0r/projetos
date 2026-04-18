
def área(a, b):
    print(f'A área de um terreno {a}x{b} é de {a*b}m²')


print(' Controle de terreno  ')
print('-'*25)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

área(largura, comprimento)
