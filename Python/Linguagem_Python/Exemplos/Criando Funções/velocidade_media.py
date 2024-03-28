def calcularVelocidadeMedia(distancia, tempo):
    # calcular a velocidade média
    velocidade_media = distancia / tempo
    # exibir o resultado
    return velocidade_media


# Aqui começa o programa
distancia = float(input("Informe a distancia: "))
tempo = float(input("Informe o tempo: "))
# Chamando a função com valores definidos pelo usuário
print(f"A velocidade média é {calcularVelocidadeMedia(distancia, tempo):.2f}")
