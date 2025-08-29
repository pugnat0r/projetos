texto = input("Digite um texto: " )
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=' ')

else:
    print("\nFim do loop")
    # O loop for percorre cada letra do texto e verifica se é uma vogal.    
    print() # Imprime uma nova linha após o loop


for numero in range(0, 51, 5):  # range(início, fim, passo)
    print(numero, end=' ') # end=' ' evita a quebra de linha após cada número
