rm = input("Insira seu RM: ")
idade = int(input("Insira sua idade: "))

if idade >= 18:
    print(f"Sua participação foi autorizada, aluno de RM {rm}\n"
          "Mais instruções serão enviadas via e-mail.")
else:
    print("Sua participação não foi autorizada devido sua idade.")
