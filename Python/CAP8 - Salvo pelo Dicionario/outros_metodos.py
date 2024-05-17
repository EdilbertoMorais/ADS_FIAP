# criação e exibição da tupla
tupla = (1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5)
print(f"A tupla foi criada assim: {tupla}")

print("\nutilizando enumerate para mostrar uma sequência")
for numero, valor in enumerate(tupla):
    print(f"No índice {numero} temos: {valor}")

print("\nmostrando a quantidade de itens na tupla")
print(f"Quantidade: {len(tupla)}")

print("\nmostrando o valor mínimo na tupla")
print(f"Mínimo: {min(tupla)}")

print("\nMostrando o valor máximo na tupla")
print(f"Máximo: {max(tupla)}")

print("\nMostrando a soma de todos os valores da tupla")
print(f"Soma: {sum(tupla)}")
print(f"Máximo: {sum(tupla)}")

print("\nutilizando tupla() para a conversão de uma lista para uma tupla")
lista = [True, False]
print(f"Lista: {lista}")
tupla2 = tuple(lista)
print(f"Tupla: {tupla2}")

print("\ncriando a tupla3 com os valores 1 (True) e 0 (False)")
tupla3 = (1, 0)
print(tupla3)

print("\nfunção all")
print(f"Testando a tupla2 com all: {all(tupla2)}")
print(f"Testando a tupla3 com all: {all(tupla3)}")

print("\nfunção any")
print(f"Testando a tupla2 com any: {any(tupla2)}")
print(f"Testando a tupla3 com any: {any(tupla3)}")
