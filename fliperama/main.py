# ==============================================
#Arquivo: main.py
# Disciplina: 2026-PCAP 
# Aula: 20
# Autor: Maria Eduarda Denck
# Data: 2026.08.04
# Conceitos:      
# ==============================================

# Importar funçõe de arquivos (módulos)
from telas import titulo, linha
from adivihe import jogar_adivinhe
from ppt import jogar_ppt
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores
from modulos import ler_opcao 
NOME_DO_DONO = 'MARIAA'
OPCOES = ['0', '1', '2', '3', '4']

vezes_jogado = carregar_placar()
jogadores = carregar_jogadores()
while True: 
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)
    print('[1] - Jogo Adivinhe o Número')
    print('[2] - Pedra-Papel-Tesoura')
    print('[3] - Par ou Impar')
    print('[4] Jogadores')
    print('[0] - Sair do Fliperama')
    linha()

    opcao = ler_opcao('Escolha uma opção', OPCOES)

    if opcao == '0':
        salvar_placar(vezes_jogado)
        salvar_jogadores(jogadores)
        print('Até a próxima!')
        break

    if opcao == '4':
        menu_jogadores(jogadores)
    else:
        indice = int(opcao) - 1
    vezes_jogado[indice] = vezes_jogado[indice] + 1

    if opcao == '1':
        jogar_adivinhe()
    elif opcao == '2':
        titulo('PEDRA-PAPEL-TESOURA entra na atividade 13')
        jogar_ppt()
    else:
        titulo('PAR OU IMPAR entra na atividade 13')
    indice = int(opcao) - 1
    vezes_jogado[indice] = vezes_jogado[indice] + 1

NOMES_DOS_JOGOS = ['Adivinhe o Numero', 'Pedra-Papel-Tesoura', 'Par ou Impar']
vezes_jogado = [0, 0, 0]

def mostrar_placar(): 
    titulo('PLACAR')
    for i in range(3):
        print(NOMES_DOS_JOGOS[i] + ': ' + str(vezes_jogado[i]) + 'x')

        