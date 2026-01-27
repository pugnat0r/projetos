# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. 



pagamentos_parenteses = 0

exp = str(input(f"Digite sua expressão: "))

for i in exp:

    if pagamentos_parenteses == 0 and i == ")":

        print("Sua expressão está ERRADA!")
        break

    elif i == "(":
        pagamentos_parenteses += 1
    elif i  ==  ")":
        pagamentos_parenteses -= 1

if pagamentos_parenteses == 0:
    print(f"A expressão está CERTA!")
else:
    print(f"A expressão está ERRADA!")



