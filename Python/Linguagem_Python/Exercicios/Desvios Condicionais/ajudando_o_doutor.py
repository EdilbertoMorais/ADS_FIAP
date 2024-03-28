"""
O Dr Jones estabeleceu uma regra com seus alunos da disciplina de Arqueologia: todos os que
obtiverem uma nota maior que 8,5 na sua prova semestral serão convidados para uma visita de
campo na América do Sul.

Faça um programa que solicite o e-mail e a nota do aluno, exibindo a msg "ENVIANDO CONVITE" caso
a nota do aluno satisfaça a condição proposta.
"""
import re

while True:
    email_aluno = input("digite seu e-mail: ").lower()
    # Verifica se o formato do e-mail está correto utilizando a função match do módulo re
    if re.match(r'^[a-z0-9._%+-]+@[a-z0-9_-]+\.[a-z]{2,}$', email_aluno):
        break
    else:
        print("E-mail inválido")

while True:
    nota_semestral = float(input("Insira sua nota: "))
    # Verifica se a nota está entre 0 e 10.
    if 0 <= nota_semestral <= 10:
        break
    else:
        print("Nota inválida")
# Verifica o teste logico.
if nota_semestral >= 8.5:
    print(f"ENVIANDO CONVITE para o e-mail {email_aluno}")
