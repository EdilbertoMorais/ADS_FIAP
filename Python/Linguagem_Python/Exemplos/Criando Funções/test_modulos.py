# importação do módulo calc.py
from calc import *

options = -1
while options != 5:
    print("""
    [1] Somar
    [2] Subtrair
    [3] Dividir
    [4] Multiplicar
    [5] Sair
    Digite uma opção: """)
    options = int(input())

    if options == 1:
        print(somar(float(input("Digite o 1 valor: ")), float(input("Digite o 2 valor: "))))
    elif options == 2:
        print(subtrair(float(input("Digite o 1 valor: ")), float(input("Digite o 2 valor: "))))
    elif options == 3:
        print(dividir(float(input("Digite o 1 valor: ")), float(input("Digite o 2 valor: "))))
    elif options == 4:
        print(multiplicar(float(input("Digite o 1 valor: ")), float(input("Digite o 2 valor: "))))
    elif options == 5:
        print("Saindo do programa")
    else:
        print("Opção inválida")
