import json

contatos = {
    "Clark Kent": {
        "Celular": "123456",
        "Email": "super@krypton.com"
    },
    "Bruce Wayne": {
        "Celular": "654321",
        "Email": "bat@caverna.com.br"
    }
}

# Indentando para apresentar no padrão Json
print(json.dumps(contatos, indent=4))

arquivo_json = open(
    "/home/edilberto/projetos/ADS_FIAP/Python/Arquivos para Manipular/dicionario.json",
    "w", encoding="utf-8")

conteudo = json.dumps(contatos, indent=4)
arquivo_json.write(conteudo)
arquivo_json.close()
