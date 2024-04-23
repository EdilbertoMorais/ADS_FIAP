def chamarMenu():
    try:
        escolha = int(input("""
        Escolha uma opção do Menu:
        <1> Para Registrar Ativo.
        <2> Para Persistir em Arquivo.
        <3> Para Exibir Ativos Armazenados.
        Ou escolha qualquer outro número para SAIR
        Digite sua escolha: """))
        return escolha
    except ValueError:
        print("Informe apenas números.")
        return chamarMenu()


def registrar(dicionario):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar.").upper()


def persistir(dicionario):
    with open("/home/edilberto/projetos/ADS_FIAP/Nano_Courses/Python/Arquivos/inventario"
              ".csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" +
                      valor[1] + ";" + valor[2] + "\n")
    return "Persistido com sucesso"


def exibir():
    with open("/home/edilberto/projetos/ADS_FIAP/Nano_Courses/Python/Arquivos/inventario"
              ".csv", "r") as inv:
        linhas = inv.readlines()
    return linhas
