nome = input ("Eduarda")
nota1= float(input("7.0"))
nota2= float(input("5.0"))
media=(nota1 +nota2) / 2
if media >=7.0:
    print ("situação: aprovado")
elif media<=5.0 :
     print ("situação:reprovado")
else:
     print ("situação:reprovado")

calculate_imc()
nome = input("Ana")
peso= float(input(75.5))
altura= float(input(1.80))
imc= peso/ (altura ** 2)
if imc < 18.5:
     print ("classificação; magreza")
     print("grau_obesidade= 0")
elif 18.5 <= imc <25.0:
     print("classificação=normal")
     print ("grau_obesidade=0")
elif 25.0 <= imc < 30.0 :
     elif 30.0<=