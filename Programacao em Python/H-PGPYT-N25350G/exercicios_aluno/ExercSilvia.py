
'''
#Exercicio 1 Jogo: Pedra, Papel e Tesoura

print('Vamos jogar Pedra, Papel e Tesoura')
jogador1 = input('Digite seu nome jogador 1 ')
jogador2 = input('Digite seu nome jogador 2 ')

pedra = 1
papel = 2
tesoura = 3

jog1 = int(input('Jogador 1 escolha entre as opções 1 para pedra, 2 para papel, 3 para tesoura '))
jog2 = int(input('Jogador 2 escolha entre as opções 1 para pedra, 2 para papel, 3 para tesoura '))

if jog1 == jog2:
    print('Jogar novamente')
if (jog1 == 1) & (jog2 == 2):
    print( jogador2, 'venceu')
if (jog1 == 1) & (jog2 == 3):
    print( jogador1, 'venceu')
if (jog1 == 2) & (jog2 == 1):
    print( jogador1, 'venceu')
if (jog1 == 2) & (jog2 == 3):
    print( jogador2, 'venceu')
if (jog1 == 3) & (jog2 == 1):
    print(jogador2, 'venceu')
if (jog1 == 3) & (jog2 == 2):
    print(jogador1, 'venceu')

else:
      print ('Jogar Novamente')

'''
'''
#Exercicio 2 Vamos jogar "Par ou Impar"

print("Vamos Jogar Par ou Ímpar")

escolha_jogador1 = input("Jogador 1, Você escolhe Par ou Ímpar? (P/I): ").strip().upper()
while escolha_jogador1 not in ["P", "I"]:
    escolha_jogador1 = input("Escolha inválida. Digite P para Par ou I para Ímpar: ").strip().upper()

escolha_jogador2 = "I" if escolha_jogador1 == "P" else "P"

numero_jogador1 = int(input("Jogador 1, escolha um número: "))
numero_jogador2 = int(input("Jogador 2, escolha um número: "))

soma = numero_jogador1 + numero_jogador2

resultado = "P" if soma % 2 == 0 else "I"

print(f"Soma dos números: {soma}")
print("Resultado: Par" if resultado == "P" else "Resultado: Ímpar")

if resultado == escolha_jogador1:
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")

'''

'''
#Exercicio 3 Crie um jogo de adivinhar um numero

import random

# Gera um número aleatório entre 1 e 5
numero_secreto = random.randint(1, 5)

# Pede ao jogador para adivinhar o número
palpite = int(input("Adivinhe o número (entre 1 e 5): "))

# Verifica se o jogador acertou
if palpite == numero_secreto:
    print("Você ganhou!")
else:
    print("Não foi desta vez. O número era", numero_secreto)

'''

'''

#Exercicio Liste os Dias da Semana e, caso seja, final de semana exiba se é final de semana


dias_da_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]

for dia in dias_da_semana:
    if dia in ["sábado", "domingo"]:
        print(f"{dia.title()} - Final de semana")
    else:
        print(f"{dia.title()}")

'''

'''
#Faça um laço que exiba os números da faixa solicitada pelo usuário e diga se é par ou impar. E tudo isto usando laço while.

inicio = int(input("Digite o número inicial da faixa: "))
fim = int(input("Digite o número final da faixa: "))

numero = inicio

while numero <= fim:
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
    numero += 1

'''