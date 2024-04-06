# nomes = ['Joao', 'Pedro', 'Ana', 'Maria']
# votos = [15, 5, 15, 2]
#
# maior = max(votos)
# print(maior)
#
# quantidade = votos.count(maior)                     # quantidade vez que o maior aparece na lista
# print(quantidade)
#
# if quantidade > 1:
#     print('Houve empate')
# else:
#     indice = votos.index(maior)                     # indice do maior item
#     print(f'Houve uma vitória do candidato {nomes[indice]}')
#     print(f'O candidato teve {maior} votos')

nomes = ['Joao', 'Pedro', 'Ana', 'Maria']
votos = [15, 5, 15, 2]

maior_voto = max(votos)  # Encontra o maior número de votos

# Lista de índices dos vencedores
indices_vencedores = [i for i, voto in enumerate(votos) if voto == maior_voto]

if len(indices_vencedores) > 1:
    print("Houve um empate entre:")
    for indice in indices_vencedores:
        print(f"- {nomes[indice]} com {maior_voto} votos")
else:
    indice_vencedor = indices_vencedores[0]  # Índice do único vencedor
    print(f"O vencedor foi {nomes[indice_vencedor]} com {maior_voto} votos")