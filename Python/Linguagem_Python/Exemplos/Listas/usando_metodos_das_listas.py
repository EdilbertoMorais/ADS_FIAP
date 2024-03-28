# Criando a lista com os valores fora de ordem
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5]

# exibição da lista
print("A lista foi criada assim: {}".format(valores))

# Contando os elementos da lista
contagem = valores.count(7)
print("Nessa lista o número 7 aparece {} vezes".format(contagem))

# Ordenando a lista do menor para o maior
valores.sort()
print("A lista agora está ordenada: {}".format(valores))

# Invertendo a ordem da lista
valores.reverse()
print("A lista agora está invertida: {}".format(valores))

# Verificando o tamanho da lista
tamanho = len(valores)
print("A lista possui {} elementos".format(tamanho))

# Somando o valor de todos os elementos da lista
soma = sum(valores)
print("A soma dos valores da lista é {}".format(soma))
