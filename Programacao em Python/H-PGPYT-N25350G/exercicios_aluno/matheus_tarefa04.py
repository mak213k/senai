


# 1.Verificação de email validos

import re
def verifica_email(e):
    print(["Email invalido","Email valido"][bool(re.match(r"^[a-zA-Z0-9.+-]+@[a-zA-z0-9-]+\.com$", e))])

verifica_email(input("Digite seu email:"))

# 2.Sistema  de ponto 

def calcular_horas_trabalhadas():
    while True:
        try:
            e = input("Entrada (HH:MM): ").split(":")
            s = input("Saída (HH:MM): ").split(":")
            h = (int(s[0])*60 + int(s[1]) - (int(e[0])*60 + int(e[1])))/60
            print(f"Horas trabalhadas: {h:.2f}h. {'Ok' if h >= 8 else f'Faltaram {8-h:.2f}h'}")
            if input("Continuar? (s/n): ").lower() != 's':
                break
        except Exception as e:
            print("Erro:", e)

calcular_horas_trabalhadas()

# 3.geracao de relatorio

def calcular_media_vendas(vendas):
    total_vendas = sum(vendas)
    media = total_vendas / len(vendas)
    print(f"Total de vendas: {total_vendas:.2f}")
    print(f"Média de vendas: {media:.2f}")
    print(f"Número de funcionários: {len(vendas)}")
    print("Meta atingida!" if media > 1000 else "Meta não atingida.")

# Exemplo de uso
vendas = [1200, 900, 1500, 800, 1100]
calcular_media_vendas(vendas)





# 1.CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS




# 2 CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS

# def multiplicar(a,b,c):
#  return a * b * b
# print(multiplicar(5,10,20))




# 4.CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS

# idade=int(input("Digite Sua Idade:"))
# if idade == 18:
#     print("Parabens Voce é Maior de Idade!")
# else:
#     print("Sua Idade",idade,"Anos.")
        


# 5 DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA

# idade=input("Digite Sua Idade:")
# print(idade)


