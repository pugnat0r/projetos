# Faça um programa que tenha uma função escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(txt):

    tamanho_linha = len(txt) + 4

    print("~"*tamanho_linha)
    print(f"{txt:^{tamanho_linha}}")
    #print(txt.center(tamanho_linha, ))
    print("~" * tamanho_linha)


escreva("paralelepipido")
escreva("Vitor")
escreva("Echiley")