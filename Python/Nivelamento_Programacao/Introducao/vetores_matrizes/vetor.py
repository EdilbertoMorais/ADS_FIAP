"""
- O conteúdo dos elementos é heterogêneo
- Os elementos são dinâmicos, ou seja, acrescentamos ou excluímos quando quisermos
- O append acrescenta um item no final. lista.append(45)
- O insert permite editar um elemento. lista.inserte(índice, conteúdo)
- O pop remove o último elemento da lista. lista.pop()
- O clear apaga todos os elementos da lista. lista.clear
"""

# listas em python pode ter elementos heterogêneos
lista = ["a", 2, True, 4.5]
print(lista)

# adicionando um elemento no final da lista
lista.append(45)
print(lista)

# editando um elemento existente
lista.insert(0, 99)
print(lista)

# pop remove o último elemento da lista
lista.pop()
print(lista)

# apagar todos os elementos da lista
lista.clear()
print(lista)

# preenchendo 5 elementos da lista
for cont in range(0, 5, 1):
    numero = float(input("Digite um elemento: "))
    lista.append(numero)
print(lista)

# # exibindo todos os elementos da lista usando o for
# for i in range(0, 5, 1):
#     print(lista[i])

# exibindo todos os elementos da lista usando o for sem passar o range
for elemento in lista:  # mesmo resultado da linha 37
    print(elemento)

# somando os elementos da lista
soma = 0
for elemento in lista:
    soma += elemento  # soma = soma + elemento
print("A soma dos elementos da lista é: ", soma)

