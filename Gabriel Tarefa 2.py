def jogo_impar_par():
    print("Bem-vindo ao jogo de Ímpar ou Par!")
    
    # Escolha dos jogadores
    jogador1 = input("Jogador 1, digite seu nome: ")
    jogador2 = input("Jogador 2, digite seu nome: ")

    # Jogador 1 escolhe entre ímpar ou par
    while True:
        escolha_j1 = input(f"{jogador1}, você escolhe ímpar ou par? (i/p): ").lower()
        if escolha_j1 in ['i', 'p']:
            break
        print("Escolha inválida. Digite 'i' para ímpar ou 'p' para par.")
    
    escolha_j2 = 'p' if escolha_j1 == 'i' else 'i'

    # Jogadores escolhem seus números
    while True:
        try:
            num1 = int(input(f"{jogador1}, escolha um número de 0 a 10: "))
            num2 = int(input(f"{jogador2}, escolha um número de 0 a 10: "))
            if 0 <= num1 <= 10 and 0 <= num2 <= 10:
                break
            else:
                print("Os números devem estar entre 0 e 10.")
        except ValueError:
            print("Por favor, insira números válidos.")

    soma = num1 + num2
    resultado = "par" if soma % 2 == 0 else "ímpar"

    print(f"\n{jogador1} escolheu {'ímpar' if escolha_j1 == 'i' else 'par'}")
    print(f"{jogador2} ficou com {'ímpar' if escolha_j2 == 'i' else 'par'}")
    print(f"{jogador1} jogou {num1}, {jogador2} jogou {num2}. Soma = {soma}, que é {resultado}.")

    if (resultado == "ímpar" and escolha_j1 == 'i') or (resultado == "par" and escolha_j1 == 'p'):
        print(f"🏆 {jogador1} venceu!")
    else:
        print(f"🏆 {jogador2} venceu!")

# Executa o jogo
jogo_impar_par()