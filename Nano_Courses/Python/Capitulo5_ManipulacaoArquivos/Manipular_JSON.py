from Python.Funcoes.Funcoes_JSON import *

inventario = ler_arquivo("inventario_json.json")

opcao = chamarMenu()

while opcao > 0 and opcao < 3:
    if opcao == 1:
        print(registrar(inventario,
                        "/home/edilberto/projetos/ADS_FIAP/Nano_Courses/Python/Arquivos/"
                        "inventario_json.json"))
    elif opcao == 2:
        exibir("/home/edilberto/projetos/ADS_FIAP/Nano_Courses/Python/Arquivos/"
               "inventario_json.json")
    opcao = chamarMenu()
