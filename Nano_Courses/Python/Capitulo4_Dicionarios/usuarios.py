"""
Em Java, o equivalente ao DICIONÁRIO em Python é a interface Map e suas implementações, sendo a implementação mais
comum a HashMap. Um Map em Java é uma coleção de pares chave-valor, onde cada chave é única e mapeada para um valor
correspondente. Isso é semelhante ao conceito de dicionário em Python, onde você pode associar valores a chaves e
acessar esses valores através das chaves.
"""
usuarios = {"Chaves": ["Chaves Silva", "17/06/2017", "Recep_01"],
            "Quico": ["Enrico Flores", "03/06/2017", "Raiox_02"],
            "Edilberto": ["Edilberto Cunha", "18/03/2024", "Lab_01"],
            "Florinda": ["Florinda Flores", "26/11/2017", "Recep_01"]}

# Imprime o Dicionario usuarios
print(usuarios)
print("##############========#########")
# Retorna None quando um dado buscado não é encontrado (Não existe Chiquinha no Dicionário)
print("Dados: ", usuarios.get("Chiquinha"))
