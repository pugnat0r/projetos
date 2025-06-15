# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do peso

# Entre 18.5 e 25: Peso ideal

# Acima 25 até 30: Sobrepeso

# Acima 30 até 40: 0besidade

# Acima de 40: Obesidade mórbida

peso = float(input("Qual é o seu peso? "))

altura = float(input(f"Qual é a sua altura? (ex: 1.85m): "))


imc = peso/(altura**2)

print('{:.1f}'.format(imc))


if imc < 18.5:
    print("Você está abaixo do peso!")

elif 18.5 <= imc < 25:
    print("Você está no Peso ideal!")

elif 25 <= imc < 30:
    print("Você está Sobrepeso!")

elif 30 <= imc < 40:
    print("Você está com Obesidade!")

else:
    print("Você está em OBESIDADE MÓRBIDA!!")
