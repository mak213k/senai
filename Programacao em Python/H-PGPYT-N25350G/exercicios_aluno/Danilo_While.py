'''
# laço de repetição
contador = 0
while contador < 3:
    print(contador)
    contador + 1
'''


contador = int(input('digite o numero inicial'))
fim = int(input('digite o numero final'))
while contador < fim:
    if contador % 2 == 0:
        print('par')
    else:
        print('impar')