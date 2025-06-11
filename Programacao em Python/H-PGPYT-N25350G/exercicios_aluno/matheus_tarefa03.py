1.com range()
x=200
y=0
t=11
for i in range(y,x+1,t):
    print(i)

2.com lista
lista_animal=["Animal:gato","Animal:cachorro","Animal:tigre",]
for i in lista_animal:
   print(i)

3.com enumerate()
lista_nomes=("ana" ,"bruno","carlos")
for i in enumerate(lista_nomes):
    print(i) 


lista_nomes=((reversed)("ana bruno carlos"))
for i in lista_nomes:
    print(i)  


 
4.com zip

lista=["arroz","feijao","cafe","leite"]
precos=[5.20, 4.50, 4.57, 5.3]
for lista,precos in zip(lista,precos):
       print(f"{lista}:R${precos:.2f}")

5 com string

nome=("Python é a melhor linguagem do mundo")
for i in nome:
    print(i)


