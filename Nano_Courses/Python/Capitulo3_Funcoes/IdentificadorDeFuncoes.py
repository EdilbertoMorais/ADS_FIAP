# Criando a primeira função chamada de preencherInventario()
def preencherInventario(lista):
    resposta = ""
    while resposta == "":
        equipamento = [input("Equipamento: ").upper(),
                       float(input("Valor: ")),
                       int(input("Número Serial: ")),
                       input("Departamento: ").upper()]
        lista.append(equipamento)
        resposta = input("Digite ENTER para continuar ou \"S\" para SAIR: ").upper()


# Criando a função chamada de exibirInventario()
def exibirInventario(lista):
    for elemento in lista:
        print("\nNome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.: ", elemento[3])


# Criando a funçao de buscarItemInventario(nomeItem)
def localizarPorNome(lista):
    buscar_item = input("Informe o nome do item que deseja localizar: ").upper()
    for elemento in lista:
        if buscar_item == elemento[0]:
            print("Valor..: ", elemento[1])
            print("Serial.:", elemento[2])


# Criando a função depreciarPorNome(lista, percentual)
def depreciarPorNome(lista, percentual):
    nome_item = input("Informe o nome do item que deseja depreciar: ").upper()
    for elemento in lista:
        if nome_item == elemento[0]:
            elemento[1] = elemento[1] * (1 - percentual / 100)
            print("Novo valor: ", elemento[1])


# Criando a função excluirPorSerial(lista):
def excluirPorSerial(lista):
    serial = int(input("Informe o serial do item que deseja excluir: "))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    return "Itens Excluídos com Sucesso!"


# Criando a função resumirValores(lista):
def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))
