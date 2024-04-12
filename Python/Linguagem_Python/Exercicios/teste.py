valor_divida = float(input("Valor divida?"))

print(f"Total: R$ {valor_divida:.2f} Juros: R$   0.00 Numero parcelas: 1 Valor Parcela: "
      f"R$ {valor_divida}")

for parcelas in range(3, 13, 3):
    if parcelas == 3:
        juros = valor_divida * (10/100)
        parcela = round((valor_divida + juros) / 3, 2)
        print(f"Total: R$ {valor_divida + juros:.2f} Juros: R${juros} Numero "
              f"parcelas: {parcelas} Valor Parcela: R$ {parcela}")
    elif parcelas == 6:
        juros = valor_divida * (15/100)
        parcela = round((valor_divida + juros) / 6, 2)
        print(f"Total: R$ {valor_divida + juros:.2f} Juros: R${juros} Numero "
              f"parcelas: {parcelas} Valor Parcela: R$ {parcela}")
    elif parcelas == 9:
        juros = valor_divida * (20/100)
        parcela = round((valor_divida + juros) / 9, 2)
        print(f"Total: R$ {valor_divida + juros:.2f} Juros: R${juros} Numero "
              f"parcelas: {parcelas} Valor Parcela: R$ {parcela}")
    elif parcelas == 12:
        juros = valor_divida * (25/100)
        parcela = round((valor_divida + juros) / 12, 2)
        print(f"Total: R$ {valor_divida + juros:.2f} Juros: R${juros} Numero "
              f"parcelas: {parcelas} Valor Parcela: R$ {parcela}")
