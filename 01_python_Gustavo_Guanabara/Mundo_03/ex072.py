from click import pause


números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

entrada_user = 21

while entrada_user < 0 or entrada_user > 20:
    print("Entre 0 -> 20 ")
    entrada_user = int(input("Digite um número: "))

print("~"*30)
print(f"\nVocê digitou o {números[entrada_user]}\n")
print("~"*30)
