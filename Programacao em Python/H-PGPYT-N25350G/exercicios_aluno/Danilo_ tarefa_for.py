#Exercicios com for


#1 com range()
x = 22
y = 0
z = 200


for i in range ( y, z, x):
    print(i)

#2 com lista
animais = ["gato", "cachorro", "pássaro", "tigre"]

for j in animais:
    print("Animal: ",j)

#3 com enumerate()

nomes = ["Ana", "Bruno", "Carlos"]

for n in enumerate (nomes):
    print(n)

nomes = ["Ana", "Bruno", "Carlos"]

for n in enumerate (reversed(nomes)):
    print(n)

#4 com zip()

produtos = ["Arroz", "Feijão", "Café", "Leite"]
presos = ["5.20", "4.50", "4.57", "5.30"]

for i,j in zip (produtos, presos):
    print(i,j)

#5 com string()

for i in ("python é a mehor linguagem do mundo"):
    print(i)