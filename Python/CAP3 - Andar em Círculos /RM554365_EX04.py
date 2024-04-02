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
import sys

#  Solicita a entrada de dado do usuário e verifica se o tipo de investimento é valido.
while True:
    tipo_investimento = int(input("""Informe o tipo de investimento que deseja resgatar:
[1] para CDB
[2] para LCI
[3] para LCA
[0] para SAIR da aplicação
Digite o número referente ao investimento: """))

    if tipo_investimento not in [0, 1, 2, 3]:
        print("\nOpção Invalida!\n")
    elif tipo_investimento == 0:
        print("\nFim do programa!")
        sys.exit()
    else:
        break

#  Solicita ao usuário o valor total para resgate.
valor_resgate = float(input("Digite o valor do resgate: "))

#  Solicita que o usuário informe o total de dias em que permaneceu o investimento.
tempo_do_investimento = int(input("Informe o tempo aplicado no investimento: "))

#  Calcula a aliquota de IR com base no tempo em que o valor do resgate permaneceu aplicado.
aliquota_ir = 0
if tempo_do_investimento <= 180:
    aliquota_ir = 22.5
elif 181 <= tempo_do_investimento <= 360:
    aliquota_ir = 20
elif 361 <= tempo_do_investimento <= 720:
    aliquota_ir = 17.5
else:
    aliquota_ir = 15

#  Imprime as informações de tipo de investimento, valor do resgate, e IR a pagar.
print("\n########### RESUMO DO RESGATE APLICAÇÃO ###########")

match tipo_investimento:
    case 1:
        print("Tipo Investimento definido: CDB")
    case 2:
        print("Tipo Investimento definido: LCI")
    case 3:
        print("Tipo Investimento definido: LCA")

print(f"Valor total para resgate: R$ {valor_resgate:.2f}")

print("\n                   TAXAS / TRIBUTOS                 ")
if tipo_investimento == 1:
    valor_ir = valor_resgate * (aliquota_ir / 100)
    print(f"O valor do IR a ser pago é de R$ {valor_ir:.2f}")
else:
    print("APLICAÇÃO ISENTA!")
