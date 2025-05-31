# n1 = float(input("Digite a nota 1:"))
# n2 = float(input("Digite a nota 2:"))
# n3 = float(input("Digite a nota 3:"))



# media_das_notas= (n1 + n2 + n3)/3
# print(f'A média das notas é:{media_das_notas:.2  f}')
# if media_das_notas >= 7:
#     print("Aprovado, sua média é maior que 7. Parabéns!")
# else:
#     print("Reprovado, sua média é menor que 7. Você está de recuperação!")



    # Atividade 2: Calculadora de IMC
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")
if imc <18.5:
    print("magreza, abaixo do peso ideal - obesidade grau 0")
elif imc>18.5 and imc<=24.9:
    print("peso normal - obesidade grau 0")
elif imc>25.0 and imc<=29.9:
    print("sobrepeso - obesidade I")
elif imc>30.0 and imc<=39.9:
    print("obesidade- Obesidade grau II")
else:
    print("obesidade grave - Obesidade grau III")
