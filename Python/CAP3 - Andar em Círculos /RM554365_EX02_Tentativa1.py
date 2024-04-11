"""2 – A compra de um veículo pode ser realizada parcelada. Crie um programa que receba o valor
de um carro e mostre uma tabela com os seguintes dados: preço final, quantidade de parcelas e
valor da parcela. Considere o seguinte:

a) O preço final para compra à vista tem um desconto de 20%:

b) A quantidade de parcelas pode ser 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60:

Os percentuais de acréscimo seguem na tabela abaixo:

quantidade de parcelas                               % de acréscimo sobre o preço final
6 parcelas                                           3%
12 parcelas                                          6%
18 parcelas                                          9%
24 parcelas                                          12%
30 parcelas                                          15%
36 parcelas                                          18%
42 parcelas                                          21%
48 parcelas                                          24%
54 parcelas                                          27%
60 parcelas                                          30%

"""

# Solicitar o valor do carro ao usuário
valor_total_carro = float(input("Digite o valor do carro: "))

# Preço final para compra à vista com desconto de 20%
valor_carro_a_vista = valor_total_carro * 0.8

# Imprime o preço final à vista
print(f"O preço final á vista com desconto de 20% é: R$ {valor_carro_a_vista:.2f}")

# Imprime as condições de parcelamento com o acrescimo dos juros conforme tabela.
juros = 1.03
for parcelas in range(6, 61, 6):
    if parcelas == 6:
        juros = 1.03
        valor_total_carro_com_juros = valor_total_carro * juros
        valor_juros = valor_total_carro_com_juros - valor_total_carro
        valor_parcelas = valor_total_carro_com_juros / parcelas
        print(
            f"O preço final parcelado em  {parcelas}X é de R$ {valor_total_carro_com_juros:.2f} com "
            f"parcelas de R${valor_parcelas:.2f}")
    elif parcelas == 12:
        juros = 1.06
        valor_total_carro_com_juros = valor_total_carro * juros
        valor_juros = valor_total_carro_com_juros - valor_total_carro
        valor_parcelas = valor_total_carro_com_juros / parcelas
        print(
            f"O preço final parcelado em {parcelas}X é de R$ {valor_total_carro_com_juros:.2f} com "
            f"parcelas de R${valor_parcelas:.2f}")
    elif parcelas == 18:
        juros = 1.09
        valor_total_carro_com_juros = valor_total_carro * juros
        valor_juros = valor_total_carro_com_juros - valor_total_carro
        valor_parcelas = valor_total_carro_com_juros / parcelas
        print(
            f"O preço final parcelado em {parcelas}X é de R$ {valor_total_carro_com_juros:.2f} com "
            f"parcelas de R${valor_parcelas:.2f}")
    elif parcelas == 24:
        juros = 1.12
        valor_total_carro_com_juros = valor_total_carro * juros
        valor_juros = valor_total_carro_com_juros - valor_total_carro
        valor_parcelas = valor_total_carro_com_juros / parcelas
        print(
            f"O preço final parcelado em {parcelas}X é de R$ {valor_total_carro_com_juros:.2f} com "
            f"parcelas de R${valor_parcelas:.2f}")
    elif parcelas == 30:
        juros = 1.15
        valor_total_carro_com_juros = valor_total_carro * juros
        valor_juros = valor_total_carro_com_juros - valor_total_carro
        valor_parcelas = valor_total_carro_com_juros / parcelas
        print(
            f"O preço final parcelado em {parcelas}X é de R$ {valor_total_carro_com_juros:.2f} com "
            f"parcelas de R${valor_parcelas:.2f}")
    elif parcelas == 36:
        juros = 1.18
        valor_total_carro_com_juros = valor_total_carro * juros
        valor_juros = valor_total_carro_com_juros - valor_total_carro
        valor_parcelas = valor_total_carro_com_juros / parcelas
        print(
            f"O preço final parcelado em {parcelas}X é de R$ {valor_total_carro_com_juros:.2f} com "
            f"parcelas de R${valor_parcelas:.2f}")
    elif parcelas == 42:
        juros = 1.21
        valor_total_carro_com_juros = valor_total_carro * juros
        valor_juros = valor_total_carro_com_juros - valor_total_carro
        valor_parcelas = valor_total_carro_com_juros / parcelas
        print(
            f"O preço final parcelado em {parcelas}X é de R$ {valor_total_carro_com_juros:.2f} com "
            f"parcelas de R${valor_parcelas:.2f}")
    elif parcelas == 48:
        juros = 1.24
        valor_total_carro_com_juros = valor_total_carro * juros
        valor_juros = valor_total_carro_com_juros - valor_total_carro
        valor_parcelas = valor_total_carro_com_juros / parcelas
        print(
            f"O preço final parcelado em {parcelas}X é de R$ {valor_total_carro_com_juros:.2f} com "
            f"parcelas de R${valor_parcelas:.2f}")
    elif parcelas == 54:
        juros = 1.27
        valor_total_carro_com_juros = valor_total_carro * juros
        valor_juros = valor_total_carro_com_juros - valor_total_carro
        valor_parcelas = valor_total_carro_com_juros / parcelas
        print(
            f"O preço final parcelado em {parcelas}X é de R$ {valor_total_carro_com_juros:.2f} com "
            f"parcelas de R${valor_parcelas:.2f}")
    elif parcelas == 60:
        juros = 1.30
        valor_total_carro_com_juros = valor_total_carro * juros
        valor_juros = valor_total_carro_com_juros - valor_total_carro
        valor_parcelas = valor_total_carro_com_juros / parcelas
        print(
            f"O preço final parcelado em {parcelas}X é de R$ {valor_total_carro_com_juros:.2f} com "
            f"parcelas de R${valor_parcelas:.2f}")
