...

#exercicio 1

nome= input ("nome do aluno")
nota1= int(input ("digite a primeira nota"))
nota2= int(input ("digite a segunda nota"))
nota3= int(input ("digite a terceira nota"))
notamedia= ((nota1+nota2+nota3)/3)
print (nota1,nota2,nota3,notamedia)

if notamedia > 7:
    print('aprovado')

else : 
    print ('reprovado') 


...

#exercicio 2

nome= input ('nome do usuario')
peso= float (input('informe o peso'))
altura= float (input('informe altura'))
mediaIMC= float (peso/altura**2)
print ('resulado IMC:', mediaIMC)  

if mediaIMC <= 18.5:
    print ('magreza, obesidade grau 0')
if mediaIMC >=18.5 <=24.9:
    print ('normal, obesidade grau 0')
if mediaIMC >=25.0 <=29.9:
    print ('Sobrepeso, obesidade grau I')
if mediaIMC >=30.0 <=39.9:
    print ('obesidade, obesidade grau II')
if mediaIMC >40.0:
    print ('obesidade grave, obesidade grau III') 


...

#exercicio 3



    