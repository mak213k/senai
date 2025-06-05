import random
user= input("pedra,papel,tesoura?").lower()
pc= random.choice(['Pedra','Papel','tesoura'])

vence= {'pedra':'tesoura','papel':'pedra','tesoura':'papel'}
print(f"\nVoce:{user},PC:{pc}")
print("voce venceu!"if vence[user]== pc else "empate!" if user== pc else "PC ganhou") 


import random
soma=int(input("jogador 1, digite um numero:"))+(random.randint(1,10)) if input("jogador contra cpu? (s/n) ").lower()=='s' else int(input("jogador 2, digite um numero:"))
print(f"\soma:{soma} é{'par'if soma % 2 ==0 else'inpar'} - jogador{'1' if input('jogador1,escolha inpar ou par:').lower()==('par'if soma % 2== 0 else 'inpar')else '2'}ganhou")


import random
numero_secreto=random.randint(1, 5)
chute=int(input("adivine um numero entre 1 e 5:"))
if chute ==numero_secreto:
    print("voce ganhou !")
else:
    print(f"Nao foi desta vez. numero era{numero_secreto}.")


dia=int(input("Escolha 1,2,3,4,5,:" ))

match dia:
    case 1:
        print("Segunda Feira")
    case 2:
        print("Terça Feira ")
    case 3:
        print("Quarta Feira")
    case 4:
        print("Quinta Feira")
    case 5:
        print("Sexta Feira")    
    case _:
        print("Final De Semana")
