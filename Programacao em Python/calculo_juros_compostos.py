'''
1)Criar uma calculadora que gera a partir do capital inicial emprestador, taxa de juros anual e quatidade de parcelas mensais
das parcelas de um empréstimo.
*obs.: Revisar a função que gera as parcelas para entender se o método utilizado segue o padrão adotado pelos bancos.


2)Criar uma função que abate do saldo quando o cliente escolhe abater direto no saldo e não em parcelas futuras.

3)Criar uma função que abate no pagamento de parcelas futuras os juros aplicados.

'''


'''
Calculadora
'''

'''
Juros compostos
Fórmula: M = C * (1 + i)^t
Lembrando que tanto a taxa de juros quanto o tempo de duração devem estar na mesma unidade de medida.
'''
def calculaJurosCompostos(taxaDeJuros, qtdeParcelas):
    taxaDejurosComposto = (1 + taxaDeJuros)**qtdeParcelas
    return taxaDejurosComposto


'''
Juros Compostos:
Fórmula: Taxa Mensal = (1 + Taxa Anual)^(1/12) - 1.
'''
def converterJurosAnualParaMensal(taxaAnual):
    taxaMensal = (1 + taxaAnual) ** (1/12) - 1
    return taxaMensal


def calcularParcelaPrincipal(montante, periodo):
    return montante / periodo


# def calculaParcelaCobrada(parcelaPrincipal, taxaMensal):
#     return parcelaPrincipal + taxaMensal


'''
Função ainda em construção.

'''
def calcularMontantePagoAtual(saldo_descontado,  ):
    return None


'''
Calcular o saldo não pago pela quantidade de parcelas que ainda não foram pagas.

'''
def calculaMontantePelasParcelas(parcelas_nao_pagas):
    saldo_nao_pago = 0
    for parcela_nao_paga in parcelas_nao_pagas:
        saldo_nao_pago += parcela_nao_paga
    
    return saldo_nao_pago


def calcularListaDeParcelasComJuros(capital, taxaDeJuros, qtde_parcelas):
    parcela = capital / qtde_parcelas
    residuo = capital
    parcelasPrincipal = []
    parcelasJuros = []
    parcelasPagar = []
    
    for i in range(qtde_parcelas):
        parcelasPrincipal.append(parcela)
        jurosCompostoAnual = calculaJurosCompostos(taxaDeJuros, qtde_parcelas)
        jurosCompostoPeriodo = converterJurosAnualParaMensal(jurosCompostoAnual)
        parcelaJuros = residuo * (jurosCompostoPeriodo)
        parcelasJuros.append( round(parcelaJuros, 2) )
        parcelaPagar = ( round(parcelaJuros + parcela, 2) )
        parcelasPagar.append( round(parcelaPagar, 2) )
        residuo = residuo-parcela



    '''
    Impressão em tela dos dados
    do empréstimo.
    '''
    print("Valor Parcela Principal: ")    
    print(parcelasPrincipal)
    print("-----------------------")
    print("Taxa de Juros do Período por parcela:")  
    print(jurosCompostoPeriodo)
    print("-----------------------")
    print(" Parcelas à Pagar: ")  
    print(parcelasPagar)
    print("-----------------------")
    print("Residuo restante: "+str(residuo))


'''
Esta linha de código abaixo serve para evitar com que códigos/funções de outros módulos 
executem neste contexto deste módulo.
Traduzindo esta linha: Só rode estas funções abaixo que estão neste módulo apenas.
'''
if __name__ == '__main__':

    # print(converterJurosAnualParaMensal(0.06))
    # print(calculaJurosCompostos(1000,0.010,24))    
    # taxaMensal = converterJurosAnualParaMensal(0.06)
    # juros = calculaJurosCompostos(0.010,24)
    # print(juros)
    
    # print(calculaMontantePelasParcelas([120,120,120,130,150,180]))
    '''
    
    '''   

    
    capital = 10000
    taxaDeJuros = 0.05
    qtde_parcelas = 10
    calcularListaDeParcelasComJuros(capital,taxaDeJuros,qtde_parcelas)
    exit(0)



