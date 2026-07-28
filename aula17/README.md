1 - variáveis: pontos_jogador, pontos_maquina e rodada.
pontos_jogador e pontos_maquina é uma variável para guardar os pontos e jogadas da maquina e o jogador.
rodada serve para guardar o número de rodadas jogadas.

2 - Estruturas de Condição: if jogada_jogador not in opcoes:
        print("❌ Jogada inválida! Digite pedra, papel ou tesoura."): serve para quando o jogador não joga nenhuma das opções possíveis.

3 - entrada:  elif quem == "jogador":
            print("🎉 Você ganhou a rodada!")
            pontos_jogador = pontos_jogador + 1
            adiciona +1 ponto para quem ganhar.