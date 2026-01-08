saque_realizado = notas_50 = notas_20 = notas_10 = notas_1 = 0

saque = int(input("Digite o valor do saque:   "))

while saque != 0:

    if saque >= 50:
        notas_50 = int(saque / 50)
        saque_realizado = 50 * notas_50
        saque -= saque_realizado

        # Jeito mais simples de fazer
        # notas_50 += 1
        # saque -= 50

    elif saque >= 20:
        notas_20 = int(saque / 20)
        saque_realizado = 20 * notas_20
        saque -= saque_realizado

    elif saque >= 10:
        notas_10 = int(saque / 10)
        saque_realizado = 10 * notas_10
        saque -= saque_realizado

    elif saque >= 1:
        notas_1 = int(saque / 1)
        saque_realizado = 1 * notas_1
        saque -= saque_realizado

print("~"*30)

if notas_50 > 0:
    print(f"Você sacou {notas_50} notas de 50")

if notas_20 > 0:
    print(f"Você sacou {notas_20} notas de 20")

if notas_10 > 0:
    print(f"Você sacou {notas_10} notas de 10")

if notas_1 > 0:
    print(f"Você sacou {notas_1} notas de 1")

print("~"*30)
