'''
Problema: beecrowd | 1009 
Data: 2026.05.14
Estudante: Maria Eduarda Denck
'''
# Objetivo: Ler nome, salário fixo (float), total de vendas efetuadas (float)

# --- ANÁlise (LIAC) ---
# Entrada: nome (texto) salário fixo (float), total de vendas efetuadas (float)
# Processamento: comissão = vendas * 0.15 - total = salário fixo + comissão
# Saída: exibir no formato exato "TOTAL = R$ valor" com 2 casas decimais

# input() sem conversão - retorna o nome como texto (str) 
n = input()

# float(input()) - lê valores monetários (podem ter casas decimais)
s = float(input())
v = float(input())

# o vendedor ganha 15% de comissão sobre o total de vendas 
c = v * 0.15 

# total a receber = salário fixo + comissão
st = s + c

# :.2f dentro da f-string - formata o número com exatamente 2 casas decimais 
print(f"TOTAL = R$ {st:.2f}")