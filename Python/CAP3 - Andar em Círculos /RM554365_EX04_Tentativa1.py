"""4 – Toda vez que um cliente realiza um resgate de uma aplicação financeira, o sistema deve
calcular a alíquota de imposto de renda (IR) que deve ser aplicada sobre aquele resgate,
considerando o número de dias que o valor permaneceu aplicado, conforme a tabela
abaixo:

Até 180 dias = alíquota de 22,5% de IR.
De 181 a 360 dias = alíquota de 20% de IR.
De 361 a 720 dias = alíquota de 17,5% de IR.
Acima de 720 dias = alíquota de 15% de IR.

É o que acontece, por exemplo, com o CDB - Certificado de Depósito Bancário, uma aplicação de
renda fixa comumente oferecida pelas Fintechs. Outros investimentos em renda fixa, como LCI e
LCA, respectivamente, Letra de Crédito Imobiliário e Letra de Crédito do Agronegócio são isentos
de imposto de renda. Escreva um programa que receba o tipo de investimento do qual se deseja
realizar um resgate (1 para CDB, 2 para LCI e 3 para LCA), o valor a ser resgatado e o número de
dias que esse valor permaneceu investido e, se for o caso, calcule o valor referente ao imposto
de renda.

Atenção! O programa deve consistir se o investimento fornecido é válido, ou seja, 1, 2 o 3.
"""

#  Solicita a entrada de dado do usuário e verifica se o tipo de investimento é valido.
while True:
    print("[1] para CDB")
    print("[2] para LCI")
    print("[3] para LCA")
    investimento = int(input("Digite o numero do investimento: "))

    if investimento > 0 and investimento < 4:
        break

#  Solicita ao usuário o valor total para resgate.
resgate = float(input("Digite o valor do resgate: "))

#  Solicita que o usuário informe o total de dias em que permaneceu o investimento.
dias_investidos = int(input("Informe o tempo aplicado no investimento: "))

#  Calcula a aliquota de IR com base no tempo em que o valor do resgate permaneceu aplicado.
if investimento == 1:
    if dias_investidos <= 180:
        aliquota_imposto = 22.5
        imposto_a_pagar = resgate * (aliquota_imposto / 100)
        print(f"O valor do IR a ser pago é de R$ {imposto_a_pagar:.2f}")
    elif 181 <= dias_investidos <= 360:
        aliquota_imposto = 20
        imposto_a_pagar = resgate * (aliquota_imposto / 100)
        print(f"O valor do IR a ser pago é de R$ {imposto_a_pagar:.2f}")
    elif 361 <= dias_investidos <= 720:
        aliquota_imposto = 17.5
        imposto_a_pagar = resgate * (aliquota_imposto / 100)
        print(f"O valor do IR a ser pago é de R$ {imposto_a_pagar:.2f}")
    else:
        aliquota_imposto = 15
        imposto_a_pagar = resgate * (aliquota_imposto / 100)
        print(f"O valor do IR a ser pago é de R$ {imposto_a_pagar:.2f}")
else:
    print("APLICAÇÃO ISENTA!")

