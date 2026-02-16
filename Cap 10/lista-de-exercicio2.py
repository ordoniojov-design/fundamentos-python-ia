# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.weightstats import DescrStatsW

# Exercício 1: Análise de Distribuição de Receita Mensal

# Seed
np.random.seed(10)

# Cria dados de receita
receita = np.random.normal(50000, 8000, 100)

# Cria o dataframe
df = pd.DataFrame({'Receita': receita})

# Visualiza os dados
df.head()

# Solução
# Estatísticas descritivas
media = df['Receita'].mean()
mediana = df['Receita'].median()
desvio = df['Receita'].std()
assimetria = df['Receita'].skew()
curtose = df['Receita'].kurtosis()

print("=== Relatório de Receita Mensal ===")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desvio-padrão: {desvio:.2f}")
print(f"Assimetria: {assimetria:.3f}")
print(f"Curtose: {curtose:.3f}")

# Visualização
plt.figure(figsize=(8,4))
sns.histplot(df['Receita'], kde=True, bins=15, color='skyblue')
plt.axvline(media, color='red', linestyle='--', label=f'Média = {media:.0f}')
plt.axvline(mediana, color='green', linestyle='-', label=f'Mediana = {mediana:.0f}')
plt.title('Distribuição da Receita Mensal')
plt.xlabel('Receita (R$)')
plt.ylabel('Frequência')
plt.legend()
plt.show()

# Interpretação
print("\nInterpretação:")
if abs(assimetria) < 0.5:
    print("A distribuição é aproximadamente simétrica (assimetria próxima de zero).")
elif assimetria > 0:
    print("A distribuição possui assimetria positiva (cauda à direita).")
else:
    print("A distribuição possui assimetria negativa (cauda à esquerda).")

if curtose > 0:
    print("A distribuição é leptocúrtica (caudas mais pesadas que a normal).")
elif curtose < 0:
    print("A distribuição é platicúrtica (caudas mais leves que a normal).")
else:
    print("A distribuição é mesocúrtica (similar à normal).")

if abs(media - mediana) < 0.1 * desvio:
    print("A média representa bem o centro dos dados, pois está próxima da mediana.")
else:
    print("A média pode ser influenciada por valores extremos; a mediana é uma medida mais robusta.")

# Exercício 2: Desempenho por Segmento de Cliente

# Seed
np.random.seed(5)

# Dataframe
clientes = pd.DataFrame({
    'Grupo': ['Novo']*80 + ['Antigo']*80,
    'Gasto': np.concatenate([np.random.normal(180, 40, 80),
                             np.random.normal(230, 35, 80)])
})

# Visualiza os dados
clientes.sample(10)

# Solução
# Estatísticas por grupo
estatisticas = clientes.groupby('Grupo')['Gasto'].agg(['mean', 'median', 'std'])
print("\n=== Estatísticas por Grupo ===")
print(estatisticas)

# Boxplot comparativo
plt.figure(figsize=(6,4))
sns.boxplot(x='Grupo', y='Gasto', data=clientes, palette='Set2')
plt.title('Distribuição do Gasto por Grupo de Cliente')
plt.ylabel('Gasto (R$)')
plt.show()

# Discussão
media_novo = clientes[clientes['Grupo']=='Novo']['Gasto'].mean()
media_antigo = clientes[clientes['Grupo']=='Antigo']['Gasto'].mean()
std_novo = clientes[clientes['Grupo']=='Novo']['Gasto'].std()
std_antigo = clientes[clientes['Grupo']=='Antigo']['Gasto'].std()

print("\nDiscussão:")
print(f"Clientes novos gastam em média R$ {media_novo:.2f} (desvio {std_novo:.2f}).")
print(f"Clientes antigos gastam em média R$ {media_antigo:.2f} (desvio {std_antigo:.2f}).")
print(f"A diferença média é de R$ {media_antigo - media_novo:.2f}.")
if std_novo > std_antigo:
    print("Clientes novos apresentam maior variabilidade nos gastos.")
else:
    print("Clientes antigos apresentam maior variabilidade nos gastos.")

# Verificar sobreposição
min_antigo = clientes[clientes['Grupo']=='Antigo']['Gasto'].min()
max_novo = clientes[clientes['Grupo']=='Novo']['Gasto'].max()
if max_novo > min_antigo:
    print("Há sobreposição entre os grupos, ou seja, alguns clientes novos gastam tanto quanto antigos.")
else:
    print("Os grupos são bem separados, sem sobreposição.")

# Exercício 3: Correlação Entre Horas de Estudo e Nota

# Seed
np.random.seed(2)

# Dados
horas = np.random.uniform(1, 10, 50)
notas = 5*horas + np.random.normal(0, 5, 50)

# Dataframe
df = pd.DataFrame({'Horas': horas, 'Nota': notas})

# Visualiza os dados
df.head()

# Solução
# Correlação de Pearson
corr = df['Horas'].corr(df['Nota'])
print(f"\n=== Correlação entre Horas de Estudo e Nota ===")
print(f"Coeficiente de correlação de Pearson: {corr:.3f}")

# Gráfico de dispersão com linha de regressão
plt.figure(figsize=(6,4))
sns.regplot(x='Horas', y='Nota', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Relação entre Horas de Estudo e Nota')
plt.xlabel('Horas de Estudo')
plt.ylabel('Nota')
plt.show()

# Interpretação
print("\nInterpretação:")
if corr > 0:
    print("Correlação positiva: quanto mais horas de estudo, maior a nota.")
elif corr < 0:
    print("Correlação negativa: mais horas de estudo estão associadas a notas menores.")
else:
    print("Correlação nula: não há relação linear entre horas e nota.")

if abs(corr) >= 0.7:
    print("A correlação é forte.")
elif abs(corr) >= 0.3:
    print("A correlação é moderada.")
else:
    print("A correlação é fraca.")

print("Em termos práticos, o tempo de estudo parece influenciar positivamente o desempenho dos alunos.")

# Exercício 4: Variação Semanal de Vendas

# Seed
np.random.seed(3)

# Dados
dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
vendas = pd.DataFrame({
    'Dia': np.random.choice(dias, 200),
    'Vendas': np.random.normal(1000, 150, 200)
})

# Visualiza os dados
vendas.head()

# Solução
# Agrupar por dia da semana
resumo_dias = vendas.groupby('Dia')['Vendas'].agg(['mean', 'std']).reindex(dias)

print("\n=== Média e Desvio Padrão de Vendas por Dia ===")
print(resumo_dias)

# Gráfico de barras com barras de erro
plt.figure(figsize=(8,5))
plt.bar(resumo_dias.index, resumo_dias['mean'], yerr=resumo_dias['std'], capsize=5, color='lightcoral', edgecolor='black')
plt.title('Vendas Médias por Dia da Semana com Desvio Padrão')
plt.xlabel('Dia')
plt.ylabel('Vendas Médias (R$)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Identificar dias de maior e menor performance
dia_max = resumo_dias['mean'].idxmax()
dia_min = resumo_dias['mean'].idxmin()
print(f"\nDia de maior venda média: {dia_max} (R$ {resumo_dias.loc[dia_max, 'mean']:.2f})")
print(f"Dia de menor venda média: {dia_min} (R$ {resumo_dias.loc[dia_min, 'mean']:.2f})")

# Estabilidade
coef_variacao = resumo_dias['std'] / resumo_dias['mean'] * 100
media_cv = coef_variacao.mean()
print(f"Coeficiente de variação médio: {media_cv:.1f}%")
if media_cv < 10:
    print("As vendas são estáveis ao longo da semana (baixa variabilidade relativa).")
elif media_cv < 20:
    print("As vendas apresentam variabilidade moderada.")
else:
    print("As vendas são bastante instáveis ao longo da semana.")

# Exercício 5: Estimativa da Média com Intervalo de Confiança (Statsmodels)

# Seed
np.random.seed(7)

# Conjunto de dados
alturas = np.random.normal(1.75, 0.08, 40)

# Visualiza os dados
alturas

# Solução
# Criar objeto DescrStatsW
dstats = DescrStatsW(alturas)

# Calcular média e intervalo de confiança de 95%
media_alt = dstats.mean
ic_alt = dstats.tconfint_mean(alpha=0.05)  # 95% CI

print("\n=== Estimativa da Altura Média dos Colaboradores ===")
print(f"Média amostral: {media_alt:.3f} m")
print(f"Intervalo de confiança de 95%: ({ic_alt[0]:.3f}, {ic_alt[1]:.3f}) m")

# Interpretação
print("\nInterpretação:")
print("Com base na amostra de 40 colaboradores, estimamos que a altura média populacional")
print(f"esteja entre {ic_alt[0]:.3f} m e {ic_alt[1]:.3f} m, com 95% de confiança.")
print("Isso significa que, se repetíssemos o processo de amostragem muitas vezes,")
print("em 95% das vezes o intervalo construído conteria a verdadeira média populacional.")