# Adicionando dados a  lista
inventario = []
resposta = "S"
while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar ou qualquer outra para sair: ").upper()

# Imprimindo os dados da lista com o uso do for
for elemento in inventario:
    print(elemento)
    
