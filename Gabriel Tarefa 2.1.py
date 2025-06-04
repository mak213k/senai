import random

def vencedor(jogador, computador):
    if jogador == computador:
        return "Empate!"
    elif (
        (jogador == "pedra" and computador == "tesoura") or
        (jogador == "papel" and computador == "pedra") or
        (jogador == "tesoura" and computador == "papel")
    ):
        return "Você venceu!"
    else:
        return "Você perdeu!"

opcoes = ["pedra", "papel", "tesoura"]

print("Ola bem vindo ao jogo Pedra, Papel e Tesoura!")
jogador = input("Escolha: pedra, papel ou tesoura? ").lower()

if jogador not in opcoes:
    print("Escolha inválida.")
else:
    computador = random.choice(opcoes)
    print(f"O computador escolheu: {computador}")
    resultado = vencedor(jogador, computador)
    print(resultado)