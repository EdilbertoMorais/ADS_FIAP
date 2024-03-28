# Exibe "Meu primeiro programa"
print("Meu primeiro Programa")
# Exibe o número 12
print(12)
"""
nome = "Edson"
idade = 48
peso = 85.64

# Forma 1
print("1. O meu nome é", nome, "tenho", idade, "anos e ", peso, "Quilos")

# Forma 2
print("2. O meu nome é {} tenho {} anos e {} Quilos".format(nome, idade, peso))
print("2. O meu nome é {0} tenho {1} anos e {2:.1f} Quilos".format(nome, idade, peso))
print("2. O meu nome é {n} tenho {i} anos e {p:.2f} Quilos".format(n=nome,i=idade,p=peso))

# Forma 3
print(f"3. O meu nome é {nome} tenho {idade} anos e {peso:.2f} Quilos")

# Pede a digitação do salário ao usuário
salario = input("Digite o seu salário:")
salario = float(salario)
# Exibe o salário digitado
print("Salário = R$", salario)

nome = "Edson"      # Tipo Texto (string)
salario = 1234.56   # tipo real (float)
qtd_filhos = 2      # tipo inteiro (int)
opcao = 's'         # tipo caractere
maioridade = True   # tipo lógico

# Utilizando casting para modificar o tipo da variável
x = "55"            # x é do tipo string e vale '55'
x = float(x)        # x passou a ser float e vale 55.0
x = str(x)          # x voltou a ser string
x = int(float(x))          # x passou a ser int e vale 55

print("X vale = ", x)
"""
print("###########################################################")

# UTILIZANDO VARIÁVEIS DIFERENTES E DESCOBRINDO OS TIPOS
nome = "Edson"      # Tipo Texto (string)
print(f"A variável nome = {nome} é do tipo {type(nome)}")
salario = 1234.56   # tipo real (float)
print(f"A variável salario = {salario} é do tipo {type(salario)}")
qtd_filhos = 2      # tipo inteiro (int)
print(f"A variável qtd_filhos = {qtd_filhos} é do tipo {type(qtd_filhos)}")
opcao = 's'         # tipo caractere
print(f"A variável opcao = {opcao} é do tipo {type(opcao)}")
maioridade = True   # tipo lógico
print(f"A variável maioridade = {maioridade} é do tipo {type(maioridade)}")

# UTILIZANDO A MESMA VARIÁVEL E DESCOBRINDO O SEU TIPO DEPOIS DE UM CASTING
x = "55"            # x é do tipo string e vale '55'
print(f"x = {x} e é do tipo {type(x)}")
x = int(x)          # x passou a ser int e vale 55
print(f"x = {x} e é do tipo {type(x)}")
x = str(x)          # x voltou a ser string
print(f"x = {x} e é do tipo {type(x)}")
x = float(x)        # x passou a ser float e vale 55.0
print(f"x = {x} e é do tipo {type(x)}")

print("################################################3")

# Solicita quatro números ao usuário
print("Digite 4 números:")
n1 = input()
n1 = float(n1)
n2 = float(input())
n3 = float(input())
n4 = float(input())
# Calcula a média dos 4 números
media = (n1 + n2 + n3 + n4) / 4
print("Média = ", media)


print("################################################3")
# Solicitando os dados ao usuário
preco_maco = float(input("Digite o preço do maço: "))
qtd_maco = float(input("Digite a quantidade de maços:"))
anos = float(input("Digite a qtd. de anos que fuma:"))
# calcula a qtd. de dias como fumante
dias_fumante = anos * 365
# calcula o gasto do tempo que fuma
custo = dias_fumante * preco_maco
# Exibe o custo
print("Você já gastou R$ ", custo, "Fumando")

print("################################################3")
# Solicita a quantia
quantia = int(input("Digite a quantia: "))
# Efetua o cálculo das quantias de cédulas
ced50 = quantia // 50
quantia = quantia % 50
ced20 = quantia // 20
quantia = quantia % 20
ced10 = quantia // 10
quantia = quantia % 10
# Exibe as quantidades de cédulas
print("Quantidade das cédulas 50: ", ced50)
print("Quantidade das cédulas 20: ", ced20)
print("Quantidade das cédulas 10: ", ced20)
