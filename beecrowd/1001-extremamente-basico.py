'''
Problema: beecrowd | 1001
Data: 2026.04.09
Estudante: Maria Eduarda Denck
'''
# Objetivo: Ler dois inteiros nas variáveis A e B, clacular a soma em X e exibir o resultado

# --- ANÁLISE (LIAC) --- 
# Entrada: dois números inteiros, cada um em uma linha separada
# Processamento: spmar A + B e armazenar em X
# Saída: exibir no formato exato "X = valor" (espaços ao redor do =, sem mensagens extras)

# int()    - converte o texto lido para número inteiro
# input()  - lê o valor fornecido (digitado ou pelo Beecrowd)
# int(input()) - lê e converte tudo em uma única intrução
A = int(input())
B =int (input())

# O enunciado especifica explicitamente as variáveis A, B e X - seguir à risca
X = A + B

# f-string: insere o valor de X dentro do texto com {}
# Atenção: espaço antes e depois do = é obrigatório conforme o enunciado
print(f"X = {X}")