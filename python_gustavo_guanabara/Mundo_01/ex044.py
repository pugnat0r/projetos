# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# À vista dinheiro/cheque: 10% de DESCONTO

# À vista no cartão: 5% de DESCONTO

# Em até 2x no cartão: PREÇO NORMALA

# 3x ou mais no cartão: 20% de juros

print(f" \033[4;31;45m {" LOJAS VITIM ":=^40} \033[0;00;00m")

valor = float(input("\033[1;00;42mVALOR:\033[0;00;00m "))

print(" ( 1 ) \033[0;00;43mDinheiro\033[0;00;00m")
print(" ( 2 ) \033[0;00;44mDébito\033[0;00;00m")
print(" ( 3 ) \033[0;00;41mCrédito\033[0;00;00m")

condição = int(input("Forma de pagamento: "))


if (condição == 1):
    print("")
    print("Seu pagamento foi no dinheiro!")
    print("Você ganhou 10% de DESCONTO!")
    print("Sua compra ficou no valor de R$ {} ".format(valor-(valor*0.10)))
    print("")

elif (condição == 2):
    print("")
    print("Seu pagamento foi Débito!")
    print("Você ganhou 5% de DESCONTO!")
    print("Sua compra ficou no valor de R$ {} ".format(valor-(valor*0.05)))
    print("")

elif (condição == 3):
    print("")
    print("Seu pagamento foi no Crédito")
    print("")
    parcelamento = int(input("quantas vezes você quer parcelar? "))
    print("Você escolheu parcelar em {} vezes!".format(parcelamento))
    print("")

    if (parcelamento == 1):
        print("Você escolheu pagar avista no cartão de crédito! Seu desconto é de 5%")
        print("Sua compra ficou no valor de R$ {}".format(valor-(valor*0.05)))

    elif (parcelamento == 2):
        print("Você escolheu pagar em 2x no cartão de crédito!")
        print("Sua compra ficou no valor de R$ {}".format(valor))

    elif (parcelamento >= 3) and (parcelamento <= 12):
        print("Você escolheu pagar em {} vezes".format(parcelamento))
        print("Sua parcela ficou no valor de R$ {} em {}x".format(
            (valor+(valor*0.2))/parcelamento, parcelamento))
        print("Sua compra ficou no valor de R$ {} com 20% de juros".format(
            valor+(valor*0.2)))
    else:
        print("Comando não encontrado! ")
else:
    print("Comando não encontrado!")
