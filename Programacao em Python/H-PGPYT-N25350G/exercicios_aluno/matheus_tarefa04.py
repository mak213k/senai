


# 1.Verificação de email validos

# import re
# def verifica_email(e):
#     print(["Email invalido","Email valido"][bool(re.match(r"^[a-zA-Z0-9.+-]+@[a-zA-z0-9-]+\.com$", e))])

# verifica_email(input("Digite seu email:"))

# 2.Sistema  de ponto 

# def calcular_horas_trabalhadas():
#     e= input("Entrada(HH:MM):").split(":")
#     s= input("Saida (HH:MM):  ").split(":") 
#     h= (int(s[0])*60+int(s[1]))-(int(e[0]*60+int(e[1])))/60
#     print(f"Horas trabalhadas:{h:.2f}h.{'ok'if h >= 8 else f'faltaram{8-h:.2f}h'}")

# calcular_horas_trabalhadas()   