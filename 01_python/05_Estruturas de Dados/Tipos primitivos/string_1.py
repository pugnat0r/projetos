nome1 = "ViToR"
nome = "      VitOR      "
print(nome.upper())  # Converte para maiúsculas
print(nome.lower())  # Converte para minúsculas
print(nome.title())  # Converte a primeira letra de cada palavra para maiúscula

print(nome.strip())  # Remove espaços no início e no final
print(nome.lstrip())  # Remove espaços no início
print(nome.rstrip())  # Remove espaços no final


print(nome.center(14)) # Centraliza a string com espaços como preenchimento
print(nome.title().strip().center(14, "#"))  # Centraliza a string com '#' como preenchimento
print("-".join(nome1)) # Une os caracteres da string com '-'