"""Criar um algoritmo que receba o tipo de assinatura do cliente o faturamento anual dele e que
calcule e exiba o qual valor de bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a
porcentagem de acordo com cada nível de assinatura:

Basic       30%
Silver      20%
Gold        10%
Platinum    5%
"""
bonus = 0
assinatura = int(input("""Informe o tipo de assinatura: 
[1] Basic
[2] Silver
[3] Gold
[4] Platinum
Escolha uma das assinaturas acima: """))

faturamento = float(input("Informe o faturamento anual do canal:"))

if assinatura == 1:
    bonus = faturamento * 0.3
elif assinatura == 2:
    bonus = faturamento * 0.2
elif assinatura == 3:
    bonus = faturamento * 0.1
elif assinatura == 4:
    bonus = faturamento * 0.05
else:
    print("Tipo de assinatura inválida!")

print(f"Valor total a pagar R$ {bonus:.2f}")
