contatos = {
    "Clark Kent": {
        "celular": "123456",
        "email": "clark@krypto.com"
    },
    "Bruce Wayne": {
        "celular": "654321",
        "email": "bat@caverna.com"
    }
}

print("Chaves do dicionario...")
print(contatos.keys())
print("####################################")
print("Valores do dicionario...")
print(contatos.values())
print("####################################")
print("Chaves e valores do dicionario...")
print(contatos.items())
print("####################################")

print("Formatando a apresentação do dicionario...")
for nome, formas_contato in contatos.items():
    print(f"O contato {nome}")
    for forma, valor in formas_contato.items():
        print(f"pode ser contatado pelo seu {forma} através do {valor}")
    print("\n")
