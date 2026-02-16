# Exercício 1: Selecionando uma Coluna Específica (Nível Baby)
import numpy as np

# Cria a matriz
matriz = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# Solução - Selecionar terceira coluna (índice 2)
terceira_coluna = matriz[:, 2]
print(f"Terceira coluna: {terceira_coluna}")
# Saída: [ 3  7 11 15]

# Exercício 2: Extraindo um Bloco (Submatriz) (Nível Aprendiz)
# Extrair o bloco central 2x2 (valores 6, 7, 10, 11)
bloco_central = matriz[1:3, 1:3]
print("\nBloco central 2x2:")
print(bloco_central)
# Saída:
# [[ 6  7]
#  [10 11]]

# Exercício 3: Produto de Matrizes (Nível Iniciante)
A = np.array([[1, 2, 3], [4, 5, 6]])       # Matriz 2x3
B = np.array([[7, 8], [9, 10], [11, 12]])  # Matriz 3x2

# Solução - Produto matricial
produto = np.dot(A, B)
# Alternativa: produto = A @ B
print("\nProduto matricial A * B:")
print(produto)
# Saída:
# [[ 58  64]
#  [139 154]]

# Exercício 4: Selecionando Linhas Pares e Colunas Ímpares (Nível Iniciante Plus)
# Cria a matriz 9x9
matriz2 = np.arange(81).reshape(9, 9)

# Solução - Linhas de índice par, colunas de índice ímpar
resultado = matriz2[::2, 1::2]
print("\nLinhas pares e colunas ímpares:")
print(resultado)
# Saída esperada:
# [[ 1  3  5  7]
#  [19 21 23 25]
#  [37 39 41 43]
#  [55 57 59 61]
#  [73 75 77 79]]

# Exercício 5: Somando Valor a Uma Submatriz (Nível Pro)
# Cria a matriz de zeros
matriz3 = np.zeros((4, 4), dtype=int)

# Solução - Adicionar 5 ao bloco central 2x2
matriz3[1:3, 1:3] += 5
print("\nMatriz com bloco central 2x2 = 5:")
print(matriz3)
# Saída:
# [[0 0 0 0]
#  [0 5 5 0]
#  [0 5 5 0]
#  [0 0 0 0]]

# Exercício 6: Normalização de Uma Matriz (Nível Master)
matriz4 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Solução - Normalização Z-score
media = np.mean(matriz4)
desvio_padrao = np.std(matriz4)
matriz_normalizada = (matriz4 - media) / desvio_padrao
print("\nMatriz original:")
print(matriz4)
print("\nMatriz normalizada (Z-score):")
print(matriz_normalizada)
# Verificando média e desvio da matriz normalizada
print(f"Média da matriz normalizada: {np.mean(matriz_normalizada):.10f}")
print(f"Desvio padrão da matriz normalizada: {np.std(matriz_normalizada):.10f}")

# Exercício 7: Substituindo Valores com Base em Uma Condição (Nível Ninja)
dados = np.arange(16).reshape(4, 4)

# Solução - Criar cópia e substituir valores > 8 por -1
dados_modificados = dados.copy()
dados_modificados[dados_modificados > 8] = -1
print("\nMatriz original:")
print(dados)
print("\nMatriz com valores > 8 substituídos por -1:")
print(dados_modificados)
# Saída esperada:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8 -1 -1 -1]
#  [-1 -1 -1 -1]]

# Exercício 8: Inversa de Uma Matriz (Nível Ninja Pro Master)
A = np.array([[4, 7], [2, 6]])

# Solução - Calcular inversa e verificar
# Primeiro, verificar o determinante (deve ser diferente de zero)
determinante = np.linalg.det(A)
print(f"\nDeterminante da matriz A: {determinante}")

# Calcular a matriz inversa
A_inversa = np.linalg.inv(A)
print("\nMatriz inversa de A:")
print(A_inversa)

# Verificar o produto A * A_inversa (deve resultar na matriz identidade)
identidade = np.dot(A, A_inversa)
print("\nProduto A * A_inversa (deve ser matriz identidade):")
print(np.round(identidade))  # Arredondar para evitar erros de ponto flutuante

# Exercício 9: Resolvendo Um Sistema de Equações Lineares (Nível Ninja Pro Master das Galáxias)
# Sistema:
# 2x + y = 8
# x + 3y = 7

# Solução - Forma matricial Ax = b
A_sistema = np.array([[2, 1], [1, 3]])
b = np.array([8, 7])

# Resolver o sistema
x = np.linalg.solve(A_sistema, b)
print("\nSolução do sistema linear:")
print(f"x = {x[0]:.2f}, y = {x[1]:.2f}")
print(f"Vetor solução: {x}")
# Saída esperada: [3.4 1.2]

# Verificando a solução
verificacao = np.dot(A_sistema, x)
print(f"Verificação (A*x = b): {verificacao}")

# Exercício 10: Extraindo a Borda de Uma Matriz (Nível Ninja Pro Master das Galáxias Plus)
matriz5 = np.arange(25).reshape(5, 5)
print("\nMatriz 5x5:")
print(matriz5)

# Solução - Extrair borda em sentido horário começando pelo canto superior esquerdo
# Método 1: Usando índices
primeira_linha = matriz5[0, :]           # Linha superior
ultima_coluna = matriz5[1:, -1]          # Coluna direita (excluindo primeiro elemento)
ultima_linha = matriz5[-1, -2::-1]       # Linha inferior (em ordem reversa)
primeira_coluna = matriz5[-2:0:-1, 0]    # Coluna esquerda (em ordem reversa, excluindo extremos)

borda = np.concatenate([primeira_linha, ultima_coluna, ultima_linha, primeira_coluna])
print("\nBorda da matriz em sentido horário (Método 1):")
print(borda)

# Método 2: Mais elegante usando índices booleanos e máscara
mascara = np.ones(matriz5.shape, dtype=bool)
mascara[1:-1, 1:-1] = False  # Apenas a borda é True
borda2 = matriz5[mascara]
# Para garantir a ordem correta, precisamos ordenar de forma específica
# Este método é mais complexo, então o Método 1 é mais claro para este caso

# Método 3: Abordagem passo a passo para garantir a ordem correta
linhas, colunas = matriz5.shape
elementos_borda = []

# Linha superior (esquerda para direita)
for j in range(colunas):
    elementos_borda.append(matriz5[0, j])

# Coluna direita (cima para baixo, excluindo primeiro e último)
for i in range(1, linhas - 1):
    elementos_borda.append(matriz5[i, colunas - 1])

# Linha inferior (direita para esquerda)
for j in range(colunas - 1, -1, -1):
    elementos_borda.append(matriz5[linhas - 1, j])

# Coluna esquerda (baixo para cima, excluindo primeiro e último)
for i in range(linhas - 2, 0, -1):
    elementos_borda.append(matriz5[i, 0])

borda3 = np.array(elementos_borda)
print("\nBorda da matriz em sentido horário (Método 3):")
print(borda3)
# Saída esperada: [ 0  1  2  3  4  9 14 19 24 23 22 21 20 15 10  5]