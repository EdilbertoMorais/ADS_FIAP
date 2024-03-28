"""
Criar um algoritmo que receba o VALOR BRUTO do pacote de viagem, a CATEGORIA DOS ASSENTOS no voo
e a QUANTIDADE DE VIAJANTES que moram em uma mesma casa e calcule os descontos conforme
a tabela abaixo:

Econômica:          2 viajantes 3%
                    3 viajantes 4%
                    4 viajantes ou mais 5%
Executiva:          2 viajantes 5%
                    3 viajantes 7%
                    4 viajantes ou mais 8%
Primeira Classes:   2 viajantes 10%
                    3 viajantes 15%
                    4 viajantes ou mais 20%

Exibir o valor BRUTO DA VIAGEM, o VALOR DO DESCONTO, o VALOR LÍQUIDO, o VALOR MEDIO POR VIAJANTE.
"""

valor_bruto = float(input("Informe o valor total da VIAGEM: "))
categoria = int(input("""Escolha a opção de categoria:
[1] Econômica
[2] Executiva
[3] Primeira Classes
Informe a categoria: """))
qtda_viajantes = int(input("Informe a quantidade de viajantes: "))
valor_desconto = 0
if categoria == 1:
    if qtda_viajantes == 2:
        valor_desconto = valor_bruto * 0.03
    elif qtda_viajantes == 3:
        valor_desconto = valor_bruto * 0.04
    elif qtda_viajantes >= 4:
        valor_desconto = valor_bruto * 0.05
elif categoria == 2:
    if qtda_viajantes == 2:
        valor_desconto = valor_bruto * 0.05
    elif qtda_viajantes == 3:
        valor_desconto = valor_bruto * 0.07
    elif qtda_viajantes >= 4:
        valor_desconto = valor_bruto * 0.08
elif categoria == 3:
    if qtda_viajantes == 2:
        valor_desconto = valor_bruto * 0.1
    elif qtda_viajantes == 3:
        valor_desconto = valor_bruto * 0.15
    elif qtda_viajantes >= 4:
        valor_desconto = valor_bruto * 0.2
else:
    print("Categoria Inexistente! Sem desconto concedido.")

valor_liquido = valor_bruto - valor_desconto
valor_media = valor_liquido / qtda_viajantes

print("############# RESUMO #############")
print(F"Valor Total da viagem R${valor_bruto:.2f}")
print(F"Valor do desconto R${valor_desconto:.2f}")
print(F"Valor Líquido a pagar R${valor_liquido:.2f}")
print(F"Valor médio por viajante R${valor_media:.2f}")


# Refatorando o código com o uso de um dicionario:
# Definindo os descontos e valores líquidos para cada categoria e quantidade de viajantes
# categorias = {
#     1: {2: (3, 0.97), 3: (4, 0.96), 'mais_de_3': (5, 0.95)},
#     2: {2: (5, 0.95), 3: (7, 0.93), 'mais_de_3': (8, 0.92)},
#     3: {2: (10, 0.9), 3: (15, 0.85), 'mais_de_3': (20, 0.8)}
# }
# # Entrada de dados
# valor_total = float(input("Informe o valor total da VIAGEM: "))
# categoria = int(input("""Escolha a opção de categoria:
# [1] Econômica
# [2] Executiva
# [3] Primeira Classe
# Informe a categoria: """))
# qtda_viajantes = int(input("Informe a quantidade de viajantes: "))
#
# # Obtendo os descontos e valores líquidos da estrutura de dados
# if qtda_viajantes == 2:
#     desconto, percentual = categorias[categoria][2]
# elif qtda_viajantes == 3:
#     desconto, percentual = categorias[categoria][3]
# elif qtda_viajantes > 3:
#     desconto, percentual = categorias[categoria]['mais_de_3']
# else:
#     desconto, percentual = 0, 1  # Se houver apenas um viajante, nenhum desconto é aplicado
# # Calculando valores
# valor_desconto = (valor_total * desconto) / 100
# valor_liquido = valor_total * percentual
# if qtda_viajantes == 1:  # Corrigindo o cálculo para 1 viajante
#     valor_media = valor_liquido
# else:
#     valor_media = valor_liquido / qtda_viajantes
# # Exibindo o resumo
# print("############# RESUMO #############")
# print(f"Valor Total da viagem R${valor_total:.2f}")
# print(f"Valor do desconto R${valor_desconto:.2f}")
# print(f"Valor Líquido a pagar R${valor_liquido:.2f}")
# print(f"Valor médio por viajante R${valor_media:.2f}")
