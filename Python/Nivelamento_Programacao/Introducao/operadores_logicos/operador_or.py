# Uma loja concede descontos para compras pagas com dinheiro OU com valor superior a R$ 100

valor_compra = float(input("Informe o total da compra: "))
forma_pagamento = int(input("""Escolha a opção de pagamento:
[1] Cartão de crédito 
[2] Dinheiro
Informe o meio de pagamento: """))

if valor_compra >= 100 or forma_pagamento == 2:
    valor_compra = valor_compra * 0.9
    print("O cliente tem direito a um desconto.")

print(f"O valor da compra é de {valor_compra}")
