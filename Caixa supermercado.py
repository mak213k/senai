print("Bem vindo ao mercado!!")

a1 = float(input("Quanto você gastou para solicitarmos o desconto ?"))

if a1 > 100:
    desconto = a1 *0.10
    a2 = a1 - desconto
    print('Parabéns você ganhou 10% de desconto')

else: 
    print('Infelizmente não disponibilizamos o desconto')