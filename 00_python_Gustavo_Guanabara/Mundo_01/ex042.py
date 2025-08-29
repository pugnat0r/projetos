# Refaça o desafio ex035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.

# Equilátero: todos os lados iquais

# isósceles: dois lados iquais

# Escaleno: todos os lados diferentes


s1 = float(input(" 1° Segmento: "))
s2 = float(input(" 2° Segmento: "))
s3 = float(input(" 3° Segmento: "))

ordem = [s1, s2, s3]
ordem.sort()

print("")
print(f"S1 {ordem[0]} \nS2 {ordem[1]} \nS3 {ordem[2]}")
print("")

if ordem[0] < ordem[1] + ordem[2] and ordem[1] < ordem[0] + ordem[2] and ordem[2] < ordem[0] + ordem[1]:

    print("")
    print("Esses segmentos podem formar um triângulo!")
    print("")
    print(ordem)
    if ordem[0] == ordem[1] == ordem[2]:
        print("")
        print("Equilátero")
        print("Todos os lados iquais")
        print("")

    elif ordem[0] == ordem[1] or ordem[0] == ordem[2]:
        print("")
        print("Isósceles")
        print("Dois lados iquais")
        print("")

    elif ordem[0] != ordem[1] and ordem[0] != ordem[2]:
        print("")
        print("Escaleno")
        print("Todos os lados diferentes")
        print("")


else:
    print("")
    print("Esses segmentos não podem formar um triângulos!")
    print(ordem)
    print("")
