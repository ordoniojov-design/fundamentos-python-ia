# Mini-Projeto 1 - Análise de Vendas Para Loja de E-commerce

# ============================================
# 1. Importação das Bibliotecas
# ============================================

!pip install -q -U watermark

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta
from matplotlib.ticker import FuncFormatter
import warnings
warnings.filterwarnings('ignore')

%matplotlib inline

np.random.seed(42)
random.seed(42)

%reload_ext watermark
%watermark -a "Data Science Academy"
%watermark --iversions

# ============================================
# 2. Função Para Geração de Dados Fictícios
# ============================================

def dsa_gera_dados_ficticios(num_registros=600):
    print(f"\nIniciando a geração de {num_registros} registros de vendas...")

    produtos = {
        'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
        'Mouse Vertical': {'categoria': 'Acessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
        'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
        'Placa de Vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}
    }

    lista_produtos = list(produtos.keys())

    cidades_estados = {
        'São Paulo': 'SP', 'Rio de Janeiro': 'RJ', 'Belo Horizonte': 'MG',
        'Porto Alegre': 'RS', 'Salvador': 'BA', 'Curitiba': 'PR', 'Fortaleza': 'CE'
    }

    lista_cidades = list(cidades_estados.keys())
    dados_vendas = []
    data_inicial = datetime(2026, 1, 1)

    for i in range(num_registros):
        produto_nome = random.choice(lista_produtos)
        cidade = random.choice(lista_cidades)
        quantidade = np.random.randint(1, 8)
        data_pedido = data_inicial + timedelta(days=int(i/5), hours=random.randint(0, 23))

        if produto_nome in ['Mouse Vertical', 'Teclado Mecânico']:
            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0)
        else:
            preco_unitario = produtos[produto_nome]['preco']

        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100, 150),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade]
        })
    
    print("Geração de dados concluída.\n")
    return pd.DataFrame(dados_vendas)

# ============================================
# 3. Gerar, Carregar e Explorar os Dados
# ============================================

df_vendas = dsa_gera_dados_ficticios(500)

print(type(df_vendas))
print(df_vendas.shape)
print(df_vendas.head())
print(df_vendas.tail())
print(df_vendas.info())
print(df_vendas.describe())
print(df_vendas.dtypes)

# ============================================
# 4. Limpeza, Pré-Processamento e Engenharia de Atributos
# ============================================

df_vendas['Data_Pedido'] = pd.to_datetime(df_vendas['Data_Pedido'])
df_vendas['Faturamento'] = df_vendas['Preco_Unitario'] * df_vendas['Quantidade']
df_vendas['Status_Entrega'] = df_vendas['Estado'].apply(
    lambda estado: 'Rápida' if estado in ['SP', 'RJ', 'MG'] else 'Normal'
)

print(df_vendas.info())
print(df_vendas.head())

# ============================================
# 5. Análise 1 - Top 10 Produtos Mais Vendidos
# ============================================

top_10_produtos = df_vendas.groupby('Nome_Produto')['Quantidade'].sum().sort_values(ascending=False).head(10)
print(top_10_produtos)

sns.set_style("whitegrid")

plt.figure(figsize=(12, 7))
top_10_produtos.sort_values(ascending=True).plot(kind='barh', color='skyblue')
plt.title('Top 10 Produtos Mais Vendidos', fontsize=16)
plt.xlabel('Quantidade Vendida', fontsize=12)
plt.ylabel('Produto', fontsize=12)
plt.tight_layout()
plt.show()

# ============================================
# 6. Análise 2 - Faturamento Mensal
# ============================================

df_vendas['Mes'] = df_vendas['Data_Pedido'].dt.to_period('M')
faturamento_mensal = df_vendas.groupby('Mes')['Faturamento'].sum()
faturamento_mensal.index = faturamento_mensal.index.strftime('%Y-%m')
print(faturamento_mensal.map('R$ {:,.2f}'.format))

plt.figure(figsize=(12, 6))
faturamento_mensal.plot(kind='line', marker='o', linestyle='-', color='green')
plt.title('Evolução do Faturamento Mensal', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Faturamento (R$)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# ============================================
# 7. Análise 3 - Vendas Por Estado
# ============================================

vendas_estado = df_vendas.groupby('Estado')['Faturamento'].sum().sort_values(ascending=False)
print(vendas_estado.map('R$ {:,.2f}'.format))

plt.figure(figsize=(12, 7))
vendas_estado.plot(kind='bar', color=sns.color_palette("husl", 7))
plt.title('Faturamento Por Estado', fontsize=16)
plt.xlabel('Estado', fontsize=12)
plt.ylabel('Faturamento (R$)', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ============================================
# 8. Análise 4 - Faturamento Por Categoria
# ============================================

faturamento_categoria = df_vendas.groupby('Categoria')['Faturamento'].sum().sort_values(ascending=False)
print(faturamento_categoria.map('R$ {:,.2f}'.format))

faturamento_ordenado = faturamento_categoria.sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(12, 7))

def formatador_milhares(y, pos):
    return f'R$ {y/1000:,.0f}K'

ax.yaxis.set_major_formatter(FuncFormatter(formatador_milhares))
faturamento_ordenado.plot(kind='bar', ax=ax, color=sns.color_palette("viridis", len(faturamento_ordenado)))
ax.set_title('Faturamento Por Categoria', fontsize=16)
ax.set_xlabel('Categoria', fontsize=12)
ax.set_ylabel('Faturamento', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# ============================================
# 9. Conclusão
# ============================================

print("\n" + "="*50)
print("ANÁLISE CONCLUÍDA COM SUCESSO!")
print("="*50)
print("\nResumo das análises realizadas:")
print("1. Top 10 produtos mais vendidos")
print("2. Evolução do faturamento mensal")
print("3. Faturamento por estado")
print("4. Faturamento por categoria")
print("\nFim do Mini-Projeto 1")