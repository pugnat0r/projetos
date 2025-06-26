v = input('Diga algo: ')
print(f' 1 - Seu tipo primitivo é: {type(v)}\n' 
      f' 2 - É somente palavras? {v.isalpha()}\n'
      f' 3 - É palavras ou/com números? {v.isalnum()}\n'
      f' 4 - É tudo maiusculo? {v.isupper()}\n'
      f' 5 - Contém só espaços? {v.isspace()}\n'
      f' 6 - É tudo minusculo? {v.islower()}\n'
      f' 7 - É da familia ASCII {v.isascii()}\n'
      f' 8 - É só numero ? {v.isnumeric()}\n'
      f' 9 - Está capitalizada? {v.istitle()}')



