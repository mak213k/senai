import random

def jogo_adivinhacao():
    print("🎲 Bem-vindo ao jogo de adivinhação!")
    numero_sorteado = random.randint(1, 5)

    try:
        palpite = int(input("Tente adivinhar o número entre 1 e 5: "))
        if 1 <= palpite <= 5:
            if palpite == numero_sorteado:
                print("🎉 Você ganhou!")
            else:
                print(f"😢 Não foi desta vez. O número era {numero_sorteado}.")
        else:
            print("⚠️ O número deve estar entre 1 e 5.")
    except ValueError:
        print("❌ Entrada inválida. Por favor, digite um número inteiro.")

# Executa o jogo
jogo_adivinhacao()