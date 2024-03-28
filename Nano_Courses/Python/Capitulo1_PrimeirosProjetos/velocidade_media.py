# Pedir a distância da viagem
distancia = float(input("Por favor, digite a distancia percorrida: "))
# Pedir o tempo da viagem
tempo = float(input("Por favor, digite a distancia percorrida: "))
# Dividir a distancia pelo tempo
velocidade_media = distancia / tempo
# Exibir o resultado para o usuario
print("A velocidade média foi de {:.2f} Km/h".format(velocidade_media))  # :.2f aqui preserva-se tudo antes da virgula
# e considera-se apensas 2 casas decimais
print(f"A velocidade média foi de {velocidade_media:.2f} km/h")
