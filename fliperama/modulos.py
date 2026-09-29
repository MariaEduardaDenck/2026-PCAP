# ==============================================
#Arquivo: main.py
# Disciplina: 2026-PCAP 
# Aula: 20
# Autor: Maria Eduarda Denck
# Data: 2026.08.04
# Conceitos:      
# ==============================================

def ler_opcao(mensagem, validas):
    resposta = input(mensagem + ': ').strip()
    while resposta not in validas: 
        print('Opção Inválida! Tente Novamente.')
        resposta = input(mensagem + ': ').strip()
    return resposta

def ler_numero (mensagem, minimo, maximo):
    numeros = []
    for n in range(minimo, maximo + 1):
        numeros.append(str(n))
    return int(ler_opcao(mensagem, numeros))

def ler_texto(mensagem):
    # So devolve quando o texto nao estiver vazio.
    resposta = input(mensagem + ': ').strip()
    while resposta == '':
        print('nao pode ficar e branco! Tente denovo.')
        resposta = input(mensagem + ': ').strip()
    return resposta