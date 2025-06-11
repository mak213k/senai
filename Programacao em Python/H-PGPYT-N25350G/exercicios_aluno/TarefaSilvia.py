
'''
#1 Com range() / Enuciado: numeros 0 a 200 e pule de 11 a 11

x = 22
y = 0
z = 200

for i in range(y,z,x):
    print(i)

'''

'''
# 2 Com lista () / Enunciado: Dada a lista de animais = ['gato','cachorro', 'passaro','tigre'], imprimir cada animal com a frase: Animal: antes do nome

animais =  ['gato','cachorro','passaro','tigre']


for i in animais:
    print ("Animal:",i)

'''

'''

#3 Com enumerate()  Enunciado: Imprima os indices e nome da Lista ['Ana', 'Bruno', "Carlos"]. Depos faça o mesmo exercicio invertendo os elementos

Nomes = ["Ana", "Bruno", "Carlos"]

#for i in enumerate (Nomes):
 #  print (i) 

for i in enumerate(reversed(Nomes)):
    print (i)

'''
'''
#4 Com zip() Enunciado: Dada duas listas de produtos ["Arroz", "Feijao","Cafe","Leite"] e preços  = [5.20,4.50,4.57,5.3], imprima o nome do produto seguido do preço

produto = ["Arroz,","Feijao","Cafe","Leite"]
preços = [5.20,4.50,4.57,5.3]

for i,j in zip (produto, preços):
    print (i,j)

'''

'''

# 5 Com string imprima cada letra da Palabra "Python é a melhor linguagem do mundo" em uma linha

frase = ["Python é a melhor linguagem do mundo"]
for i in (frase):
    print (i)
'''