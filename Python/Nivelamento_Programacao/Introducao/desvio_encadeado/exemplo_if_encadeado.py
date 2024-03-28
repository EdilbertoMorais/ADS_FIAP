rm = int(input("Insira seu RM: "))
idade = int(input("Insira sua idade: "))

if idade >= 18:
    print(f"Sua participação foi autorizada, aluno de RM {rm}\n"
          "Mais instruções serão enviadas via e-mail.")
else:
    autorizado = input("Você possui autorização dos seus responsáveis "
                       "para participar? S=SIM ou N=Não: ").upper()
    if autorizado == "S":
        print(f"Sua participação foi autorizada, aluno de RM {rm}\n"
              "Mais instruções serão enviadas via e-mail.")
    else:
        print("Sua participação não foi autorizada devido sua idade.")
