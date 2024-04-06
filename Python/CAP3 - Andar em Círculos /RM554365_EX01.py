"""1 – A Bidu é uma startup na área de Fintech fundada em 2011 que ajuda os usuários a controlar
suas fontes de receitas, gastos, dívidas e investimentos.  Ela precisa realizar uma votação para
escolher qual dia da semana é o melhor para a realização das lives com o time da mentoria
financeira. Desenvolva um programa em que os colaboradores informem um dos 5 dias da semana (
segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) da sua preferência para
participar da live. Verifique e exiba ao final, qual dia foi o escolhido pelos colaboradores.

Observação: Verifique o número de colaboradores que irão participar da votação para programar sua
estrutura de repetição."
"""

#  Verificar quantos colaboradores irão participar da votação:
qtda_votos = int(input("Informe a quantidade de colaboradores que irão participar da votação: "))

#  Cria uma lista com os dias que serão votados
dias_semana = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira"]

#  Cria a lista com 5 elementos que receberão os votos, cada elemento dessa lista representa
#  o elemento da lista dias_semana na mesma ordem.
votos = [0] * 5

# Laço de repetição que solicita o voto do colaborador
for i in range(qtda_votos):
    voto_valido = False
    while not voto_valido:
        voto = int(input(""" Vote em uma das opções abaixo: 
        [1] Segunda-feira
        [2] Terça-feira
        [3] Quarta-feira
        [4] Quinta-feira
        [5] Sexta-feira
        
        Digite o número conforme as opções apresentadas acima: """))
        # valida o voto do colaborador
        if 1 <= voto <= 5:
            voto_valido = True
        else:
            print("Opção inválida!")
    #  Incrementa o indíce da lista votos conforme a opção de voto escolhido
    if voto == 1:
        votos[0] += 1
    elif voto == 2:
        votos[1] += 1
    elif voto == 3:
        votos[2] += 1
    elif voto == 4:
        votos[3] += 1
    elif voto == 5:
        votos[4] += 1

# Encontra o elemento com o maior número de votos
maior_voto = max(votos)

# Cria a lista dos mais votados
dias_mais_votados = []

#  Add os elementos da lista votos a lista dias_mais_votados que possuem o mesmo valor do elemento
for indice_do_dia, quantidade_de_votos in enumerate(votos):
    if quantidade_de_votos == maior_voto:
        dias_mais_votados.append(indice_do_dia)

#  Verifica se a lista mais_votados possui mais de 1 elemento, caso positivo, imprime a mensagem
#  "Houve um empate e itera sobre a lista imprimindo os elementos mais votados"
if len(dias_mais_votados) > 1:
    print("Houve um empate entre os dias:")
    for indice in dias_mais_votados:
        print(f"- {dias_semana[indice]} com {maior_voto} votos")
#  Caso a lista mais_votados não seja maior que 1, imprime o dia mais votado
else:
    indice_vencedor = dias_mais_votados[0]  # Índice do único vencedor
    print(f"O vencedor foi {dias_semana[indice_vencedor]} com {maior_voto} votos")
