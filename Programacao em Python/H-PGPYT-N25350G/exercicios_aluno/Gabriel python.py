def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    nome = input("Digite o nome do aluno: ")
    notas = []

    for i in range(1, 4):  # Supondo 3 notas
        nota = float(input(f"Digite a nota {i} de {nome}: "))
        notas.append(nota)

    media = calcular_media(notas)
    status = verificar_aprovacao(media)

    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")

if __name__ == "__main__":
    main()
