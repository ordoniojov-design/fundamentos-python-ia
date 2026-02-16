# -*- coding: utf-8 -*-
"""
Data Science Academy
Fundamentos de Linguagem Python - Do Básico a Aplicações de IA
Lista 5 de Exercícios - Soluções

Este script contém as soluções completas para os 5 exercícios propostos.
"""

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.weightstats import DescrStatsW

# =============================================================================
# Exercício 1: Análise de Distribuição de Receita Mensal
# =============================================================================

print("="*60)
print("Exercício 1: Análise de Distribuição de Receita Mensal")
print("="*60)

# Seed
np.random.seed(10)

# Cria dados de receita
receita = np.random.normal(50000, 8000, 100)

# Cria o dataframe
df = pd.DataFrame({'Receita': receita})

# Visualiza os dados
print("\nPrimeiras linhas do DataFrame:")
print(df.head())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(df.describe())

# Estatísticas descritivas transpostas
print("\nEstatísticas descritivas (transpostas):")
print(df.describe().T)

# Assimetria e curtose
print("\nAssimetria:", df['Receita'].skew())
print("Curtose:", df['Receita'].kurtosis())

# Interpretação textual (já estava em markdown, mas incluímos como comentário)
print("\nInterpretação:")
print("- Média é o valor obtido somando todos os dados e dividindo pela quantidade de elementos, representando o “centro” dos valores.")
print("- Mediana é o valor central quando os dados são colocados em ordem, separando a metade menor da metade maior.")
print("- Desvio-padrão mede o quanto os valores se afastam da média, quanto maior, mais dispersos estão os dados.")
print("- Assimetria indica se os dados estão distribuídos de forma equilibrada em torno da média; se há cauda mais longa à direita ou à esquerda.")
print("- Curtose mostra o quão “achatada” ou “pontuda” é a distribuição em comparação com a normal; valores altos indicam picos acentuados e caudas longas.")
print("\n- A assimetria de 0.0138 está muito próxima de zero, indicando que a distribuição é praticamente simétrica, ou seja, os valores se distribuem de forma equilibrada em torno da média, sem cauda mais longa à direita ou à esquerda.")
print("- A curtose de 0.1935 também está próxima de zero, sugerindo que a distribuição é mesocúrtica, semelhante à distribuição normal, nem muito pontuda (leptocúrtica), nem muito achatada (platicúrtica).")

# Gráfico da distribuição
sns.histplot(df['Receita'], bins=20, kde=True)
plt.title('Distribuição da Receita Mensal')
plt.show()

# =============================================================================
# Exercício 2: Desempenho por Segmento de Cliente
# =============================================================================

print("\n" + "="*60)
print("Exercício 2: Desempenho por Segmento de Cliente")
print("="*60)

# Seed
np.random.seed(5)

# Dataframe
clientes = pd.DataFrame({
    'Grupo': ['Novo'] * 80 + ['Antigo'] * 80,
    'Gasto': np.concatenate([np.random.normal(180, 40, 80),
                             np.random.normal(230, 35, 80)])
})

# Visualiza os dados
print("\nAmostra dos dados:")
print(clientes.sample(10))

# Estatísticas descritivas por grupo
resumo_clientes = clientes.groupby('Grupo')['Gasto'].describe()
print("\nEstatísticas descritivas por grupo:")
print(resumo_clientes)

print("\nInterpretação:")
print("- Os clientes antigos gastam, em média, mais (232,9) do que os novos (182,7), indicando um perfil de consumo mais elevado. O desvio-padrão é parecido entre os grupos (≈38), mostrando variabilidade semelhante nos gastos.")
print("- No boxplot, deve haver pouca sobreposição, já que as faixas interquartis são diferentes. Isso sugere que, em geral, clientes antigos mantêm gastos consistentemente maiores, enquanto os novos ainda estão em fase de consumo menor, embora com dispersão parecida.")

# Boxplot
sns.boxplot(data=clientes, x='Grupo', y='Gasto')
plt.title('Comparação do Gasto por Segmento')
plt.show()

print("\nExplicação do boxplot:")
print("Um boxplot típico mostra a distribuição dos dados de forma visual e resumida. Ele é composto por uma caixa (box) que representa o intervalo entre o primeiro quartil (Q1) e o terceiro quartil (Q3), ou seja, onde está concentrada metade dos valores.")
print("Dentro da caixa há uma linha central, que indica a mediana, o valor central dos dados.")
print("Os “bigodes” (whiskers) se estendem a partir da caixa até os valores mínimos e máximos dentro de um limite considerado normal.")
print("Pontos que ficam fora desses limites são mostrados como outliers, representando valores atípicos.")
print("Assim, o boxplot permite identificar rapidamente a tendência central, a dispersão e possíveis assimetrias ou outliers em um conjunto de dados.")

# =============================================================================
# Exercício 3: Correlação Entre Horas de Estudo e Nota
# =============================================================================

print("\n" + "="*60)
print("Exercício 3: Correlação Entre Horas de Estudo e Nota")
print("="*60)

# Seed
np.random.seed(2)

# Dados
horas = np.random.uniform(1, 10, 50)
notas = 5*horas + np.random.normal(0, 5, 50)

# Dataframe
df_estudo = pd.DataFrame({'Horas': horas, 'Nota': notas})

# Visualiza os dados
print("\nPrimeiras linhas do DataFrame:")
print(df_estudo.head())

# Correlação de Pearson
print("\nMatriz de correlação:")
print(df_estudo.corr())

print("\nInterpretação:")
print("- O valor 0.914853 representa uma correlação forte e positiva entre horas de estudo e nota. Isso significa que, quanto mais horas o aluno estuda, maior tende a ser sua nota. Como o valor está próximo de 1, a relação é quase linear e direta.")
print("- Mas lembre-se: Correlação não implica causalidade!")

# Gráfico de dispersão com linha de regressão
sns.regplot(data=df_estudo, x='Horas', y='Nota', ci=None, line_kws={'color':'red'})
plt.title('Relação Entre Horas de Estudo e Nota')
plt.show()

# =============================================================================
# Exercício 4: Variação Semanal de Vendas
# =============================================================================

print("\n" + "="*60)
print("Exercício 4: Variação Semanal de Vendas")
print("="*60)

# Seed
np.random.seed(3)

# Dados
dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
vendas = pd.DataFrame({
    'Dia': np.random.choice(dias, 200),
    'Vendas': np.random.normal(1000, 150, 200)
})

print("\nPrimeiras linhas do DataFrame:")
print(vendas.head())

# Média e desvio por dia da semana
resumo_vendas = vendas.groupby('Dia')['Vendas'].agg(['mean','std']).sort_values('mean', ascending=False)
print("\nMédia e desvio-padrão das vendas por dia:")
print(resumo_vendas)

print("\nInterpretação:")
print("- As maiores médias de vendas ocorrem na sexta (1049,8) e no domingo (1034,7), indicando picos próximos ao fim de semana. Já a terça-feira (990,3) tem o menor desempenho.")
print("- O desvio-padrão é moderado, sugerindo variação regular entre os dias, mas um leve aumento de instabilidade nas quintas.")
print("- Em resumo, as vendas se mantêm estáveis ao longo da semana, com melhor performance nos dias próximos ao fim de semana.")

# Gráfico de barras com barras de erro
resumo_vendas['mean'].plot(kind='bar', yerr=resumo_vendas['std'], capsize=4)
plt.title('Média de Vendas Por Dia da Semana')
plt.ylabel('Vendas')
plt.show()

# =============================================================================
# Exercício 5: Estimativa da Média com Intervalo de Confiança (Statsmodels)
# =============================================================================

print("\n" + "="*60)
print("Exercício 5: Estimativa da Média com Intervalo de Confiança")
print("="*60)

np.random.seed(7)
alturas = np.random.normal(1.75, 0.08, 40)

# Estatísticas com DescrStatsW
desc = DescrStatsW(alturas)
print("\nMédia Estimada:", round(desc.mean, 3))
print("Intervalo de Confiança (95%):", desc.tconfint_mean())

print("\nInterpretação:")
print("- A média estimada é 1,742, e o intervalo de confiança de 95% indica que há alta probabilidade de a média real da população estar entre 1,714 e 1,770. Isso mostra uma estimativa precisa, com variação pequena em torno da média.")

print("\n" + "="*60)
print("Fim dos exercícios")
print("="*60)