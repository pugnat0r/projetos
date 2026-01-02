# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

# controlador = True

# A solução abaixo funciona, mas não é a ideal, por que usa um controlador externo e é muito longa.

# while controlador == True:

#     type_sex = str(input(f"Digite o seu Sexo: [M/F]: "))

#     if type_sex in "MmFf":
#         if type_sex in "Mm":
#             print("Sexo Masculino registrado com sucesso!")
#             controlador = False
#         else:
#             print("Sexo Feminino registrado com sucesso!")
#             controlador = False
#     else:
#         print("Dados inválidos. Por favor, digite novamente.")


sex = str(input(f"Digite o seu Sexo: [M/F]: "))

while sex not in "MmFf":
    sex = str(
        input(f"Dados inválidos. Por Favor, digite novamente o sexo [M/F]"))
