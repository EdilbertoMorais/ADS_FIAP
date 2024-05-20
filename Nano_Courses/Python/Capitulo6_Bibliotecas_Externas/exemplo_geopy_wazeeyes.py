from geopy.geocoders import Nominatim
from Python.Funcoes.Funcoes_JSON import ler_arquivo, gravar_arquivo

# Inicializa o geolocalizador
geolocalizacao = Nominatim(user_agent="wazeyes")
# Lê o arquivo json e atribui o seu conteúdo a variavel dicionario
dicionario = ler_arquivo("/home/edilberto/projetos/ADS_FIAP/Nano_Courses/Python/Arquivos/endereco.json")
# Extrai a lista com os endereços para a variavel lista
lista = dicionario["endereco"]
# Pega os elementos das 3 primeiras posições da lista
endereco = lista[0] + " " + lista[1] + " " + lista[2]
print("ENDERECO FORMATADO", endereco)
# Obtém a localização
localizacao: object = geolocalizacao.geocode(endereco)
print("LOCALIZACAO INFORMADA", localizacao)
# Cria o dicionário de saída com as coordenadas, se a localização for encontrada
saida = {"coordenadas": (localizacao.latitude, localizacao.longitude)} if localizacao else {"coordenadas": (None, None)}
# Grava o resultado no arquivo
gravar_arquivo(saida, "/home/edilberto/projetos/ADS_FIAP/Nano_Courses/Python/Arquivos/saida.json")
