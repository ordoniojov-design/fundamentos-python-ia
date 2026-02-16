# Imports
import pandas as pd
import numpy as np

# Dados de exemplo
dados = {'Nome': ['Ana', 'Bruno', 'Carla', 'Matias', 'Eliana', 'Fabiano'],
         'Departamento': ['RH', 'Vendas', 'TI', 'Vendas', 'RH', 'Vendas'],
         'Salário': [4000, 5000, 6200, 4400, 4300, 5500]}

# DataFrame
df_funcionarios = pd.DataFrame(dados)

# Solução

# Criamos o filtro da coluna de Departamento
condicao_depto = df_funcionarios['Departamento'] == 'Vendas'

# Criamos o filtro da coluna de Salário
condicao_salario = df_funcionarios['Salário'] > 4500

# Aplicamos os filtros ao dataframe
funcionarios_filtrados = df_funcionarios[condicao_depto & condicao_salario]

# Visualizamos o dataframe
funcionarios_filtrados

# Dados de exemplo
dados_vendas = {'Categoria': ['Eletrônicos', 'Vestuário', 'Eletrônicos', 'Casa', 'Vestuário', 'Eletrônicos'],
                'Produto': ['TV', 'Camiseta', 'Notebook', 'Sofá', 'Calça', 'Celular'],
                'Valor': [2500, 80, 4500, 1500, 120, 3000]}

# DataFrame
df_vendas = pd.DataFrame(dados_vendas)

# Solução

# Agrupamento
vendas_por_categoria = df_vendas.groupby('Categoria')['Valor'].sum()

# Visualizamos o dataframe
print(vendas_por_categoria)

# Dados de exemplo
dados_produtos = {'Produto': ['Monitor', 'Teclado', 'Mouse', 'Webcam'],
                  'Preco': [800, 120, 70, 250]}

# DataFrame
df_produtos = pd.DataFrame(dados_produtos)

# Solução

# A vetorização permite aplicar uma única operação para todas as linhas filtrando por coluna
df_produtos['Preco_com_Desconto'] = df_produtos['Preco'] * 0.90

# Visualizamos o dataframe
df_produtos

# Dados de exemplo
dados_alunos = {'Aluno': ['Alice', 'Bernardo', 'Clara', 'Marcelo'],
                'Nota': [8.5, 7.0, np.nan, 9.0]}

# DataFrame
df_alunos = pd.DataFrame(dados_alunos)

# Solução

# Calculamos a média (linhas com valores ausentes não são consideradas)
media_notas = df_alunos['Nota'].mean()

# Em vez de usar inplace = True, reatribuímos o resultado à coluna
df_alunos['Nota'] = df_alunos['Nota'].fillna(media_notas)

# Visualizamos o dataframe
df_alunos

# Dados de exemplo
dados_pontuacao = {'Jogador': ['J1', 'J2', 'J3', 'J4', 'J5'],
                   'Pontos': [88, 95, 74, 102, 95]}

# DataFrame
df_pontuacao = pd.DataFrame(dados_pontuacao)

# Solução

# Ordenação
df_ordenado = df_pontuacao.sort_values(by = 'Pontos', ascending = False)

# Visualizamos o dataframe
df_ordenado

# Dados de exemplo
df_clientes = pd.DataFrame({'ID_Cliente': [1, 2, 3],
                            'Nome': ['Carlos', 'Mariana', 'Lucas']})

# Dados de exemplo
df_pedidos = pd.DataFrame({'ID_Pedido': [101, 102, 103],
                           'ID_Cliente': [2, 1, 2],
                           'Produto': ['Livro', 'Caneta', 'Caderno']})

# Solução

# Usamos merge para combinar dataframes
df_combinado = pd.merge(df_clientes, df_pedidos, on = 'ID_Cliente')

# Visualizamos o dataframe
df_combinado

# Dados de exemplo
dados_eventos = {'Evento': ['Conferência A', 'Workshop B', 'Feira C'],
                 'Data': ['2025-10-25', '2026-03-12', '2026-09-01']}

# DataFrame
df_eventos = pd.DataFrame(dados_eventos)

df_eventos.info()

# Solução

# Usamos a coluna de data como tipo string (str) e aplicamos slice() para extrair o ano da data
df_eventos['Ano'] = df_eventos['Data'].str.slice(0, 4)

# Visualizamos o dataframe
df_eventos

# Solução alternativa (melhor prática)

# Usamos a coluna de data como tipo data (dt) e extraímos o ano
df_eventos['Ano'] = pd.to_datetime(df_eventos['Data']).dt.year

# Visualizamos o dataframe
df_eventos

# Dados de exemplo
dados_notas = {'Aluno': ['Maria', 'Jeremias', 'Paulo', 'Roberto'],
               'Nota': [9.5, 6.0, 5.5, 8.0]}

# DataFrame
df_notas = pd.DataFrame(dados_notas)

# Solução

# Usamos expressão lambda para aplicar a condição a uma coluna e gravar em uma nova coluna
df_notas['Status'] = df_notas['Nota'].apply(lambda nota: 'Aprovado' if nota >= 7 else 'Reprovado')

# Visualizamos o dataframe
df_notas

# Dados de exemplo
dados_regional = {'Regiao': ['Norte', 'Sul', 'Norte', 'Sul', 'Norte', 'Sul'],
                  'Vendedor': ['Ana', 'Bruno', 'Ana', 'Carlos', 'Carlos', 'Bruno'],
                  'Vendas': [1000, 1500, 1200, 1800, 800, 1300]}

# DataFrame
df_regional = pd.DataFrame(dados_regional)

# Solução
tabela_dinamica = df_regional.pivot_table(index = 'Regiao', 
                                          columns = 'Vendedor', 
                                          values = 'Vendas', 
                                          aggfunc = 'sum', 
                                          fill_value = 0)

# Visualizamos o dataframe
tabela_dinamica

# Dados de exemplo
datas = pd.to_datetime(pd.date_range(start = '2026-07-25', periods = 15, freq = 'D'))
dados_visitas = {'Visitas': [150, 165, 178, 199, 205, 210, 225, 230, 215, 240, 255, 260, 245, 250, 270]}
df_visitas = pd.DataFrame(data = dados_visitas, index = datas)
df_visitas.index.name = 'Data'

# Solução

# Para selecionar linhas com base no índice, usamos o .loc
visitas_agosto = df_visitas.loc['2026-08']

# Visualizamos o dataframe
visitas_agosto