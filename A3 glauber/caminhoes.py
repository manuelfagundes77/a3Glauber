class Caminhao:
    def __init__(self, tipo, peso_maximo, consumo_por_km, velocidade_media, horas_max):
        self.tipo = tipo
        self.peso_maximo = peso_maximo
        self.consumo_por_km = consumo_por_km
        self.velocidade_media = velocidade_media
        self.horas_max = horas_max

    def calcular_consumo(self, distancia_km):
        return distancia_km * self.consumo_por_km

    def calcular_prazo(self, distancia_km):
        tempo_total_horas = distancia_km / self.velocidade_media
        dias = tempo_total_horas / self.horas_max
        return max(1, round(dias))


# Estoque de caminhões por centro de distribuição
centros_distribuicao_caminhoes = {
    "Florianópolis": {"Van": 2, "Caminhão Toco (2 eixos)": 2, "Caminhão Truck (3 eixos)": 2},
    "Belém": {"Van": 2, "Caminhão Toco (2 eixos)": 2, "Caminhão Truck (3 eixos)": 2},
    "Recife": {"Van": 2, "Caminhão Toco (2 eixos)": 2, "Caminhão Truck (3 eixos)": 2},
    "São Paulo": {"Van": 2, "Caminhão Toco (2 eixos)": 2, "Caminhão Truck (3 eixos)": 2},
    "Brasília": {"Van": 2, "Caminhão Toco (2 eixos)": 2, "Caminhão Truck (3 eixos)": 2}
}

caminhoes = [
    Caminhao("Van", 1500, 0.12, 80, 8),
    Caminhao("Caminhão Toco (2 eixos)", 6000, 0.28, 70, 9),
    Caminhao("Caminhão Truck (3 eixos)", 14000, 0.35, 60, 10)
]

def escolher_caminhao(centro, peso, distancia_km):
    """ Escolhe o caminhão disponível e avisa qual será o próximo caso um esteja indisponível. """
    
    caminhão_selecionado = None
    aviso = ""  # Mensagens de alerta

    for i, caminhao in enumerate(caminhoes):
        if peso <= caminhao.peso_maximo:
            if centros_distribuicao_caminhoes[centro][caminhao.tipo] > 0:
                caminhão_selecionado = caminhao.tipo
                break  # Achou um caminhão disponível
            else:
                # Se há outro caminhão maior, avisa qual será tentado
                if i + 1 < len(caminhoes):
                    proximo_caminhao = caminhoes[i + 1].tipo
                    aviso += f"\n⚠️ Todos os {caminhao.tipo}s desse centro de distribuição estão ocupados. Tentando {proximo_caminhao}..."
                else:
                    aviso += f"\n⚠️ Todos os {caminhao.tipo}s desse centro de distribuição estão ocupados."

    if caminhão_selecionado is None:
        print("\n❌ Nenhum caminhão disponível nesse centro de distribuição no momento.")
        return None, None, None  # Nenhum caminhão pode ser alocado

    # Exibe o aviso antes de seguir
    if aviso:
        print(aviso)

    # Atualiza o estoque de caminhões
    centros_distribuicao_caminhoes[centro][caminhão_selecionado] -= 1

    # Calcula consumo e prazo com base no caminhão escolhido
    melhor_caminhao = next(c for c in caminhoes if c.tipo == caminhão_selecionado)
    consumo = melhor_caminhao.calcular_consumo(distancia_km)
    prazo = melhor_caminhao.calcular_prazo(distancia_km)

    return caminhão_selecionado, consumo, prazo
