# ═══════════════════════════════════════════════════════════
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Par ou Ímpar"
# Arquivo    : par_impar.py
# Autor      : Maria Eduarda Denck
# Data       : 2026.06.25
# ═══════════════════════════════════════════════════════════
import random

pontos_jogador = 0
pontos_maquina = 0
for rodada in range(0, 5):
    print("--- Rodada", rodada, "---")
    pontos_jogador = pontos_maquina + 1

    Escolha = input("Sua escolha (par ou impar): ")
    jogada_maquina = random.randint(0, 5)
    jogada_jogador = int(input("Sua jogada (0 a 5): "))
    opcoes = ["par", "impar"]

    if Escolha not in opcoes:
        print("Jogada Inválida.")


    dedos = jogada_maquina + jogada_jogador
    if dedos % 2 == 0:
        print("par")
    else:
        print("impar")

    print(f"{jogada_maquina}")

    def quem_venceu(paridade, Escolha):
        if paridade % 2 == 0:
            paridade = "par"
        else:
            paridade = "impar"
    

print("Placar -> Você:", pontos_jogador, "| Máquina:", pontos_maquina)