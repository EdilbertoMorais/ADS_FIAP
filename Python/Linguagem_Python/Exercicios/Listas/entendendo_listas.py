lista_instrumentos = ["Bateria", "Guitarra", "Violão", "Guitarra", "Baixo", "Microfone"]

print(lista_instrumentos)

# Qual é o tamanho da minha lista?
print(len(lista_instrumentos))

# Quantas vezes o elemento "Guitarra" aparece na lista?
print(lista_instrumentos.count("Guitarra"))

# Como alterar a ordem dos elementos da lista?
lista_instrumentos.reverse()
print(lista_instrumentos)

# Ordenando em ordem crescente (para colocar em ordem decrescente, basta usar o reverse=True)
lista_instrumentos.sort(reverse=True)
print(lista_instrumentos)
