mensagens = ("um número", "outro número", "mais um número", "ultimo número")
tupla_mestre = valor_pares = ()

for c in range(0, 4):
    valor = int(input(f"Digite {mensagens[c]}: "))
    tupla_mestre += (valor,)

print("-=" * 30)

print(f"Você digitou os valores: {tupla_mestre}")

if 9 in tupla_mestre:
    print(f"O valor 9 apareceu {tupla_mestre.count(9)} vezes")
else:
    print(f"Não foi digitado 9 em nenhuma posição!")

if 3 in tupla_mestre:
    print(f"O valor 3 apareceu na {tupla_mestre.index(3)+1}° posição")
else:
    print(f"Não foi digitado 3 em nenhuma posição!")

print(f"Os números pares que foram inseridos são: ", end='')

for n in tupla_mestre:
    if n % 2 == 0:
        print(f"{n} ", end='')

print("")
print("-=" * 30)
