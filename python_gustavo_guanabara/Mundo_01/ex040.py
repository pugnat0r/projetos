# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# Média abaixa de 5.0
# REPROVADO

# Média entre 5.0 e 6.9
# RECUPERAÇÃO

# Média 7.0 ou superior
# APROVADO


n1 = float(input('Sua primeira nota: '))
n2 = float(input('Sua segunda nota: '))

media = (n1 + n2) / 2


if media < 5.0:
    print('Sua média foi abaixo de 5.0 ')
    print('Sua média é {:.1f}'.format(media))
    print('Reprovado!!!')

elif 7 > media >= 5:
    #media >= 5 and media <= 6.9: Minha solução
    print('Sua média foi abaixo de 6.9')
    print('Sua média é {:.1f}'.format(media))
    print('Recuperação')

else:
    print('Sua média foi acima de 6.9')
    print('Sua média é {:.1f}'.format(media))
    print('APROVADO!!!')
