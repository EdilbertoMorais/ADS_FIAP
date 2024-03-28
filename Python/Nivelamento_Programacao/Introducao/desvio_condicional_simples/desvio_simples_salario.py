# Pedir que o usuário digite o nome do funcionário:
nome = input("Informe o nome do funcionário: ")
# Pedir que o usuário digite o salário do funcionário:
salario = float(input("informe o salário do funcionário: "))
# Caso o salário sejá negativo, alertar o usuário:
if salario < 0:
    # salario = salario * -1  # Calculo que converte número negativo em positivo.
    salario = abs(salario)  # Função que converte um valor negativo em positivo.
    print("ATENÇÃO, o salário informado é negativo, estamos corrigindo o valor.")
# Exibir o salário armazenado:
print(f"O salário do funcionário {nome} com valor de R${salario}, foi armazenado com sucesso.")
