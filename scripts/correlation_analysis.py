import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr
import os

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

os.makedirs('/home/ubuntu/analise_correlacao', exist_ok=True)

print("Carregando dados...")
df_dengue = pd.read_csv('/home/ubuntu/dengue_data_raw.csv')

df_temp = pd.read_csv('/home/ubuntu/dados_complementares/temperatura_media_por_estado.csv', index_col=0)
df_precip = pd.read_csv('/home/ubuntu/dados_complementares/precipitacao_por_estado.csv', index_col=0)

df_socio = pd.read_csv('/home/ubuntu/dados_complementares/dados_socioeconomicos_por_estado.csv', index_col=0)

print("Preparando dados para correlação...")
df_dengue_estados = df_dengue[(df_dengue['UF_Notificacao'] != 'TOTAL') & 
                             (df_dengue['UF_Notificacao'] != 'Ignorado/exterior')]

mapeamento_estados = {
    'Acre': 'Acre',
    'Alagoas': 'Alagoas',
    'Amapá': 'Amapá',
    'Amazonas': 'Amazonas',
    'Bahia': 'Bahia',
    'Ceará': 'Ceará',
    'Distrito Federal': 'Distrito Federal',
    'Espírito Santo': 'Espírito Santo',
    'Goiás': 'Goiás',
    'Maranhão': 'Maranhão',
    'Mato Grosso': 'Mato Grosso',
    'Mato Grosso do Sul': 'Mato Grosso do Sul',
    'Minas Gerais': 'Minas Gerais',
    'Pará': 'Pará',
    'Paraíba': 'Paraíba',
    'Paraná': 'Paraná',
    'Pernambuco': 'Pernambuco',
    'Piauí': 'Piauí',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Rio Grande do Norte',
    'Rio Grande do Sul': 'Rio Grande do Sul',
    'Rondônia': 'Rondônia',
    'Roraima': 'Roraima',
    'Santa Catarina': 'Santa Catarina',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Sergipe',
    'Tocantins': 'Tocantins'
}

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
df_dengue_estados['Total_Calculado'] = df_dengue_estados[meses].sum(axis=1)

df_correlacao = pd.DataFrame(index=df_dengue_estados['UF_Notificacao'])
df_correlacao['Total_Casos'] = df_dengue_estados['Total_Calculado'].values

for estado in df_correlacao.index:
    if estado in df_temp.index:
        df_correlacao.loc[estado, 'Temperatura_Media'] = df_temp.loc[estado, 'Media_Anual']
        df_correlacao.loc[estado, 'Precipitacao_Total'] = df_precip.loc[estado, 'Total_Anual']

for estado in df_correlacao.index:
    if estado in df_socio.index:
        df_correlacao.loc[estado, 'IDH'] = df_socio.loc[estado, 'IDH']
        df_correlacao.loc[estado, 'Renda_Per_Capita'] = df_socio.loc[estado, 'Renda_Per_Capita']
        df_correlacao.loc[estado, 'Taxa_Urbanizacao'] = df_socio.loc[estado, 'Taxa_Urbanizacao']
        df_correlacao.loc[estado, 'Acesso_Saneamento'] = df_socio.loc[estado, 'Acesso_Saneamento']
        df_correlacao.loc[estado, 'Densidade_Demografica'] = df_socio.loc[estado, 'Densidade_Demografica']

df_correlacao['Casos_por_100k'] = df_correlacao['Total_Casos'] / df_correlacao['Densidade_Demografica'] * 100

df_correlacao.to_csv('/home/ubuntu/analise_correlacao/dados_correlacao.csv')

print("Calculando correlações...")
matriz_corr = df_correlacao.corr(method='spearman')
matriz_corr.to_csv('/home/ubuntu/analise_correlacao/matriz_correlacao.csv')

print("Criando visualizações de correlação...")

plt.figure(figsize=(12, 10))
sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, 
            linewidths=0.5, fmt=".2f", square=True)
plt.title('Matriz de Correlação entre Variáveis', fontsize=16)
plt.tight_layout()
plt.savefig('/home/ubuntu/analise_correlacao/matriz_correlacao.png', dpi=300)

plt.figure(figsize=(10, 8))
sns.scatterplot(x='Temperatura_Media', y='Casos_por_100k', data=df_correlacao, 
                s=100, alpha=0.7)

sns.regplot(x='Temperatura_Media', y='Casos_por_100k', data=df_correlacao, 
            scatter=False, ci=None, line_kws={"color": "red"})

for i, txt in enumerate(df_correlacao.index):
    plt.annotate(txt, (df_correlacao['Temperatura_Media'].iloc[i], 
                      df_correlacao['Casos_por_100k'].iloc[i]),
                fontsize=8)

plt.title('Relação entre Temperatura Média e Casos de Dengue por 100 mil habitantes', fontsize=14)
plt.xlabel('Temperatura Média Anual (°C)', fontsize=12)
plt.ylabel('Casos de Dengue por 100 mil habitantes', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('/home/ubuntu/analise_correlacao/temp_vs_dengue.png', dpi=300)

plt.figure(figsize=(10, 8))
sns.scatterplot(x='Precipitacao_Total', y='Casos_por_100k', data=df_correlacao, 
                s=100, alpha=0.7)

sns.regplot(x='Precipitacao_Total', y='Casos_por_100k', data=df_correlacao, 
            scatter=False, ci=None, line_kws={"color": "red"})

for i, txt in enumerate(df_correlacao.index):
    plt.annotate(txt, (df_correlacao['Precipitacao_Total'].iloc[i], 
                      df_correlacao['Casos_por_100k'].iloc[i]),
                fontsize=8)

plt.title('Relação entre Precipitação Total e Casos de Dengue por 100 mil habitantes', fontsize=14)
plt.xlabel('Precipitação Total Anual (mm)', fontsize=12)
plt.ylabel('Casos de Dengue por 100 mil habitantes', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('/home/ubuntu/analise_correlacao/precip_vs_dengue.png', dpi=300)

plt.figure(figsize=(10, 8))
sns.scatterplot(x='IDH', y='Casos_por_100k', data=df_correlacao, 
                s=100, alpha=0.7)

sns.regplot(x='IDH', y='Casos_por_100k', data=df_correlacao, 
            scatter=False, ci=None, line_kws={"color": "red"})

for i, txt in enumerate(df_correlacao.index):
    plt.annotate(txt, (df_correlacao['IDH'].iloc[i], 
                      df_correlacao['Casos_por_100k'].iloc[i]),
                fontsize=8)

plt.title('Relação entre IDH e Casos de Dengue por 100 mil habitantes', fontsize=14)
plt.xlabel('Índice de Desenvolvimento Humano (IDH)', fontsize=12)
plt.ylabel('Casos de Dengue por 100 mil habitantes', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('/home/ubuntu/analise_correlacao/idh_vs_dengue.png', dpi=300)

plt.figure(figsize=(10, 8))
sns.scatterplot(x='Acesso_Saneamento', y='Casos_por_100k', data=df_correlacao, 
                s=100, alpha=0.7)

sns.regplot(x='Acesso_Saneamento', y='Casos_por_100k', data=df_correlacao, 
            scatter=False, ci=None, line_kws={"color": "red"})

for i, txt in enumerate(df_correlacao.index):
    plt.annotate(txt, (df_correlacao['Acesso_Saneamento'].iloc[i], 
                      df_correlacao['Casos_por_100k'].iloc[i]),
                fontsize=8)

plt.title('Relação entre Acesso a Saneamento e Casos de Dengue por 100 mil habitantes', fontsize=14)
plt.xlabel('Acesso a Saneamento Básico (%)', fontsize=12)
plt.ylabel('Casos de Dengue por 100 mil habitantes', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('/home/ubuntu/analise_correlacao/saneamento_vs_dengue.png', dpi=300)

plt.figure(figsize=(10, 8))
sns.scatterplot(x='Taxa_Urbanizacao', y='Casos_por_100k', data=df_correlacao, 
                s=100, alpha=0.7)

sns.regplot(x='Taxa_Urbanizacao', y='Casos_por_100k', data=df_correlacao, 
            scatter=False, ci=None, line_kws={"color": "red"})

for i, txt in enumerate(df_correlacao.index):
    plt.annotate(txt, (df_correlacao['Taxa_Urbanizacao'].iloc[i], 
                      df_correlacao['Casos_por_100k'].iloc[i]),
                fontsize=8)

plt.title('Relação entre Taxa de Urbanização e Casos de Dengue por 100 mil habitantes', fontsize=14)
plt.xlabel('Taxa de Urbanização (%)', fontsize=12)
plt.ylabel('Casos de Dengue por 100 mil habitantes', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('/home/ubuntu/analise_correlacao/urbanizacao_vs_dengue.png', dpi=300)

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(df_correlacao['Temperatura_Media'], 
                    df_correlacao['Acesso_Saneamento'], 
                    df_correlacao['Casos_por_100k'],
                    c=df_correlacao['Casos_por_100k'], 
                    cmap='viridis', 
                    s=100, 
                    alpha=0.7)

for i, txt in enumerate(df_correlacao.index):
    ax.text(df_correlacao['Temperatura_Media'].iloc[i], 
           df_correlacao['Acesso_Saneamento'].iloc[i], 
           df_correlacao['Casos_por_100k'].iloc[i], 
           txt, fontsize=8)

ax.set_xlabel('Temperatura Média Anual (°C)', fontsize=12)
ax.set_ylabel('Acesso a Saneamento (%)', fontsize=12)
ax.set_zlabel('Casos de Dengue por 100 mil habitantes', fontsize=12)
plt.title('Análise Multivariada: Temperatura, Saneamento e Casos de Dengue', fontsize=14)

cbar = plt.colorbar(scatter)
cbar.set_label('Casos de Dengue por 100 mil habitantes', fontsize=10)

plt.tight_layout()
plt.savefig('/home/ubuntu/analise_correlacao/analise_multivariada.png', dpi=300)

print("Análise de correlação concluída com sucesso!")
