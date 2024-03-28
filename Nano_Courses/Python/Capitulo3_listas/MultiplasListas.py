# equipamentos = []
# valores = []
# seriais = []
# departamentos = []
# resposta = "S"
# while resposta == "S":
#     equipamentos.append(input("Equipamento: "))
#     valores.append(float(input("Valor: ")))
#     seriais.append(int(input("Número Serial: ")))
#     departamentos.append(input("Departamento: "))
#     resposta = input("Digite 'S' para continuar: ").upper()
#
# for equipamento in equipamentos:
#     print("Equipamento: ", equipamento)

print("################ OUTRO EXEMPLO ################")
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: ").upper())
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: ").upper())
    resposta = input("Digite 'S' para continuar: ").upper()

for indice in range(0, len(equipamentos)):
    print("Equipamento..: ", (indice + 1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])

busca = input("Digite o nome do equipamento que deseja buscar: ").upper()
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Nome..: ", valores[indice])
        print("Valor..: ", valores[indice])
        print("Serial.:", seriais[indice])
