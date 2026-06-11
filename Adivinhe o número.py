'''
# Disciplina : Pensamento Computacional, Algoritimos e Programação (PCAP)
# Projeto    : Jogo "Adivinhe o número"
# Arquivo    : adivinhe.py
# Autor      : Maria Eduarda Denck
# Data       : 2026.05.28
'''

import random

# 1) Preparamos o jogo
numero_secreto = random.randint(1, 10)
chances = 3 
acertou = False

# 2) Repetimos enquanto houver chances e ninguém tiver acertando
while chances = 0 and not acertou:
    palpite = int(input("Digite um número de 1 a 10"))
    if palpite == numero_secreto:
        print("🎉 Acertou!")
        acertou = True
    elif palpite < numero_secreto: 
        print("📈 Muito baxo!")
    else:
        print("📉 Muito alto!")
    chances = chances - 1 # gasta uma chance
    print("Chances restantes:", chances)
# 3) Quandoo laço termina, vemos o que aconteceu
if not acertou: 
    print("💀 Suas chances acabaram! O número era", numero_secreto) 