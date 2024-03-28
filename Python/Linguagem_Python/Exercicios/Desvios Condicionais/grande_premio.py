"""
Criar um algoritmo onde o usuário possa digitar o voto de cada um dos 5 membros da equipe
e, ao final, exiba qual foi o console escolhido e com quantos votos.

Opções: PLAYSTATION, XBOX e NINTENDO
"""

playstation = 0
xbox = 0
nintendo = 0
equipe = 0

# Entrada de dados
while equipe < 5:
    voto = int(input(f"""Vote em uma das opções:
[1] Playstation
[2] Xbox
[3] Nintendo
[4] Sair 
{equipe + 1}º Voto: """))
    if voto == 1:
        print("Voto computado para Playstation")
        playstation += 1
    elif voto == 2:
        print("Voto computado para Xbox")
        xbox += 1
    elif voto == 3:
        print("Voto computado para Nintendo")
        nintendo += 1
    equipe += 1

print("####### APURAÇÃO DOS VOTOS #######")
print(f""" Quantidade de votos até o momento:
 - Playstation: {playstation}
 - Xbox: {xbox}
 - Nintendo: {nintendo}""")

print("####### O Console Escolhido foi:  #######")
if playstation > xbox and playstation > nintendo:
    print("Playstation".upper())
elif xbox > nintendo and xbox > playstation:
    print("Xbox".upper())
else:
    print("Nintendo".upper())
