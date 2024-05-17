# criando um dicionario vazio
dicionario = {}

# criando um dicionario com dados
dicionario = {"Yoda": "Mestre Jedi",
              "Mace Windu": "Mestre Jedi",
              "Anakin Skywalker": "Cavaleiro Jedi",
              "R2-D2": "Dróide",
              "Dex": "Balconista"}

# exibindo o tipo do dicionário
print(f"O objeto dicionário é do tipo {dicionario}")

# exibindo o valor associado a uma chave específica
print(dicionario["R2-D2"])

# exibindo o valor associado a uma chave específica
print(dicionario["R2-D2"])

# exibindo todos os valores em um dicionário
for valor in dicionario.values():
    print(valor)

# exibindo todas as chaves em um dicionário
for chave in dicionario.keys():
    print(chave)

# exibindo o dicionário completo
for chave, valor in dicionario.items():
    print(f"O personagem {chave} é da categoria {valor}")
