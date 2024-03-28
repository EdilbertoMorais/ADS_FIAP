total_calorias = 0

qtda_alimentos = int(input("informe o total de alimentos: "))

for i in range(1, qtda_alimentos + 1):
    calorias = int(input(f"Informe o valor calórico do {i}º alimento: "))
    total_calorias = total_calorias + calorias
print(f"O total de calorias consumidos foi de {total_calorias} calorias"
      f" para um total de {qtda_alimentos} alimentos")
