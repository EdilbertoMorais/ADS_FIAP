# Implementar uma calculadora (soma, subtração, multiplicação, divisão)

while True:
    a = float(input('Digite um numero: '))
    b = float(input('Digite outro numero: '))

    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Finalizar')
    opcao = int(input('Escolha uma das opções acima: '))

    if opcao == 1:
        print(f'Resultado da soma: {a + b}')
    elif opcao == 2:
        print(f'Resultado da subtração: {a - b}')
    elif opcao == 3:
        print(f'Resultado da multiplicação: {a * b}')
    elif opcao == 4:
        print(f'Resultado da divisão: {a / b}')
    elif opcao == 5:
        print('Fim do programa')
        break                                   # finaliza uma estrutura de repetição
    else:
        print('Opção inválida')
