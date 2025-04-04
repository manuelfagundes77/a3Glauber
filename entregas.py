# Classe que representa uma entrega
class Entrega:
    def __init__(self, cidade_destino, centro_origem, distancia, caminhao, prazo):
        self.cidade_destino = cidade_destino  # Nome da cidade de destino
        self.centro_origem = centro_origem  # Nome do centro de distribuição de origem
        self.distancia = distancia  # Distância em quilômetros até o destino
        self.caminhao = caminhao  # Caminhão usado para a entrega
        self.prazo = prazo  # Prazo estimado para a entrega em dias

    def detalhes_entrega(self):
        return (f"\n===== DETALHES DA ENTREGA =====\n"
                f"Centro de Distribuição: {self.centro_origem}\n"  # Exibe o centro de origem
                f"Destino: {self.cidade_destino}\n"  # Exibe a cidade de destino
                f"Distância: {self.distancia:.2f} km\n"  # Exibe a distância formatada com 2 casas decimais
                f"Caminhão Escolhido: {self.caminhao}\n"  # Exibe o caminhão usado
                f"Prazo Estimado: {self.prazo} dias\n")  # Exibe o prazo estimado

# Lista para armazenar todas as entregas
entregas = []  # Armazena objetos do tipo Entrega