cadastro = {
    "20087972794": {
        "Nome": "Vitor",
        "Idade": "23y"
    },

}

cpf = input("Diga seu CPF: ")

if cpf in cadastro:
    print(" cadrastro encontrado! ")
    print(cadastro [cpf])
else:
    print("CPF NÃO Encontrado! ")
