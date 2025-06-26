n1 = float(139)

medida = float(0.01)

result = 0

while (result <= 36):
    result = n1 * medida

    medida+= 0.01

    porcento = medida * 100

    print("{:.4f}% de 139 é : {}  ".format(porcento, result))
