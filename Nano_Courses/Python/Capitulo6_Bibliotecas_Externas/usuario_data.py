import getpass
from datetime import datetime

# Retorna o usuário logado no momento.
print("Usuário.......: ".upper(), getpass.getuser())
# Os demais retornam o dado conforme descritivo.
print("Data Completa.: ".upper(), datetime.now())
print("Dia...........: ".upper(), datetime.now().day)
print("Mês...........: ".upper(), datetime.now().month)
print("Ano...........: ".upper(), datetime.now().year)
print("Hora..........: ".upper(), datetime.now().hour)
print("Minuto........: ".upper(), datetime.now().minute)
print("Segundo.......: ".upper(), datetime.now().second)

#  Outro exemplo de como usar o getpass()

usuario = input("Digite o usuário: ").upper()
senha = getpass.getpass("Digite a senha: ")

if usuario == "TESTE" and senha == "12345":
    print("Usuário logado")
else:
    print("Login Negado")
