'''
Problema: beecrowd | 1021 - Notas e Moedas
Data: 2026.04.30
Estudante: Maria Eduarda Denck 
'''
# Objetivo: Ler um valor monetário e decompô-lo no MENOR número possível
#           de nots (100, 50, 20, 10, 5, 2, 1) e moedas (0.50, 0.25, 0.10, 0.05, 0.01)

# --- ANÁLISE (LIAC)
# Entrada: um valor monetário com 2 casas decimais (ex.: 576.73)
# Processamento: separar parte inteira (reais - notas) e parte decimal (centávos - moedas);
#                usar divisão inteira (//) para decobrir QUANTAS unidades cabem
#                e o resto da divisão (%) para guardar o que SOBROU para a próxima troca
# Saída: lista formada de notas e moedas, na ordem do maior para o menor valor

# input() lê o valor como texto (ex.: "576.73"); split(".") corta no ponto 
# e devolve uma LISTA com 2 pedaços: ["576", "73"]
# Atribuição múltipla - n recebe o 1° pedaço (reais), m recebe o 2º pedaço (centavos) 
n,m =input().split(".")

# Converte os pedaços de texto para inteiro, pois faremoss contas com eles 
n = int(n) # reais (parte inteira do valor)
m = int(m) # centavos (parte decimal)

# Decomposição dos REAIS em notas - sempre da maior para a menor: 
# // é a divisão INTEIRA (descarta o decimal) - diz QUANTAS  notas daquele valor cabem
# % é o RESTO da divisão - guarda o que sobrou para a próxima troca 

n100 = n // 100; n = n % 100 # quantas notas de 100 cabem; n vira o resto 
n50 = n  //  50; n = n  % 50 # quantas notas de 50 cabem no que sobrou
n20 = n  //  20; n = n  % 20 # quantas notas de 20 cabem no que sobrou
n10 = n  //  10; n = n  % 10 # quantas notas de 10 cabem no que sobrou
n05 = n  //  5; n = n  % 5 # quantas notas de 5 cabem no que sobrou
n02 = n  //  2; n = n  % 2 # quantas notas de 2 cabem no que sobrou
n01 = n                 # o que restou são notas de 1 real 

# Decomposição dos CENTAVOS em moedas - mesma lógica agora em centavos
# (50 centavos, 25 centavos, 10 centavos, 5 centavos, 1 centavo)
m50 = m // 50; m = m % 50 
m25 = m // 25; m = m % 25
m10 = m // 10; m = m % 10
m05 = m // 5; m = m % 5
m01 = m/* ==========================================================================
   CONTAINER DE BOTÕES (AÇÕES DO CARD)
   ========================================================================== */
.card-actions {
    display: flex;
    gap: 10px;
    width: 100%;
    margin-top: 12px;
}

.card-actions a {
    flex: 1;
    display: inline-flex;
    justify-content: center;
    align-items: center;

    padding: 11px 14px;
    border-radius: var(--radius-md, 10px); /* Usa a variável do tema principal, se não achar, usa 10px */

    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    text-decoration: none;
    
    color: #ffffff !important; /* Garante que nunca vai herdar o azul padrão de links */
    
    transition: cubic-bezier(0.4, 0, 0.2, 1) 0.25s;
    box-shadow: 0 0 12px rgba(0, 0, 0, 0.5);
    text-align: center;
}

/* Força a cor branca em todos os estados padrão do navegador */
.card-actions a:link,
.card-actions a:visited,
.card-actions a:active {
    color: #ffffff !important;
}

/* ==========================================================================
   ALTERAR (ROXO NEON / ENERGIA VIVA)
   ========================================================================== */
.btn-alterar {
    background: linear-gradient(to bottom, #a61aff, #4c008f);
    border: 1px solid rgba(166, 26, 255, 0.4);
}

.btn-alterar:hover {
    background: linear-gradient(to bottom, #bd59ff, #6200b3);
    border-color: rgba(166, 26, 255, 0.7);
    box-shadow: 
        0 0 15px rgba(166, 26, 255, 0.45),
        0 0 30px rgba(166, 26, 255, 0.2);
    transform: translateY(-2px);
}

/* ==========================================================================
   EXCLUIR (ROXO PROFUNDO / VAZIO ESCURO)
   ========================================================================== */
.btn-excluir {
    background: linear-gradient(to bottom, #1d0033, #08050d);
    border: 1px solid rgba(166, 26, 255, 0.2);
}

.btn-excluir:hover {
    background: linear-gradient(to bottom, #3b0066, #140024);
    border-color: rgba(166, 26, 255, 0.5);
    box-shadow: 
        0 0 18px rgba(166, 26, 255, 0.3),
        0 0 35px rgba(0, 0, 0, 0.6);/* ==========================================================================
   CONTAINER DE BOTÕES (AÇÕES DO CARD)
   ========================================================================== */
.card-actions {
    display: flex;
    gap: 10px;
    width: 100%;
    margin-top: 12px;
}

.card-actions a {
    flex: 1;
    display: inline-flex;
    justify-content: center;
    align-items: center;

    padding: 11px 14px;
    border-radius: var(--radius-md, 10px); /* Usa a variável do tema principal, se não achar, usa 10px */

    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    text-decoration: none;
    
    color: #ffffff !important; /* Garante que nunca vai herdar o azul padrão de links */
    
    transition: cubic-bezier(0.4, 0, 0.2, 1) 0.25s;
    box-shadow: 0 0 12px rgba(0, 0, 0, 0.5);
    text-align: center;
}

/* Força a cor branca em todos os estados padrão do navegador */
.card-actions a:link,
.card-actions a:visited,
.card-actions a:active {
    color: #ffffff !important;
}

/* ==========================================================================
   ALTERAR (ROXO NEON / ENERGIA VIVA)
   ========================================================================== */
.btn-alterar {
    background: linear-gradient(to bottom, #a61aff, #4c008f);
    border: 1px solid rgba(166, 26, 255, 0.4);
}

.btn-alterar:hover {
    background: linear-gradient(to bottom, #bd59ff, #6200b3);
    border-color: rgba(166, 26, 255, 0.7);
    box-shadow: 
        0 0 15px rgba(166, 26, 255, 0.45),
        0 0 30px rgba(166, 26, 255, 0.2);
    transform: translateY(-2px);
}

/* ==========================================================================
   EXCLUIR (ROXO PROFUNDO / VAZIO ESCURO)
   ========================================================================== */
.btn-excluir {
    background: linear-gradient(to bottom, #1d0033, #08050d);
    border: 1px solid rgba(166, 26, 255, 0.2);
}

.btn-excluir:hover {
    background: linear-gradient(to bottom, #3b0066, #140024);
    border-color: rgba(166, 26, 255, 0.5);
    box-shadow: 
        0 0 18px rgba(166, 26, 255, 0.3),
        0 0 35px rgba(0, 0, 0, 0.6);
    transform: translateY(-2px);
}
    transform: translateY(-2px);
}

print('NOTAS:') 
print(f'{n100} nota(s) de R$ 100.00')
print(f'{n50} nota(s) de R$ 50.00')
print(f'{n20} nota(s) de R$ 20.00')
print(f'{n10} nota(s) de R$ 10.00')
print(f'{n05} nota(s) de R$ 5.00')
print(f'{n02} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{n01} moeda(s) de R$ 1.00')
print(f'{m50} moeda(s) de R$ 0.50')
print(f'{m25} moeda(s) de R$ 0.25')
print(f'{m10} moeda(s) de R$ 0.10')
print(f'{m05} moeda(s) de R$ 0.05')
print(f'{m01} moeda(s) de R$ 0.01')