nome = "Vitor"
altura = 1.850

print(f"{nome:~^20} tem {altura:.2f}")

n = s = 0

while True:

    n = int(input("Digite um número: "))

    if n == 999:
        break

    s += n

print(f"A soma foi {s}")
