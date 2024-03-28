# Dada uma venda, calcular e exibir o desconto de 10% para compras acima de 500 reais
# entrada1 : venda: 500
# saída1 : valor final: 450
# entrada2: venda: 200
# saida2: valor final: 200
#
# PseudoCodigo
# var
# venda, desconto: real
# Inicio
# Escreva "Digite o valor da venda: "
# Leia venda
# Se venda > 300 então
#   desconto = venda * 10/100
#   venda = venda - desconto
#   fim_se
# Escreva "Novo valor = ", venda
# Fim

venda = float(input("Digite o valor da venda:"))
if venda > 300 :
    desconto = venda * 10 / 100
    venda = venda - desconto
print("Novo valor = ", venda)

