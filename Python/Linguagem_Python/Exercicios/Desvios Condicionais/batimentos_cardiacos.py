"""
Verifique se os batimentos cardíacos por minuto se encontram na faixa adequada. Solicite ao
usuário que informe a quantidade de batimentos cardíacos por minuto(BPM) e a IDADE. A partir
disso, o script deve verificar e exibir uma mensagem informando se os batimentos do usuário
encontram-se DENTRO da faixa de batimentos adequada, ACIMA da faixa adequada ou ABAIXO da faixa
adequada de batimentos.

Até 2 anos = 120 a 140
de 8 a 17 anos = 80 a 100
Adulto sedentário = 70 a 80
Idosos = 50 a 60
"""
bpm = int(input("Informe os batimentos por minuto (BPM):"))
idade = int(input("Informe a idade: "))

if idade <= 2 and 120 <= bpm <= 140:
    print(f"Você está DENTRO da faixa de batimentos adequada")
elif idade >= 2 and bpm > 140:
    print(f"Você está ACIMA da faixa de batimentos adequada")
elif idade <= 2 and bpm < 120:
    print(f"Você está ABAIXO da faixa de batimentos adequada")
elif 8 <= idade <= 17 and 80 <= bpm <= 100:
    print(f"Você está DENTRO da faixa de batimentos adequada")
elif 8 <= idade <= 17 and bpm > 100:
    print(f"Você está ACIMA da faixa de batimentos adequada")
elif 8 <= idade <= 17 and bpm < 80:
    print(f"Você está ABAIXO da faixa de batimentos adequada")
elif 18 <= idade < 65 and 70 <= bpm <= 80:
    print(f"Você está DENTRO da faixa de batimentos adequada")
elif 18 <= idade < 65 and bpm > 80:
    print(f"Você está ACIMA da faixa de batimentos adequada")
elif 18 <= idade < 65 and bpm < 70:
    print(f"Você está ABAIXO da faixa de batimentos adequada")
elif idade >= 65 and 50 <= bpm <= 60:
    print(f"Você está DENTRO da faixa de batimentos adequada")
elif idade >= 65 and bpm > 60:
    print(f"Você está ACIMA da faixa de batimentos adequada")
elif idade >= 65 and bpm < 50:
    print(f"Você está ABAIXO da faixa de batimentos adequada")
