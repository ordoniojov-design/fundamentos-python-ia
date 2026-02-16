# Instala o pacote watermark (comando mágico do Jupyter) - opcional, pode ser comentado se não usar Jupyter
# !pip install -q -U watermark

# Importando as bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Os comandos a seguir são específicos do Jupyter (extensão watermark). Se não estiver no Jupyter, comente-os.
# %reload_ext watermark
# %watermark -a "Data Science Academy"
# %watermark --iversions

# Configurando o estilo dos gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# --- Geração de Dados Fictícios Coerentes ---
print("\nGerando conjunto de dados fictícios...")

# Define a semente para resultados reproduzíveis
np.random.seed(42)

# Criando um dicionário de dados
data = {
    'ID_Pedido': range(1001, 1101),
    'Data_Compra': pd.to_datetime(pd.date_range(start='2026-07-01', periods=100, freq='D')) - pd.to_timedelta(np.random.randint(0, 30, size=100), unit='d'),
    'Cliente_ID': np.random.randint(100, 150, size=100),
    'Produto': np.random.choice(['Smartphone', 'Notebook', 'Fone de Ouvido', 'Smartwatch', 'Teclado Mecânico'], size=100),
    'Categoria': ['Eletrônicos', 'Eletrônicos', 'Acessórios', 'Acessórios', 'Acessórios'] * 20,
    'Quantidade': np.random.randint(1, 5, size=100),
    'Preco_Unitario': [5999.90, 8500.00, 799.50, 2100.00, 850.00] * 20,
    'Status_Entrega': np.random.choice(['Entregue', 'Pendente', 'Cancelado'], size=100, p=[0.8, 0.15, 0.05])
}

# Criando o dataframe a partir do dicionário
df_vendas = pd.DataFrame(data)

# --- Introduzindo Problemas nos Dados para o Exercício ---
print("\nIntroduzindo problemas nos dados para a limpeza...\n")

# 1. Valores Ausentes (NaN)
df_vendas.loc[5:10, 'Quantidade'] = np.nan
df_vendas.loc[20:22, 'Status_Entrega'] = np.nan
df_vendas.loc[30, 'Cliente_ID'] = np.nan

# 2. Dados Duplicados
df_vendas = pd.concat([df_vendas, df_vendas.head(3)], ignore_index=True)

# 3. Tipos de Dados Incorretos
df_vendas['Preco_Unitario'] = df_vendas['Preco_Unitario'].astype(str)
df_vendas.loc[15, 'Preco_Unitario'] = 'valor_invalido'                   # Simulando um erro de digitação
df_vendas['Cliente_ID'] = df_vendas['Cliente_ID'].astype(str)

# 4. Outliers
df_vendas.loc[50, 'Quantidade'] = 50 # Um valor claramente fora do padrão

print("Dados gerados com sucesso!\n")

# Primeiras linhas
print("Primeiras linhas do DataFrame:")
print(df_vendas.head())

# Últimas linhas
print("\nÚltimas linhas do DataFrame:")
print(df_vendas.tail())

print("\n--- Informações Gerais do DataFrame (df_vendas.info()) ---\n")
df_vendas.info()

print("\n--- Verificando valores ausentes ---\n")
print(df_vendas.isna().sum())

print("\n--- Verificando a presença de registros duplicados ---\n")
print(f"Número de linhas duplicadas: {df_vendas.duplicated().sum()}")

print("\n--- Estatísticas descritivas para colunas numéricas ---\n")
print(df_vendas.describe())

print("\n--- Estatísticas descritivas para colunas categóricas ---\n")
print(df_vendas.describe(include=[object]))

print("\n--- Tipos de dados ---\n")
print(df_vendas.dtypes)

# Copiando o DataFrame para manter o original intacto
df_limpo = df_vendas.copy()

# --- 1. Corrigindo Tipos de Dados ---
print("Corrigindo tipos de dados...")
# Convertendo 'Preco_Unitario' para numérico, tratando erros
df_limpo['Preco_Unitario'] = pd.to_numeric(df_limpo['Preco_Unitario'], errors='coerce')

# Convertendo 'Cliente_ID' para numérico, tratando erros
df_limpo['Cliente_ID'] = pd.to_numeric(df_limpo['Cliente_ID'], errors='coerce').astype('Int64')

print("Tipos de dados após correção:")
print(df_limpo.dtypes)

# --- 2. Tratando Valores Ausentes (NaN) ---
print("Tratando valores ausentes...")
# Para 'Quantidade', vamos preencher com a mediana
mediana_qtd = df_limpo['Quantidade'].median()
df_limpo.fillna({'Quantidade': mediana_qtd}, inplace=True)

# Para 'Status_Entrega', preencher com a moda
moda_status = df_limpo['Status_Entrega'].mode()[0]
df_limpo['Status_Entrega'] = df_limpo['Status_Entrega'].fillna(moda_status)

# Para 'Preco_Unitario' e 'Cliente_ID', remover linhas com NaN
df_limpo.dropna(subset=['Preco_Unitario', 'Cliente_ID'], inplace=True)

# --- 3. Removendo Duplicatas ---
print("Removendo registros duplicados...")
df_limpo.drop_duplicates(inplace=True)

# --- 4. Tratando Outliers ---
print("Tratando outliers...")
# Visualizar o outlier na coluna 'Quantidade'
sns.boxplot(x=df_limpo['Quantidade'])
plt.title('Boxplot de Quantidade (Antes de tratar outlier)')
plt.show()

# Remover valores além de 3 desvios padrão da média
limite_superior = df_limpo['Quantidade'].mean() + 3 * df_limpo['Quantidade'].std()
df_limpo = df_limpo[df_limpo['Quantidade'] < limite_superior]

# Verificar o resultado
sns.boxplot(x=df_limpo['Quantidade'])
plt.title('Boxplot de Quantidade (Depois de tratar outlier)')
plt.show()

# --- Verificação Final ---
print("\n--- Verificação Final Pós-Limpeza ---\n")
df_limpo.info()
print("\nValores ausentes restantes:\n", df_limpo.isna().sum())
print(f"\nLinhas duplicadas restantes: {df_limpo.duplicated().sum()}")

# --- Feature Engineering: Criando uma nova coluna 'Total_Venda' ---
df_limpo['Total_Venda'] = df_limpo['Quantidade'] * df_limpo['Preco_Unitario']
print("DataFrame após engenharia de atributos (primeiras linhas):")
print(df_limpo.head())

# 1. Qual o total de receita?
receita_total = df_limpo['Total_Venda'].sum()
print(f"A receita total da loja foi de: R$ {receita_total:,.2f}")

# 2. Qual a receita total por categoria de produto?
receita_por_categoria = df_limpo.groupby('Categoria')['Total_Venda'].sum().sort_values(ascending=False)
print("\n--- Receita Total por Categoria ---\n")
print(receita_por_categoria)

# 3. Qual o produto mais vendido em quantidade?
produto_mais_vendido = df_limpo.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
print("\n--- Total de Unidades Vendidas por Produto ---\n")
print(produto_mais_vendido)

# 4. Análise de vendas ao longo do tempo
# Agrupando as vendas por dia
vendas_por_dia = df_limpo.set_index('Data_Compra').resample('D')['Total_Venda'].sum()
print("\n--- Resumo de Vendas por Dia (Primeiros 5 dias) ---\n")
print(vendas_por_dia.head())

# Gráfico 1: Receita por Categoria
receita_por_categoria.plot(kind='bar', color='skyblue')
plt.title('Receita Total Por Categoria de Produto')
plt.ylabel('Receita (R$)')
plt.xlabel('Categoria')
plt.xticks(rotation=0)
plt.show()

# Gráfico 2: Quantidade Vendida por Produto
produto_mais_vendido.plot(kind='barh', color='salmon')
plt.title('Quantidade de Unidades Vendidas Por Produto')
plt.ylabel('Produto')
plt.xlabel('Quantidade Vendida')
plt.gca().invert_yaxis() # Inverte o eixo para o maior valor ficar no topo
plt.show()

# Gráfico 3: Tendência de Vendas ao Longo do Tempo
vendas_por_dia.plot(kind='line', marker='.', linestyle='-')
plt.title('Tendência de Vendas Diárias')
plt.ylabel('Receita (R$)')
plt.xlabel('Data da Compra')
plt.grid(True)
plt.show()

# Gráfico 4: Distribuição do Status de Entrega
status_counts = df_limpo['Status_Entrega'].value_counts()
plt.pie(
    status_counts,
    labels=status_counts.index,
    autopct='%1.1f%%',
    startangle=180,
    colors=['lightgreen', 'orange', 'lightcoral']
)
plt.title('\nDistribuição do Status de Entrega')
plt.show()

# Gráfico 4 (versão 3D): Distribuição do Status de Entrega com destaque para a maior fatia
status_counts = df_limpo['Status_Entrega'].value_counts()
maior_idx = status_counts.argmax()
explode = [0.1 if i == maior_idx else 0 for i in range(len(status_counts))]
plt.figure(figsize=(6,6))
plt.pie(
    status_counts,
    labels=status_counts.index,
    autopct='%1.1f%%',
    startangle=180,
    colors=['lightgreen', 'orange', 'lightcoral'],
    explode=explode,
    shadow=True
)
plt.title('\nDistribuição do Status de Entrega\n')
plt.axis('equal')
plt.show()