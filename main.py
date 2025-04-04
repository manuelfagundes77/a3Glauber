from geolocalizacao import encontrar_centro_proximo
from caminhoes import escolher_caminhao
from entregas import Entrega, entregas

def main():
    while True:
        print("\n📦 **Sistema de Gerenciamento de Entregas**")
        print("1️ - Adicionar nova entrega")
        print("2️ - Ver todas as entregas")
        print("0️ - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cidade_destino = input("\n🏙 Digite a cidade de destino: ")
            peso = float(input("📦 Digite o peso da carga (kg): "))

            centro, distancia = encontrar_centro_proximo(cidade_destino)

            if centro:
                caminhao, consumo, prazo = escolher_caminhao(centro, peso, distancia)

                if caminhao is not None:  # Apenas cadastra se houver caminhão disponível
                    entrega = Entrega(cidade_destino, centro, distancia, caminhao, prazo)
                    entregas.append(entrega)
                    print("\n✅ **Entrega cadastrada com sucesso!**\n")
                    print(entrega.detalhes_entrega())
                else:
                    print("\n❌ Todos os caminhões do centro de distribuição estão ocupados.")
            else:
                print("\n❌ Não foi possível encontrar a cidade.")

        elif opcao == "2":
            if entregas:
                print("\n📜 **Lista de todas as entregas cadastradas:**\n")
                for entrega in entregas:
                    print(entrega.detalhes_entrega())
            else:
                print("\n❌ Nenhuma entrega cadastrada ainda.")

        elif opcao == "0":
            print("\n🚪 Saindo do sistema... Até mais!")
            break

        else:
            print("\n❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
