
# LISTA (armazena uma sequência de itens)

lista = ['Paulo', 'Ana', 'João', 10, 4, 60]
print(lista)

# indice (posição de cada item, começa em zero)
print(lista[0])

# altera um item da lista
lista[0] = 100
print(lista)

# insere um item na lista
lista.append(500)
lista.append(600)
print(lista)

# preenche a lista com 10 numeros digitado pelo usuario
lista = []              # lista vazia
for i in range(10):
    numero = int(input('Numero: '))
    lista.append(numero)
print(lista)

# percorre os itens da lista
print('Itens na lista: ')
for item in lista:
    print(item)

# conta a quantidade de números pares na lista
conta_par = 0
for item in lista:
    if item % 2 == 0:
        conta_par += 1
print(f'Quantidade de pares: {conta_par}')
