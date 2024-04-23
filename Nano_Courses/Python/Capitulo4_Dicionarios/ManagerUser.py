from Python.Funcoes.Funcoes_Dicionarios import *

usuarios = {
    "1": ["Chaves".upper(), "Chaves Silva".upper(), "17/06/1975", "18:00:00", "Recep_01".upper()],
    "2": ["Quico".upper(), "Enrico Flores".upper(), "03/06/1976", "19:00:00", "Raiox_02".upper()],
    "3": ["Chiquinha".upper(), "Francisca do Choro".upper(), "21/06/1986", "20:00:00",
          "Raiox_03".upper()],
    "4": ["Florinda".upper(), "Florinda Flores".upper(), "26/11/2017", "21:00:00",
          "Recep_01".upper()]}

opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    # if opcao == "I":
    #     inserir(usuarios)
    # if opcao == "P":
    #     pesquisar(usuarios, input("Qual ID deseja pesquisar? ").upper())
    # if opcao == "E":
    #     excluir(usuarios, input("Qual ID deseja excluir? ").upper())
    # if opcao == "L":
    #     listar(usuarios)
    # opcao = perguntar()

    # Usando o match case no lugar do if encadeado
    match opcao:
        case "I":
            inserir(usuarios)
        case "P":
            pesquisar(usuarios, input("Qual ID deseja pesquisar? ").upper())
        case "E":
            excluir(usuarios, input("Qual ID deseja excluir? ").upper())
        case "L":
            listar(usuarios)
    opcao = perguntar()

