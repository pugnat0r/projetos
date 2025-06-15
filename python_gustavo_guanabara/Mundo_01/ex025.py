nome = str(input("Qual é o seu nome? ")).strip()
encontre = 'silva' in nome.lower()

print('Seu nome tem Silva?')
print('')

if (encontre == True):
    print('Seu nome TEM SILVA!!')

if (encontre == False):
    print('Seu nome NÃO TEM SILVA!!')
