lanche = ('Hambúrgue', 'Pizza', 'Suco', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")

print(f"Eu comi Pra caramba!!! ")


print(sorted(lanche))


a = (2, 5, 4)
b = (5, 8, 1, 2)

c = a + b

print(c)

# >> (2, 5, 4, 5, 8, 1, 2)

print(c.count(5))
print(c.index(4))
