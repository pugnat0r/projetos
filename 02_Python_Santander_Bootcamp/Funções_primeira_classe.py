def somar(a, b):
	return a + b


def exibir_resultado(a, b, funcao):
	resultado = funcao(a, b)
	print()
	print(f"O resultado da operação {a} + {b} = {resultado}")
	print()

exibir_resultado(10, 10, somar)
