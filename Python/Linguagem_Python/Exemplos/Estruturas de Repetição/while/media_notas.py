
# Solicitar as notas de N alunos e calcular a média da turma

quantidade = int(input('Informe a quantidade de alunos: '))

cont = 0                            # contadora (conta a quantidade repetições)
soma = 0                            # somadora (somar todas as notas dos alunos)

while cont < quantidade:
    nota = float(input('Informe a nota: '))
    soma += nota
    cont += 1

print(f'Somatório das notas: {soma}')

media = soma / quantidade
print(f'Média das notas: {media}')
