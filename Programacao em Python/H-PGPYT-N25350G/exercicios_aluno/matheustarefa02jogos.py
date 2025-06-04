import random
user= input("pedra,papel,tesoura?").lower()
pc= random.choice(['Pedra','Papel','tesoura'])

vence= {'pedra':'tesoura','papel':'pedra','tesoura':'papel'}
print(f"\nVoce:{user},PC:{pc}")
print("voce venceu!"if vence[user]== pc else "empate!" if user== pc else "PC ganhou") 
