def caixa_supermercado():
    print("=== CAIXA DO SUPERMERCADO ===")
    total = 0.0

    while True:
        try:
            entrada = input("Digite o preço do produto (ou digite 'fim' para encerrar): ").strip().lower()
            if entrada == 'fim':
                break
            preco = float(entrada)
            if preco < 0:
                print("Preço não pode ser negativo. Tente novamente.")
                continue
            total += preco
        except ValueError:
            print("Entrada inválida. Digite um número ou 'fim'.")
    
    print(f"\nTotal da compra: R$ {total:.2f}")

    if total > 100:
        desconto = total * 0.10
        total_com_desconto = total - desconto
        print(f"Desconto aplicado: R$ {desconto:.2f}")
        print(f"Total com desconto: R$ {total_com_desconto:.2f}")
    else:
        print("Nenhum desconto aplicado.")

    print("Obrigado por comprar conosco!")

# Executa o programa
caixa_supermercado()