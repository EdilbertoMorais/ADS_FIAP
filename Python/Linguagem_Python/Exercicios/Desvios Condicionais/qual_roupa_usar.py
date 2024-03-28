"""
Uma loja virtual FIAP Wear, que vende roupas personalizadas da instituição, disponibilizou
no mês do seu aniversário o cupom NIVER10, que concede um desconto de 10% no valor total da
compra feita no site.
Caso o cliente digite o cupom corretamente, deverá ser informado o valor final da compra já
com o desconto. Caso o cliente não digite o cupom corretamente, deverá ser informado o valor
sem o desconto.
"""
# Solicitando os dados para o usuário
valor_total = float(input("Informe o valor total da compra: "))
cupom = input("Informe o cupom para desconto: ").upper()
# Realizando o teste lógico.
if cupom == "NIVER10":
    # Primeira forma de aplicar o desconto
    # desconto = (valor_total * 10) / 100  # Valor do desconto
    # valor_total -= desconto  # Valor do desconto menos o total da compra

    # Segunda forma de aplicar o desconto
    valor_total = valor_total * 0.9  # Cáculo de 10% de desconto
    print(f"O valor total da compra já com o desconto aplicado é de R${valor_total}")
else:
    print(f"O valor total da compra é de R${valor_total}")
