from Python.Funcoes.Funcoes_Arquivos import *

inventario = {}

opcao = chamarMenu()

while opcao > 0 and opcao < 4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:
            # Tudo isso pode ser substituído pela função split() linha 24
            # separacao = linha[linha.find(";") + 1:-1]
            # data = separacao[0:separacao.find(";")]
            # separacao = separacao[separacao.find(";") + 1:-1]
            # descricao = separacao[0:separacao.find(";")]
            # departamento = linha[linha.rfind(";") + 1:-1]
            # print("\nData.........: ", data)
            # print("Descrição....: ", descricao)
            # print("Departamento.: ", departamento)
            lista = linha.split(";")
            print(lista)
            print("Data.........: ", lista[1])
            print("Descrição....: ", lista[2])
            print("Departamento.: ", lista[3])
    opcao = chamarMenu()
