"""3 – Na oferta de um produto de crédito aos clientes, três informações são muito importantes
apresentar ao cliente: valor da dívida, a taxa de juros e o número de parcelas para pagamento do
empréstimo contraído junto à Fintech. Faça um programa que receba o valor de uma dívida e mostre
uma tabela com os seguintes dados:

O Valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela:

Quantidade Parcelas                                     % juros sobre o valor inicial da divída.
1                                                       0
3                                                       10
6                                                       15
9                                                       20
12                                                      25
"""

#  Informar o valor total da divida.1000
divida_inicial = float(input("Digite o valor total da dívida: "))

print(
    f"Total: R$ {divida_inicial:.2f} Juros: R$   0.00 Numero parcelas: 1 Valor Parcela: "
    f"R$ {divida_inicial}")

taxa_juros = 1.10
for parcelas in range(3, 13, 3):
    valor_total = divida_inicial * taxa_juros
    valor_juros = valor_total - divida_inicial
    valor_parcelas = valor_total / parcelas
    taxa_juros += 0.05
    print(f"Total: R$ {valor_total:.2f} Juros: R$ {valor_juros:.2f} Número parcelas: "
          f"{parcelas} Valor Parcela: R$ {valor_parcelas:.2f}")
