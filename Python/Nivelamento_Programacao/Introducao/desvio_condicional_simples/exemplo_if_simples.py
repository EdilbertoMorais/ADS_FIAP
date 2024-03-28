# Solicita ao usuário que informe seu RM e sua idade
rm = input("Por favor, informe seu RM: ")
idade = int(input("Por favor, informe sua idade: "))

# Verifica se a idade é maior ou igual a 18
if int(idade) >= 18:
    # Se a idade for maior ou igual a 18, imprime a mensagem de participação autorizada
    print(f"Sua participação foi autorizada, aluno de RM {rm}\n"
          "Mais instruções serão enviadas via e-mail.")
