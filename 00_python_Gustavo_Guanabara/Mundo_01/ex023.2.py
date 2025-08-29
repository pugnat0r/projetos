n = str((input('Diga um número entre 0 e 9999: ')))
a = '000'+ n

print(f'''
número: {n}

Unidade: {a[-1]}
Dezena: {a[-2]}
Centena: {a[-3]}
Milhar: {a[-4]}
      ''')