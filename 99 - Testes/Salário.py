from cores import ColorsText, ColorsBack, StyleText

print(" \033[33m Hello World")

print(f" {ColorsText['Orange']} Hello World {ColorsText['cls']}")


bruto = float(input('Quanto você recebe por hora? '))

print('')
print('Você recebe {} por dia!'.format(bruto*8))
print('Você recebe {} por mês!'.format((bruto*8)*20))
print('')
