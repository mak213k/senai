
a = input('Qual o nome do aluno ? ')
b = float(input('Qual a primeira nota ? '))
c = float(input('Qual a segunda nota ? '))
d = float(input('Qual a terceira nota ? '))

e = (b + c + d) /2

if e >= 7:
    print(f"{a} foi aprovado!!")

else:
    print(f"{a} foi reprovado!!")