# Simule um caixa de supermercado aplicando um desconto nas compras acima de R$100,00

compra=float(input("Qual o total das compras para darmos um desconto?"))
if compra>100:
    desconto=compra*100.10
    valor_com_desconto=compra - desconto
    print('Você ganhou 10% de desconto')

else:
    print('Não foi consedido o desconto')