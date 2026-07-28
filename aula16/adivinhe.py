'''
# Disciplina: Pensamento Computacional, Algoritimos e Programação (PCAP)
# Projeto   : Jogo "Adivinhe o Número"
# Arquivo   : adivinhe.py
# Autor     : Maria Eduarda Denck
# Data      : 2026.05.28
'''

import random

# Sorteamos o número secreto entre 1 e 10
def jogar(maximo, chances):
numero_secreto = random.randint(1, 10)
chances = 3 
acertou = False 

# 2) Pedimos um palpite (input devolve TEXTO; convertemos para inteiro)
while chances > 0 and not acertou: 
    palpite = int(input("Digite um número de 1 a 10: "))
    if palpite == numero_secreto: 
        print("🎉 Acertou! O número era", numero_secreto)
        acertou = True 
    elif palpite < numero_secreto:
        print("📈 Muito baixo! Tente um número maior.")
    else:
        print("📉 Muito baixo! Tente um número menor.")
    chances = chances - 1 # gasta uma chance 
    print("Chances restantes:", chances)
    return acertou # devolve True (venceu) ou False (perdeu)


niveis = [ 
    ["Fácil", 10, 3],
    ["Médio", 100,5],
    ["Impossível", 1000, 10],
]


print("Escolhao nível de dificuldade:")
print("1 - Fácil    (1 a 10 3 chances)")
print("2 - Médio    (1 a 100, 5 chances)")
print("3 - Impossível   (1 a 1000, 10 chances)")
opcao = int(input("Digite 1, 2 ou 3: "))
print("Você chutou:", palpite)
print("O número secreto era:", numero_secreto)
nivel = niveis[opcao - 1]


venceu = jogar(10, 3)
if not venceu:
    print("💀 Fim de Jogo!")
if not acertou: 
    print("💀 Suas chances acabaram! O número era", numero_secreto)
