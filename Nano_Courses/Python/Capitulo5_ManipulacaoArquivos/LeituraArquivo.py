with open("/home/edilberto/projetos/ADS_FIAP/Nano_Courses/Python/Arquivos/pagina.html",
          "r") as arquivo:
    conteudo = arquivo.readlines()
print("Tipo de dado da variável", type(conteudo))
print("Conteúdo do arquivo:", conteudo)
