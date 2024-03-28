# instanciando a variavel com um valor inicial.
resposta = 0
# Enquanto a resposta não for 42, a repetição ocorre.
while resposta != 42:
    # Para cada uma das repetições, o usuário vai submeter uma resposta.
    resposta = int(input("Qual a resposta para a vida, o universo e tudo mais? (Dica: A resposta é"
                         " um número de 2 dígitos) :"))
# Quando o laço terminar, a mensagem é exibida.
print("Parabéns, você acertou!")
