import requests
from haversine import haversine

# Chave da OpenCage API
api_key = "b431b8eeb3bf4c58a5bb82877d41b534"
import requests  # Biblioteca para fazer requisições HTTP
from haversine import haversine  # Função para calcular a distância entre coordenadas geográficas

# Chave da OpenCage API
api_key = "b431b8eeb3bf4c58a5bb82877d41b534"  # Chave para acessar a API de geolocalização
1

# Centros de distribuição com suas coordenadas (latitude, longitude)
centros_distribuicao = {
    "Florianópolis": (-27.5954, -48.5480),
    "Belém": (-1.4558, -48.4903),
    "Recife": (-8.0476, -34.8770),
    "São Paulo": (-23.5505, -46.6333),
    "Brasília": (-15.7801, -47.9292)
}

# Função para obter as coordenadas de uma cidade usando a OpenCage API
def get_Coordenadas(city):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key={api_key}"  # Monta a URL da API
    response = requests.get(url)  # Faz a requisição para a API
    data = response.json()  # Converte a resposta para JSON
    
    if data['results']:  # Verifica se há resultados na resposta
        latitude = data['results'][0]['geometry']['lat']  # Obtém a latitude
        longitude = data['results'][0]['geometry']['lng']  # Obtém a longitude
        return (latitude, longitude)  # Retorna as coordenadas como uma tupla
    
    return None  # Retorna None se não encontrar resultados

# Função para encontrar o centro de distribuição mais próximo de uma cidade
def encontrar_centro_proximo(cidade_destino):
    destino_coords = get_Coordenadas(cidade_destino)  # Obtém as coordenadas da cidade de destino
    
    if destino_coords is None:  # Verifica se as coordenadas foram encontradas
        return None, None  # Retorna None se não encontrar as coordenadas

    distancia_minima = float('inf')  # Inicializa a distância mínima com um valor muito alto
    centro_proximo = None  # Inicializa o centro mais próximo como None

    # Itera sobre os centros de distribuição para encontrar o mais próximo
    for centro, coords in centros_distribuicao.items():
        distancia = haversine(destino_coords, coords)  # Calcula a distância entre o destino e o centro
        if distancia < distancia_minima:  # Verifica se a distância é menor que a mínima encontrada
            distancia_minima = distancia  # Atualiza a distância mínima
            centro_proximo = centro  # Atualiza o centro mais próximo

    return centro_proximo, distancia_minima  # Retorna o centro mais próximo e a distância