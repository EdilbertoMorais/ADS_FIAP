# criando um dicionario vazio
dicionario = {}
# incluindo dados no dicionario
dicionario["André David"] = "Professor"
dicionario["Edilberto"] = "Estudante"
dicionario["Edilberto1"] = "Estudante1"

# Pedindo para o usuário incluir dados no dicionário
# nova_chave = input("Informe o nome do colaborador da FIAP")
# novo_valor = input("Informe a função do colaborador da FIAP")
# dicionario[nova_chave] = novo_valor
# exibindo o dicionário completo
for chave, valor in dicionario.items():
    print(f"O colaborador {chave} desempenha a função de {valor}")

# alterando dados no dicionário (Mesma estrutura usada para adicionar dados)
dicionario["André David"] = "Coordenador"
# exibindo o dicionário completo


# removendo dados de um dicionário usando o método pop() e informando a chave.
dicionario.pop("André David")

# removendo o último dado de um dicionário com o método popitem()
dicionario.popitem()

# removendo todos os dados de um dicionário com o método clear()
# dicionario.clear()

print("imprimindo dicionário após exclusão de dados:")
if dicionario:
    for chave, valor in dicionario.items():
        print(f"O colaborador {chave} desempenha a função de {valor}")
else:
    print("Dicionário está vazio.")
