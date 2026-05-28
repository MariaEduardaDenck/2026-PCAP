''' 
Problema: beecrowd | 1050
Data: 2026.05.15
Estudante: Maria Eduarda Denck
'''
# objuetivo:? ler um código ddd e informar a qual cidade ele pertence

# --- ANÁLISE (LIAC) ---
# entrada: um número inteiro representando  código ddd
# processamento: comparar o DDD lido com cada código da tabela usando if/elif/else
# saída: nome da cidade correspondente , ou "DDD nao cadastrado" se não encontrado

DDD = int(input())

if DDD == 61:
    print("Brasilia")
elif DDD == 71: 
    print("Salvador")
elif DDD == 11:
    print("Sao Paulo")
elif DDD == 21:
    print("Rio de Janeiro")
elif DDD == 32:
    print("Juiz de Fora")
elif DDD == 19:
    print("Campinas")
elif DDD == 27:
    print("Vitoria")
elif DDD == 31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")