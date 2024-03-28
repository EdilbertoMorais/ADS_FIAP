# Minha resposta:
peso_total = 0
for i in range(1, 11):
    peso = float(input('Informe o peso da caixa: '))
    peso_total = peso_total + peso
media_peso = peso_total / 10
print(f"O peso total é de ")
print(f"Peso total {peso_total:.2f}kg. A média por volume é {media_peso:.2f}kg")

# Resposta do professor:
# # variavel para armazenar o peso total das caixas
# peso_total = 0.0
# # loop para repetir por 10 vezes a solicitação de peso
# for x in range(1, 10):
#     # para cada volta do loop, solicitar o peso da caixa
#     peso_atual = float(input("Informe o peso da caixa atual:"))
#     # para cada peso solicitado, somar ao peso total
#     peso_total = peso_total + peso_atual
# # ao final do loop, calcular a média aritmética
# media = peso_total / 10
# # exibição dos resultados!
# print(f"O peso total de caixas é {peso_total}.A média de peso é {media}")
