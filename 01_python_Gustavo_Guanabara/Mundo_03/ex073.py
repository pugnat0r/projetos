
times = ('Flamengo', 'Corinthians', 'Palmeiras', 'Atlético-MG', 'São Paulo',
         'Fluminense', 'Botafogo', 'Athletico-PR', 'Bahia', 'Chapecoense',
         'Cruzeiro', 'Grêmio', 'Fortaleza', 'Internacional', 'Red Bull Bragantino',
         'Santos', 'Juventude', 'Atlético-GO', 'América-MG', 'Vitória')


print(f'\n {"Tuplas de times do Brasileirão":^100}')
print('~^'*50)
print(f'''
        {times[0:5]}
        {times[5:10]}
        {times[10:15]}
        {times[15:20]}
''')
print('~^'*50)

print(f"\n\n\nOs  5 primeiros times do Brasileirão: {times[0:5]}")

print(f"\nOs 4 ultimos são: {times[-4:]}")

print(f"\nO Chapecoense está na {times.index('Chapecoense')+1}° posição")

print(
    f'\n\n\n{"Lista de times do Brasileirão Organizados em Ordem Alfabética:":^100}')
print('~^'*50)
ordem = sorted(times)
print(f'''
        {ordem[0:5]}
        {ordem[5:10]}
        {ordem[10:15]}
        {ordem[15:20]}
''')
print('~^'*50)
