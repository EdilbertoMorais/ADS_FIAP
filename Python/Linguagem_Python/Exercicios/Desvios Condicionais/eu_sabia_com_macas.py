"""
Criar um programa no qual o usuário só tenha que escrever os valores de A, B e C e nosso
programa vai se encarregar de fazer os cálculos.
A primeira etapa que aprendermos na escola é calcular o DELTA por meio da fórmula:
B² - 4 * A * C. Depois, caso o delta seja positivo, existem dois valores para X. Caso
seja 0, existe apenas um valor. E caso seja negativo, informamos não haver valor real para X.
"""
import math

# Solicitando os valores de A, B e C para o usuário.
a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))
# Cálculo de DELTA
delta = (b ** 2) - (4 * a * c)
# Verificando as condições.
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Para a equação {}X² + {}X + {} = 0, obtivemos os seguintes valores:"
          "X1 = {} e X2 = {}".format(a, b, c, x1, x2))
elif delta == 0:
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("Para a equação {}X² + {}X + {} = 0, obtivemos o seguinte valor: "
          "X = {}".format(a, b, c, x))
else:
    print("Para a equação {}X² + {}X + {} = 0, não existem valores reais para X".format(a, b, c))
