palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for c in range(0, len(palavras)):

    separador = tuple(palavras[c])
    vogais = ""

    for i in range(0, len(separador)):

        if separador[i] in "AEIOUaeiou":
            vogais += " " + separador[i]

    print(f"Na palavra {palavras[c]} temos {vogais}")
