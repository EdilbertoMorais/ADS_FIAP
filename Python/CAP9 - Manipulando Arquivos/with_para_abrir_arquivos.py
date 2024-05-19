# Quando usamos o with, não é necessário usarmos o close() para fechar o arquivo
# pois com o uso do with o arquivo é fechado automaticamente.
# Isso pode ser usado também para escrever no arquivo.
with open(
        "/home/edilberto/projetos/ADS_FIAP/Python/Arquivos para Manipular/dicionario.json",
        "r", encoding="utf-8") as arquivo_json:
    print(arquivo_json.read())
