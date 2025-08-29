maioridade = 18
idade_especial = 17

idade = int(input("Digite sua idade:"))

if idade >= maioridade:
    print("_______________________________")
    print("Você é maior de idade.")
    print("Você pode tirar carteira de motorista.")
    print("_______________________________")

elif idade == idade_especial:
    print("_______________________________")
    print("Você é menor de idade, \nmas pode tirar carteira de motorista com autorização dos pais.")
    print("_______________________________")

else:
    print("_______________________________")
    print("Você é menor de idade e não pode tirar carteira de motorista!! ")
    print("_______________________________")
