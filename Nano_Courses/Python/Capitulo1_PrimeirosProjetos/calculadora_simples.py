# Algoritmo "Calculadora Simples"
# // Descrição: Calcula o valor de 2 numeros! (função)
# // Autor(a)    : Edilberto Morais
# // Data atual: 15-03-2024
# Var
# valor1, valor2, soma, divisao, subtracao, multiplicacao: real
#
# Inicio
#
#     Escreva("Digite o primeiro valor: ")
#     Leia(valor1)
#     Escreva("Digite o segundo valor: ")
#     Leia(valor2)
#     soma <- valor1 + valor2
#     Escreval("A soma é:", soma)
#     divisao <- valor1 / valor2
#     Escreval("A divisão é:", divisao)
#     subtracao <- valor1 - valor2
#     Escreval("A subtração é:", subtracao)
#     multiplicacao <- valor1 * valor2
#     Escreval("A multiplicação é:", multiplicacao)
#
# Fimalgoritmo

# print("Calcula o valor de 2 numeros!")
# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# soma = valor1 + valor2
# print(f"A soma é: {soma}")
# subtracao = valor1 - valor2
# print(f"A subtração é: {subtracao}")
# divisao = valor1 / valor2
# print(f"A divisao é: {divisao}")
# multiplicacao = valor1 * valor2
# print(f"A multiplicação é: {multiplicacao}")

# Aplicando a conversão do tipo adequado para cada operação aritmetica
valor1 = input("Por favor, digite o primeiro valor: ")
valor2 = input("Por favor, digite o segundo valor: ")
soma = float(valor1) + float(valor2)
print("A soma entre os valores é {}".format(soma))
subtracao = float(valor1) - float(valor2)
print("A subtração entre os valores é {}".format(subtracao))
divisao = float(valor1) / float(valor2)
print("A divisão entre os valores é {}".format(divisao))
multiplicacao = float(valor1) * float(valor2)
print("A multiplicação entre os valores é {}".format(multiplicacao))
