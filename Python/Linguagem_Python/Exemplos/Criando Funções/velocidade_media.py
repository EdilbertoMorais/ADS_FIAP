def calcularVelocidadeMedia(distancia, tempo):
    # calcular a velocidade média
    velocidade_media = distancia / tempo
    # exibir o resultado
    print(f"A velocidade média é {velocidade_media:.2f} km/h")


# Aqui começa o programa
distancia = float(input("Informe a distancia: "))
tempo = float(input("Informe o tempo: "))
# Chamando a função com valores definidos pelo usuário
calcularVelocidadeMedia(distancia, tempo)
