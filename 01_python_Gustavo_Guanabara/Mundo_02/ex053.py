txt = input("Digite uma frase: ").strip().upper().replace(
    "Ô", "O").replace("-", "").replace(",", "").replace(" ", "")
n = len(txt)
inverso = txt[:: -1]

print(txt)

for c in range(n, n + 1):
    if inverso == txt:
        print("A frase é um palíndromo")
    else:
        print("A frase não é um palíndromo")
