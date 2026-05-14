'''
Problema: beecrowd | 1014
Data: 2026.05.7
'''

# Objetivo: Calcular o consumo médio de um automóvel em km/l 

# --- ANÁLISE (LIAC) ---
# Entrada: X é distância total em percorrida (inteiro em km) e Y o total de combustIvel gasto (float, em litros)
# Processamento: consumo = X / Y
# Saída: consumo com 3  casas decimais seguido de "consumo"

# Lê a distância total percorrida em km (tipo inteiro)
X = int(input())

# Lê o total de combustível gasto em litros (tipo ponto flutuante)
Y = float(input())

# calcula o consumo médio: quilômetros divididos por litros
consumo = X / Y  

# Exibe o resultado com 3 casas decimais e a unidade km/l
print(f"{consumo:.3f} km/l")
      