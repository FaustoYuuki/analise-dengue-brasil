import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import matplotlib as mpl

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('/home/ubuntu/dengue_data_raw.csv')

df['Total_Calculado'] = df.iloc[:, 2:14].sum(axis=1)

import os
os.makedirs('/home/ubuntu/visualizacoes', exist_ok=True)

plt.figure(figsize=(12, 6))
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
casos_por_mes = df[df['UF_Notificacao'] == 'TOTAL'][meses].values[0]

plt.plot(meses, casos_por_mes, marker='o', linewidth=2, markersize=8)
plt.title('Casos de Dengue por Mês no Brasil', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Número de Casos', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

def milhoes(x, pos):
    return f'{x/1e6:.1f}M' if x >= 1e6 else f'{x/1e3:.0f}K'

plt.gca().yaxis.set_major_formatter(FuncFormatter(milhoes))

plt.annotate(f'Pico: {casos_por_mes[3]:,.0f}',
             xy=(3, casos_por_mes[3]), 
             xytext=(3, casos_por_mes[3]*1.1),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=12)

plt.tight_layout()
plt.savefig('/home/ubuntu/visualizacoes/casos_por_mes.png', dpi=300)

df_estados = df[(df['UF_Notificacao'] != 'TOTAL') & (df['UF_Notificacao'] != 'Ignorado/exterior')]
df_estados = df_estados.sort_values(by='Total_Calculado', ascending=False).head(10)

plt.figure(figsize=(12, 6))
bars = plt.bar(df_estados['UF_Notificacao'], df_estados['Total_Calculado'], color=sns.color_palette('viridis', 10))
plt.title('Top 10 Estados com Mais Casos de Dengue', fontsize=16)
plt.xlabel('Estado', fontsize=12)
plt.ylabel('Número de Casos', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:,.0f}',
             ha='center', va='bottom', rotation=0, fontsize=9)

plt.gca().yaxis.set_major_formatter(FuncFormatter(milhoes))
plt.tight_layout()
plt.savefig('/home/ubuntu/visualizacoes/top10_estados.png', dpi=300)

top15_estados = df_estados.head(15).copy()
heatmap_data = top15_estados[meses].values
estados_nomes = top15_estados['UF_Notificacao'].values

plt.figure(figsize=(14, 8))
ax = sns.heatmap(heatmap_data, annot=False, fmt=".0f", cmap="YlOrRd", 
                 xticklabels=meses, yticklabels=estados_nomes)
plt.title('Distribuição de Casos de Dengue por Mês e Estado (Top 15)', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Estado', fontsize=12)

cbar = ax.collections[0].colorbar
cbar.set_label('Número de Casos')
plt.tight_layout()
plt.savefig('/home/ubuntu/visualizacoes/heatmap_estados_meses.png', dpi=300)

regioes = {
    'Norte': ['Acre', 'Amapá', 'Amazonas', 'Pará', 'Rondônia', 'Roraima', 'Tocantins'],
    'Nordeste': ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe'],
    'Centro-Oeste': ['Distrito Federal', 'Goiás', 'Mato Grosso', 'Mato Grosso do Sul'],
    'Sudeste': ['Espírito Santo', 'Minas Gerais', 'Rio de Janeiro', 'São Paulo'],
    'Sul': ['Paraná', 'Rio Grande do Sul', 'Santa Catarina']
}

df_regioes = pd.DataFrame(columns=meses)

for regiao, estados in regioes.items():
    df_regiao = df[df['UF_Notificacao'].isin(estados)]
    casos_regiao = df_regiao[meses].sum()
    df_regioes.loc[regiao] = casos_regiao

plt.figure(figsize=(14, 7))
for regiao in df_regioes.index:
    plt.plot(meses, df_regioes.loc[regiao], marker='o', linewidth=2, label=regiao)

plt.title('Casos de Dengue por Mês e Região', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Número de Casos', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Região', fontsize=10)
plt.gca().yaxis.set_major_formatter(FuncFormatter(milhoes))
plt.tight_layout()
plt.savefig('/home/ubuntu/visualizacoes/casos_por_regiao.png', dpi=300)

total_por_regiao = df_regioes.sum(axis=1)
plt.figure(figsize=(10, 8))
plt.pie(total_por_regiao, labels=total_por_regiao.index, autopct='%1.1f%%', 
        startangle=90, shadow=True, explode=[0.05]*5,
        colors=sns.color_palette('viridis', 5))
plt.title('Distribuição de Casos de Dengue por Região', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.tight_layout()
plt.savefig('/home/ubuntu/visualizacoes/distribuicao_por_regiao.png', dpi=300)

trimestres = {
    'Verão (Jan-Mar)': ['Jan', 'Fev', 'Mar'],
    'Outono (Abr-Jun)': ['Abr', 'Mai', 'Jun'],
    'Inverno (Jul-Set)': ['Jul', 'Ago', 'Set'],
    'Primavera (Out-Dez)': ['Out', 'Nov', 'Dez']
}

df_trimestres = pd.DataFrame(index=df_regioes.index, columns=trimestres.keys())

for trimestre, meses_trim in trimestres.items():
    for regiao in df_regioes.index:
        df_trimestres.loc[regiao, trimestre] = df_regioes.loc[regiao, meses_trim].sum()

plt.figure(figsize=(12, 7))
df_trimestres.plot(kind='bar', stacked=False, figsize=(12, 7), width=0.7)
plt.title('Casos de Dengue por Trimestre e Região', fontsize=16)
plt.xlabel('Região', fontsize=12)
plt.ylabel('Número de Casos', fontsize=12)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Trimestre', fontsize=10)
plt.gca().yaxis.set_major_formatter(FuncFormatter(milhoes))
plt.tight_layout()
plt.savefig('/home/ubuntu/visualizacoes/casos_por_trimestre.png', dpi=300)

df.to_csv('/home/ubuntu/visualizacoes/dengue_data_processed.csv', index=False)
df_regioes.to_csv('/home/ubuntu/visualizacoes/dengue_por_regiao.csv')
df_trimestres.to_csv('/home/ubuntu/visualizacoes/dengue_por_trimestre.csv')

print("Visualizações geradas com sucesso e salvas em /home/ubuntu/visualizacoes/")
