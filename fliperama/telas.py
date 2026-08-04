# ==============================================
#Arquivo: telas.py
# Disciplina: 2026-PCAP 
# Aula: 20
# Autor: Maria EduardaDenck
# Data: 2026.08.04
# Conceitos:      
# ==============================================

# Definição da moldura caracteres e tamanho
CAR =  '#'
TAM = 60

# Desenha uma linha na tela 
def linha():
    print(CAR * TAM)

# Desenha um texto entre linhas
def titulo(texto):
    linha()
    print(texto.center(TAM))
    linha()

