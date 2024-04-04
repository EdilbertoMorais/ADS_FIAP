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

#  Instanciando as variáveis para computar os votos:
segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

#  Looping para iterar a votação:
for iterador in range(qtda_votos):
    voto_valido = False
    while not voto_valido:
        voto = int(input(""" Vote em uma das opções abaixo: 
        [1] Segunda-feira
        [2] Terça-feira
        [3] Quarta-feira
        [4] Quinta-feira
        [5] Sexta-feira
        
        Digite o número conforme as opções apresentadas acima: """))

        if 1 <= voto <= 5:
            voto_valido = True
        else:
            print("Opção inválida!")

    if voto == 1:
        segunda += 1
    elif voto == 2:
        terca += 1
    elif voto == 3:
        quarta += 1
    elif voto == 4:
        quinta += 1
    elif voto == 5:
        sexta += 1


#  Condição que verifica o dia mais votado e imprime o resultado:
print("Resultado da votação: ")
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("Dia mais votado: Segunda-feira")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("Dia mais votado: Terça-feira")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("Dia mais votado: Quarta-feira")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("Dia mais votado: Quinta_feira")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("Dia mais votado: Sexta-feira")
else:
    print(f""" Houve um empate na votação:
     total votos:
     Segunda-feira :{segunda}
     Terça-feira :{terca}
     Quarta-feira :{quarta}
     Quinta-feira :{quinta}
     Sexta-feira :{sexta}
    """)
