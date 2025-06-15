frase = str(input("digite uma frase: ").strip().lower())

print('a letra a aparece',frase.count("a"),'vezes')

print('a primeira ocorrencia da letra a é na',frase.find("a")+1,'º posição')

print('a última ocorrencia '
      'da letra a é na',frase.rfind("a")+1,'º posição')