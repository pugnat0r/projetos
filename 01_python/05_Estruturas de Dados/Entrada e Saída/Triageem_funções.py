def triagem(pacientes):
    n = int(input().strip())

    for _ in range(n):
        partes = [p.strip() for p in input().split(",")]
        nome, idade, status = partes
        idade = int(idade)
        status = status.lower()
        pacientes.append((nome, idade, status))

    return pacientes


def prioridade(lista_de_pacientes):
    # Separe em baldes
    urg_90mais = []
    urg_ate89 = []
    idosos = []      # 60+ (não urgentes)
    normal = []

    for nome, idade, status in lista_de_pacientes:
        if status == "urgente" and idade >= 90:
            urg_90mais.append(nome)
        elif status == "urgente" and idade < 90:
            urg_ate89.append(nome)
        elif idade >= 60:
            idosos.append(nome)
        else:
            normal.append(nome)

    # Ordem final: urgentes 90+, urgentes <90, idosos, normal
    ordem = urg_90mais + urg_ate89 + idosos + normal
    return ", ".join(ordem)


def main():
    pacientes = []
    pacientes = triagem(pacientes)
    lista = prioridade(pacientes)
    print(f"Ordem de Atendimento: {lista}")


main()
