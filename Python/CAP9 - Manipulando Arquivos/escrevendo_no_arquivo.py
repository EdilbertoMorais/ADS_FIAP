conteudo = "\nAdicionando uma QUINTA linha de teste no arquivo, já criado."

arquivo = open("/home/edilberto/projetos/ADS_FIAP/Python/Arquivos para Manipular/teste.txt",
               "a", encoding="UTF-8")
print(arquivo.writable())
arquivo.write(conteudo)
arquivo.close()

arquivo = open("/home/edilberto/projetos/ADS_FIAP/Python/Arquivos para Manipular/teste.txt",
               encoding="UTF-8")
print(arquivo.read())
arquivo.close()
