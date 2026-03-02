# -*- coding: utf-8 -*-
"""
Mini-Projeto 6 - Modelo de Classificação Para Análise de Sentimentos
Data Science Academy
"""

#%% 1. Importação dos Pacotes

# Instala o pacote watermark (caso não esteja instalado)
!pip install -q -U watermark

# Manipulação de dados e visualização
import re
import pandas as pd
import numpy as np
import unicodedata
import seaborn as sns
import matplotlib.pyplot as plt

# Pré-Processamento e Machine Learning
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Configurações de visualização
sns.set_style('whitegrid')
%matplotlib inline

# Verifica versões
%reload_ext watermark
%watermark -a "Data Science Academy"
%watermark --iversions

#%% 2. Carregando e Compreendendo os Dados

# Define o nome do arquivo (assumindo que está no mesmo diretório)
nome_arquivo_csv = 'dataset.csv'

# Carrega o dataset
df_dsa = pd.read_csv(nome_arquivo_csv)

# Shape
print("Shape:", df_dsa.shape)

# Primeiras linhas
print("\nPrimeiras linhas:")
print(df_dsa.head())

# Amostra aleatória
print("\nAmostra aleatória:")
print(df_dsa.sample(10))

# Últimas linhas
print("\nÚltimas linhas:")
print(df_dsa.tail())

#%% 3. Análise Exploratória de Dados (EDA)

# Info
print("\nInformações do DataFrame:")
df_dsa.info()

# Verificando valores ausentes
print("\nVerificando valores ausentes:")
print(df_dsa.isnull().sum())

# Distribuição dos sentimentos
print("\nDistribuição dos Sentimentos:")
sns.countplot(x='sentimento', data=df_dsa)
plt.title('Distribuição das Classes de Sentimento')
plt.show()

#%% 4. Limpeza de Dados

# Remover linhas com valores ausentes
print(f"\nTamanho original do DataFrame: {len(df_dsa)}")
df_dsa.dropna(subset=['texto_review'], inplace=True)
print(f"Tamanho do DataFrame após remover nulos: {len(df_dsa)}")

# Função de limpeza de texto 
def dsa_limpa_texto(texto):
    """
    Função completa de limpeza de texto:
    1. Converte para minúsculas.
    2. Remove acentos e cedilha.
    3. Remove pontuações, números e caracteres especiais.
    4. Remove espaços extras.
    """
    # Garante que o texto não seja nulo
    if not isinstance(texto, str):
        return ""

    # PASSO 1: Normalizar e remover acentos
    texto_sem_acentos = ''.join(c for c in unicodedata.normalize('NFKD', texto) 
                                 if unicodedata.category(c) != 'Mn')

    # PASSO 2: Limpeza com Regex
    texto_limpo = texto_sem_acentos.lower()
    # Manter apenas letras e espaços
    texto_limpo = re.sub(r'[^a-z\s]', '', texto_limpo)
    # Remover espaços extras
    texto_limpo = re.sub(r'\s+', ' ', texto_limpo).strip()
    
    return texto_limpo

# Aplica a função de limpeza
df_dsa['texto_limpo'] = df_dsa['texto_review'].apply(dsa_limpa_texto)

# Exibe resultado
print("\nDataFrame após limpeza:")
print(df_dsa[['texto_review', 'texto_limpo']].head())

#%% 5. Engenharia de Atributos

# Mapear o sentimento para valores numéricos
df_dsa['sentimento_label'] = df_dsa['sentimento'].map({'positivo': 1, 'negativo': 0})

print("\nDataFrame após mapeamento:")
print(df_dsa[['texto_limpo', 'sentimento_label']].head())

#%% 6. Divisão em Dados de Treino e Teste

# Definir variáveis X (entrada) e y (saída)
X = df_dsa['texto_limpo']
y = df_dsa['sentimento_label']

# Dividir os dados em treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

#%% 7. Pipeline de Modelagem Preditiva

# Criação do pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words=['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um'])),
    ('scaler', StandardScaler(with_mean=False)),
    ('logreg', LogisticRegression(solver='liblinear', random_state=42, max_iter=1000))
])

# Definição do grid de hiperparâmetros
parametros_grid = {
    'tfidf__max_features': [500, 1000, 2000],
    'tfidf__ngram_range': [(1, 1), (1, 2)],
    'logreg__C': [0.1, 1, 10],
    'logreg__penalty': ['l1', 'l2'],
    'logreg__max_iter': [5000, 6000]
}

# Configurar o GridSearchCV
grid_search = GridSearchCV(
    pipeline,
    parametros_grid,
    cv=5,
    n_jobs=-1,
    scoring='accuracy',
    verbose=1
)

print("\nIniciando o treinamento do modelo com otimização de hiperparâmetros...\n")
grid_search.fit(X_treino, y_treino)

# Melhores hiperparâmetros
print("\nMelhores hiperparâmetros encontrados:")
print(grid_search.best_params_)

# Obter o melhor modelo
melhor_modelo_dsa = grid_search.best_estimator_

#%% 8. Avaliação do Modelo

# Previsões no conjunto de teste
y_pred = melhor_modelo_dsa.predict(X_teste)

# Calcular as métricas de avaliação
acuracia = accuracy_score(y_teste, y_pred)
report = classification_report(y_teste, y_pred, target_names=['Negativo', 'Positivo'])

print(f"\nAcurácia do Modelo: {acuracia:.2%}\n")
print("Relatório de Classificação:\n")
print(report)

# Matriz de Confusão
cm = confusion_matrix(y_teste, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Negativo', 'Positivo'],
            yticklabels=['Negativo', 'Positivo'])
plt.xlabel('Previsão')
plt.ylabel('Verdadeiro')
plt.title('Matriz de Confusão')
plt.show()

# Salvar o modelo treinado
joblib.dump(melhor_modelo_dsa, 'modelo_sentimento_dsa_v1.joblib')
print("\nModelo salvo como 'modelo_sentimento_dsa_v1.joblib'")

# (Opcional) Deletar da memória
del melhor_modelo_dsa

#%% 9. Deploy e Uso do Modelo

# Carregar o modelo do disco
modelo_dsa_deploy = joblib.load('modelo_sentimento_dsa_v1.joblib')

# Novos dados para teste
novos_reviews = [
    "A bateria do celular não dura nada, péssima compra.",
    "Chegou antes do prazo e o produto é de ótima qualidade! Estou muito feliz.",
    "O serviço de atendimento foi rápido e eficiente.",
    "Não recomendo, veio faltando peças e a cor estava errada."
]

# Função para prever sentimento
def dsa_prever_sentimento(reviews):
    previsoes = modelo_dsa_deploy.predict(reviews)
    sentimentos = ['Negativo' if p == 0 else 'Positivo' for p in previsoes]
    for review, sentimento in zip(reviews, sentimentos):
        print(f"\nReview: '{review}'\nSentimento Previsto: {sentimento}\n---")

print("\n--- Iniciando Classificação de Novos Reviews (Deploy) ---\n")
dsa_prever_sentimento(novos_reviews)

print("\nProjeto concluído!")