import json
arquivo_json = open(
    "/home/edilberto/projetos/ADS_FIAP/Python/Arquivos para Manipular/dicionario.json",
    "r", encoding="utf-8")

conteudo = arquivo_json.read()
arquivo_json.close()
print(type(conteudo))

novo_conteudo_em_json = json.loads(conteudo)
print(type(novo_conteudo_em_json))
print(novo_conteudo_em_json)
