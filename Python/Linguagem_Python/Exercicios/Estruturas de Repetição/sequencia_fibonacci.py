# Solicita ao usuário um número
numero_usuario = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))

# Inicializa os primeiros números da sequência de Fibonacci
a, b = 0, 1

# Verifica se o número está na sequência de Fibonacci
for i in range(1, numero_usuario + 1):
    # a, b = b, a + b
    # Seria o mesmo que fazer o que esta abaixo na linha 13
    c = a + b
    a = b
    b = c
    if numero_usuario == c:
        print(f"O número {numero_usuario} ESTÁ na sequência de Fibonacci")
        break
    elif numero_usuario < c:
        print(f"O número {numero_usuario} NÃO está na sequência de Fibonacci")
        break
