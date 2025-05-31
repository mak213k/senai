nome = input("Digite seu nome:")
peso = float(input("digite seu peso em kg(ex:70.5):"))
altura = float(input("digite sua altura em metros (ex: 1.80):"))

imc = peso/(altura**2)

print(f"\{nome}, seu IMC é: {imc:.2f}")

if imc <18.5:
    classificação = "Abaixo do peso ideal"
elif imc<24.9:
    classificação = "Peso ideal"
elif imc<29.9:
    classificação = "Sobrepeso"
elif imc<34.9:
    classificação = "Obesidade primeiro grau"
elif imc<39.9:
    classificação = "Obesidade segundo grau"
else:
    classificação = "Obesidade morbida"

print(f"Classificação:{classificação}")

print("\nComparações:")
print(f"IMC maior que 25?{'Sim' if imc>25 else 'não'}")
print(f"IMC dentro da faixa saudável(18.5 a 24.9)?{'sim'if 18.5<=imc<=24.9 else 'não'}")
