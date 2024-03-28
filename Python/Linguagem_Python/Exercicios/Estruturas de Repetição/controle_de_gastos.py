valor_total = 0

qtda_transacoes = int(input("informe o total de Transações: "))

for i in range(1, qtda_transacoes + 1):
    transacao = float(input(f"Informe o valor da {i}ª transação: "))
    valor_total += transacao

media = valor_total / qtda_transacoes

print(f"Valor total gasto: R$ {valor_total:.2f}\nMédia por transação: R$ {media:.2f}")
