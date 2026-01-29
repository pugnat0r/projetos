valores = []

# Criando um loop para inserir 4 números
for pos in range(0, 5):
    print(f"Lista atualizada: {valores}")

    valor = int(input(f'Digite um número: '))

    if pos == 0 or valor > valores[len(valores)-1]:
        valores.append(valor)
        print('Adicionado ao final da lista!')
    
    elif valor < valores[0]:
        valores.insert(0, valor)
        print('Adicionado na pos 0')

    else:
        for ind, val in enumerate(valores):
            if valor > val:
                continue
            else:
                valores.insert(ind, valor)
                print(f"Adicionado na pos {ind}") 
                break
            

print(valores)
