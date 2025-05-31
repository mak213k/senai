
n1 = input('Qual o nome do paciênte ? ')
n2 = int(input('Qual a sua idade ? '))
n3 = int(input('Qual o seu peso ? '))
n4 = float(input('Qual a sua altura ? '))

imc = n3 / (n4**2)  
print(f'{n1} seu IMC é:{imc}')

if imc < 18.50:
    print(f"{n1} você está em estado de magreza")

elif imc < 25:
    print(f'{n1} seu peso está normal') 

elif imc < 30:
    print(f'{n1} você está acima do peso')

elif imc < 40:
    print(f"{n1} você está obeso")

elif imc > 40:
    print(f'{n1} você está em obesidade nivel 3')

