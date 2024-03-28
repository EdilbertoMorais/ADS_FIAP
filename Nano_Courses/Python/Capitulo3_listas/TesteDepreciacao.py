print("################ APLICANDO DEPRECIAÇÃO ################")
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

depreciacao = input("Digite o nome do equipamento que será depreciado: ").upper()
for indice in range(0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print("Nome: ", equipamentos[indice])
        print("Valor antigo: ", valores[indice])
        valores[indice] = valores[indice] * 0.9
        print("Novo valor: ", valores[indice])

print("################ EXCLUINDO UM ITEM PELO INDICE ################")
serial = int(input("Digite o serial do equipamento que será excluído: "))
for indice in range(0, len(departamentos)):
    if seriais[indice] == serial:
        del departamentos[indice]
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]
        break

for indice in range(0, len(equipamentos)):
    print("    Equipamento..: ", (indice + 1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])
