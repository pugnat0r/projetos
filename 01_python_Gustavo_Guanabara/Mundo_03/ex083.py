# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
par_esq = par_dir = 0
exp = []

exp.append(str(input('Digite a expressão: ')))

for i in exp[0]:
    if i == '(':
        par_esq += 1
    elif i == ')':
        par_dir += 1
    else:
        continue

if par_dir % 2 == 0:
    if par_esq % 2 == 0:
        print(f'Sua espressão está valida! ')

else:
    print(f'Sua espressão está errada! ')
