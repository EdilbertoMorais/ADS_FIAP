# importando a biblioteca socket
import socket
# variável criada para controlar o laço do while
resp = "S"
while (resp == "S"):
    # Variável url criada para armazenar o domínio que vamos buscar
    url = input("Digite uma url: ")
    # Variável ip criada para armazenar o retorno do método gethostbyname().
    ip = socket.gethostbyname(url)
    print("O IP referente à url informada é: ", ip)
    resp = input("Digite <s> para continuar: ").upper()
