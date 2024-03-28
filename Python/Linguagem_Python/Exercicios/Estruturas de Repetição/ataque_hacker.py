senha = "LIBERDADE"
minutos = int(input("Informe os minutos atuais: "))
fatorial = 1

for i in range(1, minutos + 1):
    fatorial = fatorial * i
print(f"A senha é : {senha}{fatorial}")
