# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = 100  # float(input("Preço: ").strip())
cupom = "DESCONTO10"  # input("cupom: ").strip()

# TODO: Aplique o desconto se o cupom for válido:

if cupom in descontos:
    valor_final = preco * (1 - descontos[cupom])
else:
    valor_final = preco

print(valor_final)
print(cupom)