from click import pause


valores = []

for cont in range(0, 5):
    print(valores)
    valor = int(input('Digite um número: '))

    if cont == 0:
        valores.append(valor)
        print(f'Adicionado ao final da lista...')

    elif cont == 1:
        if valor > valores[0]:
            valores.append(valor)
            print(f"Adicionado ao final da lista...")

        else:
            valores.insert(0, valor)
            print('Adicionado na posição 0')

    else:
        for ind, val in enumerate(valores):

            if valor > val:
                print(
                    f'O valor adicionado é maior que o valor no indice {ind} sendo ele {val}')
                if valor > max(valores):
                    print(f"O valor adicionado é maior que o todos os valores da lista, vou adicionar ao final...")
                    valores.append(valor)
                    break
                
                continue

            else:
                print(
                    f'O valor adicionado não é maior que o comparado no indice {ind} sendo ele {val}')
                print(f"Vou colocar na pos {ind}")
                valores.insert(ind, valor)
                break


print(valores)
