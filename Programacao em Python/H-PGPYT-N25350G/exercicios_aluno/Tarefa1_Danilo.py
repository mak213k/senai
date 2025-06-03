#Exercicios 1 Média

aluno=input('Digite o nome do aluno:')
nota1=int(input('digite a primeiro nota: '))
nota2=int(input('digite a segunda nota: '))
nota3=int(input('digite a terceira nota: '))
#print(nota1)
media=int((nota1+nota2+nota3)/3 )
print('A média do aluno(a) ,',aluno, 'é',media)

if media > 7:
    print('aprovado')
else:
    print('reprovado')


#Exercicios 2 Imc

peso=float (input('Informe seu peso: '))
altura=float (input('Informe a altura: '))
imc=float(peso/(altura**2))
print('O seu imc é: ',imc)

if imc < 18.5:
    print('Magreza, obesidade grau 0')
if imc >=18.5<=24.9:
    print('Normal, obesidade grau 0')
if imc >=25<=29.9:
    print('Sobrepeso, Obesidade grau 1')
if imc >=30<=39.9:
    print('Obesidade, grau 2')
if imc >40:
    print('Obesidade grave, grau 3')


#Exercicios 3 desconto supermercado

    valorcompra= float(input('Informe o valor da compra: '))
desconto= float(input('informe o desconto: '))
valorfinal= float((valorcompra*desconto/100)-valorcompra)
if valorcompra > 100:
    print('Valor com desconto de: ', valorfinal)
else:
        print('Valor sem desconto: ', valorcompra)


