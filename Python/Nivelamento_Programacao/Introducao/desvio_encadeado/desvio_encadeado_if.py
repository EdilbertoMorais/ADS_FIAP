# Faixa de bonus
# > 1000 3gb
# > 500 1.5gb
# > 200 500mb
# < 200 nenhum bonus


pontos = int(input("Informe a pontuação do cliente: "))

if pontos >= 1000:
    print(f"Pontuação: {pontos} - Bonus: 3gb")
else:
    if pontos >= 500:
        print(f"Pontuação: {pontos} - Bonus: 1.5gb")
    else:
        if pontos >= 200:
            print(f"Pontuação: {pontos} - Bonus: 500mb")
        else:
            print(f"Pontuação: {pontos} - Nenhum bonus concedido.")
