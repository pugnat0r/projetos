def teste_função(**dict_1):

    meta_dados = " ".join(
        [f"{chave} {valor}" for chave, valor in dict_1.items()])
    print(meta_dados)


teste_função(nome="vitor", idade=23)
