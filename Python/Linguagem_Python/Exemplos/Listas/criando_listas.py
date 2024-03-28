# criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
# exibindo a lista com um print
print("exibindo a lista completa")
print(jedi)
# exibindo um valor específico da lista
print("exibindo um valor específico")
print(jedi[2])
# incluíndo um item no início da lista
print("incluíndo um item no final da lista")
jedi.append("Mace Windu")
# Solicitando ao usuário que informe um valor para incluir na lista.
jedi.append(input("Informe o nome de um jedi: "))
# Incluindo um valor em uma posição específica da lista
jedi.insert(5, "Luminara")
# Incluindo um valor pelo usuário em uma posição específica da lista
jedi.insert(5, input("Informe o nome de um jedi: "))
# A variável nome assumirá cada um dos valores da lista a cada looping
print("Exibindo um nome por vez:")
# Para removermos um valor da última posição da lista
# jedi.pop()
# Para removermos um valor específico da lista basta informar o indice dentro do pop
# jedi.pop(5)
# O método remove permite removermos um valor específico da lista
jedi.remove("Dart")



# A função enumerate atribui a variavel indice o número do indice da lista jedi, podendo ser impresso depois para melhorar a apresentação
for indice, nome in enumerate(jedi):
    # para cada volta do loop, exibir o valor assumido
    print(f" O indice {[indice]} é o {nome}")
