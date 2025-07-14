email = input("Email:").strip()


if " " in email:
    print("E-mail inválido")

elif email.count("@") == 1:
    if ("@" in email) and (email[:1] != "@") and (email[-1:] != "@"):
        usuario, dominio = email.split("@")
        if usuario and dominio in ["gmail.com", "outlook.com"]:
            print("E-mail válido")
        else:
            print("E-mail inválido")
    else:
        print("E-mail inválido")
else:
  print("E-mail inválido")
