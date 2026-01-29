valores = []
le, le2, le3, ri = '\033[1;97m', '\033[1;91m', '\033[1;96m', '\033[m'

for c in range(5):
    while True:
        num = input(f'\nDigite um número ({c + 1}º): ').strip()
        if num.isdigit():
            num = int(num)
            break

    if num not in valores:
        for i, v in enumerate(valores):  # valor menor ou igual a existente
            if num <= v:
                valores.insert(i, num)
                print(
                    f'\n{le}O valor{ri} {le3}{num}{ri} {le}foi inserido na{ri} {le2}{i + 1}ª{ri} {le}posição da lista.{ri}')
                break
        else:  # primeiro valor; novo MAIOR valor
            valores.append(num)
            print(f'\n{le}O valor{ri} {le3}{num}{ri} {le}foi adicionado a lista.{ri}' if not valores else f'\n{le}O valor{ri} {le3}{num}{ri} {le}foi inserido ao final da lista.{ri}')
    else:  # duplicata
        print(f'\n{le2}Valor já adicionado.{ri}')


print(f'\n\n\n{le}Valores digitados:{ri}\n\n'
      + (', '.join(f'{le3}{x}{ri}' for x in valores)))
