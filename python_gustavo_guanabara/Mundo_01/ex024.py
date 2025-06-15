city = str(input('Qual é a sua cidade? ')).strip()

print('Começa com ( santo ): {}'.format( city[:5].lower() == 'santo' ))
