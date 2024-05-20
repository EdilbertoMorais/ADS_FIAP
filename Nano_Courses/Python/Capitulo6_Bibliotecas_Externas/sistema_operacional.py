import platform

# Retorna a distro exata que esta sendo utilizada no sistema operacional.
print("Distribuição do Sistema Operacional.: ", platform.platform())
# Retorno o sistema operacional que esta sendo utilizado.
print("Nome do Sistema Operacional.........: ", platform.system())
# Retorna a versão do sistema operacional que esta sendo utilizado.
print("Versão do Sistema Operacional.......: ", platform.release())
# Retorna a arquitetura do sistema operacional que esta sendo utilizado.
print("Arquitetura.........................: ", platform.architecture())
# Retorna o nome do computador na rede.
print("Nome do Computador..................: ", platform.node())
# Retorna o tipo da máquina.
print("Tipo de Máquina.....................: ", platform.machine())
# Retorna o processador que esta sendo utilizado.
print("Processador.........................: ", platform.processor())
# Retorna a versão do Python que esta sendo utilizado.
print("Versão do Python....................: ", platform.python_version())
