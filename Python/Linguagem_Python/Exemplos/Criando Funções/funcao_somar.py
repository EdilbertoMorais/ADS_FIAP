def somar(valorA, valorB):
    soma = valorA + valorB
    # print(f"A soma entre {valorA} e {valorB} é igual a {soma}") # Isso limita o uso da função.
    return soma


valor1 = int(input("Informe um valor para soma: "))
valor2 = int(input("Informe um outro valor para soma: "))

print(F"{valor1} + {valor2} = {somar(valor1, valor2)}")
