# def titulo(txt):
#     print("-" * 30)
#     print(txt)
#     print("-" * 30)


# for i in range(0, 10):
#     titulo("Hello World")

# def soma(a, b):
#     print(f"A = {a} e B = {b}")
#     s = a + b
#     print(f"A soma de A + B é {s}")


# soma(b=4, a=5)
# soma(7, 2)

def dobra(lst):
	pos = 0
	while pos < len(lst):
		lst[pos] *= 2
		pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
