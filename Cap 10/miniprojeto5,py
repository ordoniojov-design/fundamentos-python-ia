# -*- coding: utf-8 -*-
"""
Mini-Projeto 5 - Modelagem Estatística e Interpretação de Resultados na Análise de Churn
Complemento para completar a análise.
"""

# =============================================================================
# 5. Preparação dos dados para modelagem
# =============================================================================
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Criar variáveis dummy para as variáveis categóricas
df_dummies = pd.get_dummies(df_churn, columns=['Tipo_Contrato', 'Servico_Internet'], drop_first=True)

# Selecionar features e target
X = df_dummies.drop(['ID_Cliente', 'Churn'], axis=1)
y = df_dummies['Churn']

# Padronizar variáveis numéricas (opcional, mas pode ajudar na convergência)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42, stratify=y)

print(f"Tamanho do treino: {X_train.shape[0]} amostras")
print(f"Tamanho do teste: {X_test.shape[0]} amostras")

# =============================================================================
# 6. Ajuste do modelo de regressão logística (com statsmodels)
# =============================================================================
import statsmodels.api as sm

# Adicionar constante (intercepto)
X_train_const = sm.add_constant(X_train)

# Ajustar modelo
model = sm.Logit(y_train, X_train_const)
result = model.fit(method='newton', maxiter=100)  # Pode aumentar maxiter se necessário

# Exibir sumário estatístico
print(result.summary())

# =============================================================================
# 7. Avaliação do modelo no conjunto de teste
# =============================================================================
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# Prever probabilidades e classes no teste
X_test_const = sm.add_constant(X_test)
y_pred_prob = result.predict(X_test_const)
y_pred = (y_pred_prob >= 0.5).astype(int)

print("\n--- Avaliação no teste ---")
print(f"Acurácia: {accuracy_score(y_test, y_pred):.4f}")
print("Matriz de confusão:")
print(confusion_matrix(y_test, y_pred))
print("\nRelatório de classificação:")
print(classification_report(y_test, y_pred, target_names=['Não Churn', 'Churn']))

# Curva ROC e AUC
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
auc = roc_auc_score(y_test, y_pred_prob)

plt.figure(figsize=(6,5))
plt.plot(fpr, tpr, label=f'ROC curve (AUC = {auc:.3f})')
plt.plot([0,1],[0,1], 'k--')
plt.xlabel('Taxa de Falso Positivo')
plt.ylabel('Taxa de Verdadeiro Positivo')
plt.title('Curva ROC')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# =============================================================================
# 8. Interpretação dos coeficientes (odds ratio)
# =============================================================================
# Obter coeficientes e intervalos de confiança
params = result.params
conf = result.conf_int()
conf['OR'] = np.exp(params)          # Odds ratio
conf.columns = ['2.5%', '97.5%', 'OR']
conf = np.exp(conf)                  # Aplica exp também nos limites (já estão em log)
conf = conf.sort_values('OR', ascending=False)

print("\n--- Odds ratio (exp(coef)) ---")
print(conf)

# Destacar variáveis estatisticamente significativas (p-valor < 0.05)
p_values = result.pvalues
significativas = p_values[p_values < 0.05].index
print("\nVariáveis com p-valor < 0.05:")
print(significativas.tolist())

# =============================================================================
# 9. Geração de recomendações de negócio
# =============================================================================
print("\n" + "="*60)
print("RECOMENDAÇÕES DE NEGÓCIO BASEADAS NO MODELO")
print("="*60)

# Analisar as variáveis mais importantes (maior odds ratio)
top_vars = conf.head(5)
for var in top_vars.index:
    if var == 'const':
        continue
    or_val = top_vars.loc[var, 'OR']
    desc = ""
    if 'Tipo_Contrato_Mensal' in var and or_val > 1:
        desc = "Clientes com contrato mensal têm muito mais chance de churn. Ofereça incentivos para migração para planos anuais ou bienais."
    elif 'Servico_Internet_Fibra Óptica' in var and or_val > 1:
        desc = "Usuários de fibra óptica podem estar insatisfeitos com o preço ou qualidade. Avalie promoções ou melhorias no serviço."
    elif 'Fatura_Mensal' in var and or_val > 1:
        desc = "Aumentos na fatura mensal elevam o risco de churn. Considere políticas de fidelidade que ofereçam descontos progressivos."
    elif 'Fidelidade_Meses' in var and or_val < 1:
        desc = "Quanto maior o tempo de fidelidade, menor a chance de churn. Invista em programas de retenção para novos clientes."
    else:
        desc = f"Variável '{var}' tem impacto significativo (odds ratio = {or_val:.2f}). Analise ações específicas para este fator."
    print(f"- {var}: odds ratio = {or_val:.2f}  =>  {desc}")

print("\n" + "="*60)
print("Fim da análise.")