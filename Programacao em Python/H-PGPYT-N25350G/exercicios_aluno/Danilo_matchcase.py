#match
'''
a = int(input("Escolha 1, 2, 3:"))

match a :
    case 1: 
        print("Você escolheu um")
    case 2:
        print("Você escolheu dois")
    case 3:
        print("Você escolheu tres")
    case _:
        print("opção errada")
'''

    #Liste os dias da semana e, caso seja, final de semana exiba se é final de semana.

dia = (input("Digite o dia da semana, segunda, terça, quarta, quinta, sexta, sabado, domingo "))

match dia :
    case 'sabado':
        print('Final de semana')
    case 'domingo':
        print('Final de semana')
    case 'segunda':
        print('segunda não é final de semana')
    case 'terça':
        print('terça não é final de semana')
    case 'quarta':
        print('quarta não é final de semana')
    case 'quinta':
        print('quinta não é final de semana')
    case 'sexta':
        print('sexta não é final de semana')


        


