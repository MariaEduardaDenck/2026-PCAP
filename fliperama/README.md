# Fliperama do MARIAA

Um fliperama de terminal com três jogos, placar que nnao esquece e cadstro de jogadores. Projeto da disciplina PCAP, 1° ano do Tecnico em Informatica do IFPR.

## O que ele faz

- Três jogos pelo menu: Adivinhe o numero, Pedra-Papel-Tesoura e Par ou Impar
- Placar que conta quantas vezes cada jogo foi jogado e continua contando depois de fechar o programa
- Cadastro de jogadores: cadastrar, listar, alterar e excluir

## Como rodar

'''
cd fliperama
python3 main.py
'''

## Os arquivos

- 'main.py' - o gabinete: menu, placar e chamadas
- 'telas.py' - ferramentas visuais
- 'modulos.py' - ferramentas de logica: as tres funcoes que perguntam e conferem
- 'placar.py' - quantas partidas cadsa jogo teve
- 'jogadores.py' - quem sao os jogadores
- 'adivinhe.py' - 'ppt.py', 'parimpar.py' - um arquivo por jogo
- 'placar.csv' e 'jogadores.csv' - os dados, que nascem sozinhos

A função 'ler_texto' ficou no 'modulos.py' porque tem mais textos para ler nos outros, entao ele nao é apenas de um, mas sim de quase todos

## De onde ele veio

- Aula 20: os tres jogos viraram um programa só, com modulos e menu
- Aula 21: entrou o pedra-papel-tesoura e o placar passou a sobreviver
- Aula 22: entrou o cadastro de jogadores, com as quatro operações
- Aula 23: campo em branco barrado e o projeto documentado

## O que ainda não funciona

- Nome com vígula quebra a linha do arquivo porque a vírgula é o separador
- O placar.






## Autoavaliacao

Conceito que eu acho que a minha entrega vale: [A, B ou C] C/D. (ta mais pra D).

### Mapa do projeto: onde esta cada coisa

| O que | Arquivo | Funcao |
|---|---|---|
| Adivinhe o Numero | `adivinhe.py` | `jogar_adivinhe` |
| Pedra-Papel-Tesoura | `ppt.py` | `jogar_ppt` |
| Par ou Impar | `parimpar.py` | `jogar_parimpar` |
| [NOME DO MEU JOGO] | `meujogo.py` | `jogar_meujogo` |
| Cadastro de jogadores | `jogadores.py` | `menu_jogadores` |
| Ranking Top 10 | `jogadores.py` | `listar` |
| Placar que sobrevive | `placar.py` | `salvar_placar`, `carregar_placar` |

### Criterio por criterio: o nivel e a prova

| Criterio | Nivel | Onde esta a prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura e registro | [A/B/C] | [arquivo, linha] | C
| 2. As quatro operacoes | [A/B/C] | [arquivo, linha] | C
| 3. Busca e indice | [A/B/C] | [arquivo, linha] | C/D
| 4. Persistencia e primeira execucao | [A/B/C] | [arquivo, linha] | D
| 5. Documentacao e autoavaliacao | [A/B/C] | [arquivo, linha] | C
| 6. Jogo autoral e reuso | [A/B/C] | [arquivo, linha] | DDDDDDDDDDDDDDDD

### Usei IA?
não.
