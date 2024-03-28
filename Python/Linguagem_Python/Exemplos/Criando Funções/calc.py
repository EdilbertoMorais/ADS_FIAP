# função de soma
def somar(a: float, b: float):
    return float(a) + float(b)


# função de subtração
def subtrair(a: float, b: float):
    return float(a) - float(b)


# função de divisão
def dividir(a: float, b: float):
    if b == 0:
        return 0
    return float(a) / float(b)


# função de multiplicar
def multiplicar(a: float, b: float):
    return float(a) * float(b)
