def verificar_situacao_aluno():
    print("=== SISTEMA DE NOTAS ===")

    nome = input("Digite o nome do aluno: ")

    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota"))
    except ValueError:
        print("Erro: você deve digitar números válidos para as notas.")
        return

    if not (0 <= nota1 <= 10) or not (0 <= nota2 <= 10):
        print("Erro: as notas devem estar entre 0 e 10.")
        return

    media = (nota1 + nota2) / 2

    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Situação: ✅ Aprovado")
    elif media >= 5:
        print("Situação: ⚠️ Recuperação")
    else:
        print("Situação: ❌ Reprovado")

# Executa o programa
verificar_situacao_aluno()