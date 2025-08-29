historia = {}
frase = "Vitor, programador"

profissão, nome = frase.split(", ")

for _ in range(1):
    if profissão not in historia:
        historia[profissão] = []
    
    historia[profissão].append(nome)

print(historia)