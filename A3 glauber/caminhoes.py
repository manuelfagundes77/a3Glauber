

class Caminhao:
    def __init__(self, tipo, peso_maximo, consumo_por_km):
        self.tipo = tipo
        self.peso_maximo = peso_maximo
        self.consumo_por_km = consumo_por_km

    def calcular_consumo(self, distancia_km):
        return distancia_km * self.consumo_por_km


# Lista de caminhões
caminhoes = [
    Caminhao("Van", 1000, 0.1),
    Caminhao("Caminhão de 2 eixos", 5000, 0.2),
    Caminhao("Caminhão de 4 eixos", 10000, 0.3)
]

def escolher_caminhao(peso, distancia_km):
    for caminhao in caminhoes:  
        if peso <= caminhao.peso_maximo:
            consumo = caminhao.calcular_consumo(distancia_km)
            print(f"Usando {caminhao.tipo} com capacidade de {caminhao.peso_maximo} kg, o consumo será de {consumo:.2f} litros de gasolina.")
            return caminhao.tipo, consumo
    return "Nenhum caminhão disponível para esse peso", 0
