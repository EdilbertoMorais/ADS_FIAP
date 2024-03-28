# Faixa de bonus
# > 1000 3gb
# > 500 1.5gb
# > 200 500mb
# < 200 nenhum bonus

pontos_cliente = int(input('Insira a pontuação do cliente: '))

if pontos_cliente >= 1000:
    print(f'Pontuação: {pontos_cliente} - Bonus: 3gb')
elif pontos_cliente >= 500:
    print(f'Pontuação: {pontos_cliente} - Bonus: 1,5gb')
elif pontos_cliente >= 200:
    print(f'Pontuação: {pontos_cliente} - Bonus: 500mb')
else:
    print(f'Pontuação: {pontos_cliente} - nenhum bonus concedido')
