with open("/home/edilberto/projetos/ADS_FIAP/Nano_Courses/Python/Arquivos/pagina.html",
          "w") as pagina:
    pagina.write("<meta charset='UTF-8'>")
    pagina.write("<body> <h1> Este é um teste para página WEB </h1>")
    pagina.write("<br><h2> Abaixo seguem alguns nomes importantes para o projeto:  </h2>")
    pagina.write("<h3>")
    nome = ""
    while nome != "SAIR":
        nome = input("Digite um nome ou SAIR: ").upper()
        if nome != "SAIR":
            pagina.write("<br>" + nome)
    pagina.write("</h3></body>")
