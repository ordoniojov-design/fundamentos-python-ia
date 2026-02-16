# Imports
import pandas as pd
import numpy as np

# Exercício 1: Seleção de Dados Condicional
dados = {'Nome': ['Ana', 'Bruno', 'Carla', 'Matias', 'Eliana', 'Fabiano'],
         'Departamento': ['RH', 'Vendas', 'TI', 'Vendas', 'RH', 'Vendas'],
         'Salário': [4000, 5000, 6200, 4400, 4300, 5500]}
df_funcionarios = pd.DataFrame(dados)
print("Exercício 1 - Funcionários de Vendas com salário > 4500:")
filtro = (df_funcionarios['Departamento'] == 'Vendas') & (df_funcionarios['Salário'] > 4500)
df_filtrado = df_funcionarios[filtro]
print(df_filtrado)
print()

# Exercício 2: Agrupamento e Agregação (groupby)
dados_vendas = {'Categoria': ['Eletrônicos', 'Vestuário', 'Eletrônicos', 'Casa', 'Vestuário', 'Eletrônicos'],
                'Produto': ['TV', 'Camiseta', 'Notebook', 'Sofá', 'Calça', 'Celular'],
                'Valor': [2500, 80, 4500, 1500, 120, 3000]}
df_vendas = pd.DataFrame(dados_vendas)
print("Exercício 2 - Total de vendas por categoria:")
total_por_categoria = df_vendas.groupby('Categoria')['Valor'].sum()
print(total_por_categoria)
print()

# Exercício 3: Criação de Nova Coluna
dados_produtos = {'Produto': ['Monitor', 'Teclado', 'Mouse', 'Webcam'],
                  'Preco': [800, 120, 70, 250]}
df_produtos = pd.DataFrame(dados_produtos)
print("Exercício 3 - Produtos com preço com desconto de 10%:")
df_produtos['Preco_com_Desconto'] = df_produtos['Preco'] * 0.9
print(df_produtos)
print()

# Exercício 4: Tratamento de Dados Ausentes (NaN)
dados_alunos = {'Aluno': ['Alice', 'Bernardo', 'Clara', 'Marcelo'],
                'Nota': [8.5, 7.0, np.nan, 9.0]}
df_alunos = pd.DataFrame(dados_alunos)
print("Exercício 4 - Notas com NaN substituído pela média:")
media_notas = df_alunos['Nota'].mean()
df_alunos['Nota'].fillna(media_notas, inplace=True)
print(df_alunos)
print()

# Exercício 5: Ordenação de Dados (sort_values)
dados_pontuacao = {'Jogador': ['J1', 'J2', 'J3', 'J4', 'J5'],
                   'Pontos': [88, 95, 74, 102, 95]}
df_pontuacao = pd.DataFrame(dados_pontuacao)
print("Exercício 5 - Pontuação ordenada decrescente:")
df_ordenado = df_pontuacao.sort_values('Pontos', ascending=False)
print(df_ordenado)
print()

# Exercício 6: Combinação de DataFrames (merge)
df_clientes = pd.DataFrame({'ID_Cliente': [1, 2, 3],
                            'Nome': ['Carlos', 'Mariana', 'Lucas']})
df_pedidos = pd.DataFrame({'ID_Pedido': [101, 102, 103],
                           'ID_Cliente': [2, 1, 2],
                           'Produto': ['Livro', 'Caneta', 'Caderno']})
print("Exercício 6 - Merge de clientes e pedidos:")
df_combinado = pd.merge(df_clientes, df_pedidos, on='ID_Cliente')
print(df_combinado)
print()

# Exercício 7: Manipulação de Strings (.str)
dados_eventos = {'Evento': ['Conferência A', 'Workshop B', 'Feira C'],
                 'Data': ['2025-10-25', '2026-03-12', '2026-09-01']}
df_eventos = pd.DataFrame(dados_eventos)
print("Exercício 7 - Extração do ano:")
df_eventos['Ano'] = df_eventos['Data'].str[:4]
print(df_eventos)
print()

# Exercício 8: Uso do Método apply
dados_notas = {'Aluno': ['Maria', 'Jeremias', 'Paulo', 'Roberto'],
               'Nota': [9.5, 6.0, 5.5, 8.0]}
df_notas = pd.DataFrame(dados_notas)
def classificar_status(nota):
    if nota >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'
print("Exercício 8 - Status com apply:")
df_notas['Status'] = df_notas['Nota'].apply(classificar_status)
print(df_notas)
print()

# Exercício 9: Criação de Tabela Dinâmica (pivot_table)
dados_regional = {'Regiao': ['Norte', 'Sul', 'Norte', 'Sul', 'Norte', 'Sul'],
                  'Vendedor': ['Ana', 'Bruno', 'Ana', 'Carlos', 'Carlos', 'Bruno'],
                  'Vendas': [1000, 1500, 1200, 1800, 800, 1300]}
df_regional = pd.DataFrame(dados_regional)
print("Exercício 9 - Tabela dinâmica (soma de vendas por região e vendedor):")
tabela_dinamica = pd.pivot_table(df_regional, values='Vendas', index='Regiao', columns='Vendedor', aggfunc='sum', fill_value=0)
print(tabela_dinamica)
print()

# Exercício 10: Análise de Séries Temporais
datas = pd.to_datetime(pd.date_range(start='2026-07-25', periods=15, freq='D'))
dados_visitas = {'Visitas': [150, 165, 178, 199, 205, 210, 225, 230, 215, 240, 255, 260, 245, 250, 270]}
df_visitas = pd.DataFrame(data=dados_visitas, index=datas)
df_visitas.index.name = 'Data'
print("Exercício 10 - Registros de agosto de 2026:")
df_agosto = df_visitas[df_visitas.index.month == 8]
print(df_agosto)
print()