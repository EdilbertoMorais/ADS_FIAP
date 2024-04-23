def perguntar():
    resposta = input("""O que deseja realizar?
 <I> - Para Inserir um usuário
 <P> - Para Pesquisar um usuário
 <E> - Para Excluir um usuário
 <L> - Para Listar um usuário: """).upper()
    return resposta


def inserir(dicionario):
    dicionario[input("Digite o ID do colaborador: ").upper()] = \
        [input("Digite o login: ").upper(),
         input("Digite o nome: ").upper(),
         input("Digite a última data de acesso: "),
         input("Digite a hora do último acesso: "),
         input("Qual a última estação acessada: ").upper()]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is not None:
        print("Login..........: " + lista[0])
        print("Nome...........: " + lista[1])
        print("Último acesso..: " + lista[2])
        print("Hora do acesso.: " + lista[3])
        print("Última estação.: " + lista[4])


def excluir(dicionario, chave):
    if dicionario.get(chave) is not None:
        del dicionario[chave]
    print("Registro Eliminado")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("ID: ", chave)
        print("Dados: ", valor)
