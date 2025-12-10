
p1 = int((input("Digite o primeiro termo da PA: ")))
r = int((input("Digite a razão da PA: ")))

print("Os 10 primeiros termos dessa PA são: ")
print(f"a1 = {p1}")

for c in range(2, 11):
    print(f"a{c} = {p1} + {r} = {p1 + r}")
    p1 += r
