with open(
        "/home/edilberto/projetos/ADS_FIAP/Nano_Courses/Python/Arquivos/economic-indicators.csv",
        "r") as boston_arquivo:
    # Instanciando as variáveis que serão usadas
    total_voos = 0
    maior = 0
    total_passageiros = 0
    maior_media_diaria = 0
    # Solicitando ao usuário que informe o ano para pesquisa
    ano_usuario = input("Qual ano deseja pesquisar? ")
    # Iterando o arquivo iniciando na linha 2 e convertendo os dados para uma lista com a função
    # split()
    for linha in boston_arquivo.readlines()[1:-1]:
        lista = linha.split(",")
        # Atribuindo a variável total_voos a soma dos voos partindo de Boston no ano de 2014
        if lista[0] == "2014":
            total_voos += int(lista[3])
        # Comparando o valor do elemento do índice 2 da lista com a variável maior
        if int(lista[2]) > int(maior):
            # Caso seja True, a variável maior recebe o valor do elemento de índice 2
            maior = lista[2]
            # A variável ano recebe o valor do elemento de índice 0
            ano = lista[0]
            # A variável mes recebe o valor do elemento de índice 1
            mes = lista[1]
        # Comparando o ano informado pelo usuário com o do arquivo
        if ano_usuario == lista[0]:
            # Atribuindo a variável total_passageiros a soma dos passageiros no ano informado pelo
            # usuário
            total_passageiros = total_passageiros + int(lista[2])
            # Compara se o elemento da lista de índice 5 é maior do que o valor da variável criada
            # para capturar o elemento de maior valor
            if float(lista[5]) > float(maior_media_diaria):
                # Se o valor do elemento de índice 5 for maior, a variável maior_media_diaria
                # recebe o valor do elemento de índice 5
                maior_media_diaria = lista[5]
                # E a variável mes_maior_diaria recebe o valor do elemento de índice 1
                mes_maior_diaria = lista[1]
    # Imprime os resultados esperados
    print(f"O total de voos que partiram de Boston em 2014 doi de {total_voos}")
    print(f"O mês/ano de maior movimento no aeroporto foi {str(mes)}/{str(ano)}")
    print(f"O total de passageiros do ano de {ano_usuario} foi de {total_passageiros}")
    print(f"O mês do ano de {ano_usuario} com maior média para diária de hotel foi: "
          f"{mes_maior_diaria}")
