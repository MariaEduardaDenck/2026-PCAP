# ==========================================================
# Disciplina: Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto: Jogo "Pedra-Papel-Tesoura"
# Arquivo: ppt.py
# Autor: Maria Eduarda Denck
# Data: 16/06/26
# ==========================================================

import random
def resultado(jogador, maquina):
    if jogador == maquina:
        return "empate"
    if jogador == "pedra" and maquina == "tesoura":
        return "jogador"
    if jogador == "papel" and maquina == "pedra":
        return "jogador"
    if jogador == "tesoura" and maquina == "papel":
        return "jogador"
    return "maquina"

opcoes = ["pedra", "papel", "tesoura"]
pontos_jogador = 0
pontos_maquina = 0

for rodada in range(1, 6):
    print("--- Rodada", rodada, "---")

    jogada_maquina = random.choices(opcoes)
    entrada = input("Sua jogada (pedra, papel, tesoura): ")
    jogada_jogador = entrada.lower().strip()


    if jogada_jogador not in opcoes:
        print("❌ Jogada inválida! Digite pedra, papel ou tesoura.")
        pontos_maquina = pontos_maquina + 1
    elif jogada_jogador == jogada_maquina:
        print("🤝 Empate! Os dois jogaram", jogada_maquina)
    elif jogada_jogador == "pedra" and jogada_maquina == "tesoura":
        print("🎉 Você venceu! Pedra quebra tesoura.")
        pontos_jogador = pontos_jogador +1
    elif jogada_jogador == "papel" and jogada_maquina == "pedra":
        print("🎉 Você venceu! Papel embrulha a pedra.")
        pontos_jogador = pontos_jogador + 1
    elif jogada_jogador == "tesoura" and jogada_maquina == "papel":
        print("🎉Você venceu! Tesoura corta papel.")
        pontos_jogador = pontos_jogador + 1
    else: 
        quem = resultado(jogada_jogador, jogada_maquina)
        if quem == "empate":
            print("🤝 Empate!")
        elif quem == "jogador":
            print("🎉 Você ganhou a rodada!")
            pontos_jogador = pontos_jogador + 1
        print("💀 A máquina venceu! Ela jogou", jogada_maquina)
        pontos_maquina = pontos_maquina + 1

print("Placar final --> Você", pontos_jogador, "| Máquina:", pontos_maquina)
