
Bchocolate = 31  # 1000g
Lcondensado = 3  # 12u
Cleite = 3.5  # 12u

ChocolatePó = 5.70  # 200g
Amendoim = 16  # 1000g
Coco = 3.60  # 50g

# Trufa de brigadeiro

brigadeiro = float(Bchocolate / 48)
brigadeiro += float((ChocolatePó/200)*50)/12
brigadeiro += float(Lcondensado/12)
brigadeiro += float(Cleite/12)

# Trufa de Amendoim

amendoim = float(Bchocolate / 48)
amendoim += float((Amendoim/1000)*50)/12
amendoim += float(Lcondensado/12)
amendoim += float(Cleite/12)

# Trufa de Coco

coco = float(Bchocolate / 48)
coco += float(Coco/12)
coco += float(Lcondensado/12)
coco += float(Cleite/12)


print(" Truffa de Brigadeiro: R$ {:.2f} \n Truffa de Amendoim: R$ {:.2f} \n Truffa de coco: R$ {:.2f} \n "
      .format(brigadeiro, amendoim, coco))
