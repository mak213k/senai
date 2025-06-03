compra= float(input('Registre o valor da compra?'))

if compra > 100:
    desconto= compra * 0.10
    total= compra-desconto
    print (total) 
    
    
else:
  print('Infelizmente sua compra nao gerou desconto')