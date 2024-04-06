numero = 1

while numero % 2 != 0:
    numero = int(input("Digite um numero par: "))
print("Parabens o número digitado é par!")


# Solicitar 10 números inteiros e contar quantos desses numeros são pares

cont = 0                                    # contadora (a quantidade de repetições)
conta_par = 0                               # contadora (a quantidade de números pares digitados)

while cont < 10:
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:                     # verifica se o numero é par
        conta_par += 1
    cont += 1

print(f'Quantidade de Pares: {conta_par}')


# Exibir todos os numeros inteiros pares de 1 até 10

cont = 10

while cont <= 20:
    print(cont)
    cont += 2


