import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from io import StringIO
import os

os.makedirs('/home/ubuntu/dados_complementares', exist_ok=True)

def gerar_dados_climaticos():
    """
    Gera dados simulados de temperatura e precipitação por estado
    baseados em padrões climáticos conhecidos do Brasil.
    """
    
    estados = [
        'Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 
        'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 
        'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 
        'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 
        'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 
        'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins'
    ]
    
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    
    temp_base_regiao = {
        'Norte': [27, 27, 27, 27, 26, 26, 26, 27, 28, 28, 28, 27],
        'Nordeste': [28, 28, 28, 27, 26, 25, 25, 26, 27, 28, 28, 28],
        'Centro-Oeste': [26, 26, 26, 25, 23, 22, 22, 24, 26, 27, 26, 26],
        'Sudeste': [25, 25, 24, 23, 21, 20, 19, 21, 22, 23, 24, 25],
        'Sul': [24, 24, 23, 20, 17, 15, 15, 16, 18, 20, 22, 23]
    }
    
    precip_base_regiao = {
        'Norte': [300, 300, 300, 250, 200, 100, 80, 60, 80, 150, 200, 250],
        'Nordeste': [150, 180, 200, 180, 150, 100, 80, 30, 30, 50, 80, 100],
        'Centro-Oeste': [250, 200, 180, 100, 50, 20, 10, 30, 80, 150, 200, 250],
        'Sudeste': [200, 180, 150, 80, 50, 30, 30, 30, 80, 120, 150, 200],
        'Sul': [150, 150, 150, 120, 100, 100, 100, 100, 150, 180, 150, 150]
    }
    
    regiao_por_estado = {
        'Acre': 'Norte', 'Amapá': 'Norte', 'Amazonas': 'Norte', 'Pará': 'Norte', 
        'Rondônia': 'Norte', 'Roraima': 'Norte', 'Tocantins': 'Norte',
        'Alagoas': 'Nordeste', 'Bahia': 'Nordeste', 'Ceará': 'Nordeste', 
        'Maranhão': 'Nordeste', 'Paraíba': 'Nordeste', 'Pernambuco': 'Nordeste', 
        'Piauí': 'Nordeste', 'Rio Grande do Norte': 'Nordeste', 'Sergipe': 'Nordeste',
        'Distrito Federal': 'Centro-Oeste', 'Goiás': 'Centro-Oeste', 
        'Mato Grosso': 'Centro-Oeste', 'Mato Grosso do Sul': 'Centro-Oeste',
        'Espírito Santo': 'Sudeste', 'Minas Gerais': 'Sudeste', 
        'Rio de Janeiro': 'Sudeste', 'São Paulo': 'Sudeste',
        'Paraná': 'Sul', 'Rio Grande do Sul': 'Sul', 'Santa Catarina': 'Sul'
    }
    
    df_temp = pd.DataFrame(index=estados, columns=meses)
    df_precip = pd.DataFrame(index=estados, columns=meses)
    
    for estado in estados:
        regiao = regiao_por_estado[estado]
        
        temp_var = np.random.uniform(-1.5, 1.5)
        precip_var_factor = np.random.uniform(0.8, 1.2)
        
        for i, mes in enumerate(meses):
            temp_base = temp_base_regiao[regiao][i]
            df_temp.loc[estado, mes] = float(temp_base + temp_var + np.random.uniform(-0.5, 0.5))
            
            precip_base = precip_base_regiao[regiao][i]
            df_precip.loc[estado, mes] = float(precip_base * precip_var_factor * np.random.uniform(0.9, 1.1))
    
    for col in meses:
        df_temp[col] = df_temp[col].astype(float).round(1)
        df_precip[col] = df_precip[col].astype(float).round(1)
    
    df_temp['Media_Anual'] = df_temp[meses].mean(axis=1).round(1)
    df_precip['Total_Anual'] = df_precip[meses].sum(axis=1).round(1)
    
    return df_temp, df_precip

def gerar_dados_socioeconomicos():
    """
    Gera dados socioeconômicos simulados por estado baseados em
    estatísticas aproximadas do Brasil.
    """
    estados = [
        'Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 
        'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 
        'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 
        'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 
        'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 
        'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins'
    ]
    
    idh_aproximado = {
        'Distrito Federal': 0.850, 'São Paulo': 0.826, 'Santa Catarina': 0.808,
        'Rio de Janeiro': 0.796, 'Paraná': 0.792, 'Rio Grande do Sul': 0.787,
        'Espírito Santo': 0.778, 'Goiás': 0.769, 'Minas Gerais': 0.768,
        'Mato Grosso do Sul': 0.766, 'Mato Grosso': 0.762, 'Amapá': 0.740,
        'Roraima': 0.738, 'Tocantins': 0.732, 'Rondônia': 0.725,
        'Rio Grande do Norte': 0.722, 'Ceará': 0.715, 'Amazonas': 0.713,
        'Pernambuco': 0.709, 'Sergipe': 0.702, 'Acre': 0.697,
        'Bahia': 0.693, 'Paraíba': 0.691, 'Pará': 0.690,
        'Piauí': 0.684, 'Maranhão': 0.676, 'Alagoas': 0.672
    }
    
    renda_aproximada = {
        'Distrito Federal': 2800, 'São Paulo': 2100, 'Rio de Janeiro': 1900,
        'Santa Catarina': 1850, 'Rio Grande do Sul': 1800, 'Paraná': 1750,
        'Mato Grosso': 1650, 'Mato Grosso do Sul': 1600, 'Espírito Santo': 1550,
        'Goiás': 1500, 'Minas Gerais': 1450, 'Roraima': 1400,
        'Amapá': 1350, 'Tocantins': 1300, 'Rondônia': 1250,
        'Rio Grande do Norte': 1200, 'Sergipe': 1150, 'Amazonas': 1100,
        'Pernambuco': 1050, 'Ceará': 1000, 'Acre': 950,
        'Bahia': 900, 'Paraíba': 850, 'Pará': 800,
        'Piauí': 750, 'Alagoas': 700, 'Maranhão': 650
    }
    
    urbanizacao_aproximada = {
        'São Paulo': 96.5, 'Rio de Janeiro': 97.3, 'Distrito Federal': 97.0,
        'Goiás': 91.2, 'Minas Gerais': 85.3, 'Espírito Santo': 84.2,
        'Santa Catarina': 84.0, 'Rio Grande do Sul': 85.1, 'Paraná': 85.3,
        'Mato Grosso do Sul': 86.7, 'Mato Grosso': 81.9, 'Amapá': 89.8,
        'Amazonas': 79.1, 'Roraima': 76.4, 'Acre': 73.5,
        'Rondônia': 73.2, 'Tocantins': 78.8, 'Pará': 68.5,
        'Maranhão': 63.1, 'Piauí': 65.8, 'Ceará': 75.1,
        'Rio Grande do Norte': 77.8, 'Paraíba': 75.4, 'Pernambuco': 80.2,
        'Alagoas': 73.6, 'Sergipe': 73.5, 'Bahia': 72.1
    }
    
    saneamento_aproximado = {
        'São Paulo': 92.0, 'Santa Catarina': 88.5, 'Distrito Federal': 90.0,
        'Paraná': 82.3, 'Rio Grande do Sul': 81.7, 'Minas Gerais': 79.5,
        'Espírito Santo': 78.2, 'Rio de Janeiro': 87.1, 'Goiás': 76.4,
        'Mato Grosso do Sul': 75.8, 'Mato Grosso': 72.3, 'Tocantins': 65.4,
        'Sergipe': 63.2, 'Rio Grande do Norte': 62.8, 'Paraíba': 61.5,
        'Ceará': 60.2, 'Pernambuco': 64.8, 'Bahia': 59.7,
        'Alagoas': 55.3, 'Piauí': 52.1, 'Maranhão': 48.5,
        'Rondônia': 54.2, 'Acre': 51.8, 'Amazonas': 53.6,
        'Roraima': 55.7, 'Pará': 49.3, 'Amapá': 56.2
    }
    
    densidade_aproximada = {
        'Distrito Federal': 500, 'Rio de Janeiro': 365, 'São Paulo': 175,
        'Alagoas': 112, 'Sergipe': 94, 'Pernambuco': 89,
        'Paraíba': 66, 'Espírito Santo': 76, 'Santa Catarina': 65,
        'Rio Grande do Norte': 60, 'Ceará': 56, 'Paraná': 52,
        'Rio Grande do Sul': 38, 'Bahia': 25, 'Minas Gerais': 33,
        'Goiás': 17, 'Maranhão': 20, 'Piauí': 12,
        'Mato Grosso do Sul': 7, 'Rondônia': 6, 'Tocantins': 5,
        'Pará': 6, 'Acre': 5, 'Mato Grosso': 3,
        'Amapá': 4, 'Roraima': 2, 'Amazonas': 2
    }
    
    df_socio = pd.DataFrame({
        'UF': estados,
        'IDH': [idh_aproximado[estado] for estado in estados],
        'Renda_Per_Capita': [renda_aproximada[estado] for estado in estados],
        'Taxa_Urbanizacao': [urbanizacao_aproximada[estado] for estado in estados],
        'Acesso_Saneamento': [saneamento_aproximado[estado] for estado in estados],
        'Densidade_Demografica': [densidade_aproximada[estado] for estado in estados]
    })
    
    df_socio.set_index('UF', inplace=True)
    
    return df_socio

print("Gerando dados climáticos simulados...")
df_temp, df_precip = gerar_dados_climaticos()
df_temp.to_csv('/home/ubuntu/dados_complementares/temperatura_media_por_estado.csv')
df_precip.to_csv('/home/ubuntu/dados_complementares/precipitacao_por_estado.csv')

print("Gerando dados socioeconômicos simulados...")
df_socio = gerar_dados_socioeconomicos()
df_socio.to_csv('/home/ubuntu/dados_complementares/dados_socioeconomicos_por_estado.csv')

print("Carregando dados de dengue...")
df_dengue = pd.read_csv('/home/ubuntu/dengue_data_raw.csv')

print("Criando visualizações exploratórias...")

plt.figure(figsize=(14, 10))
sns.heatmap(df_temp.iloc[:, :-1].astype(float), annot=False, cmap='YlOrRd', 
            linewidths=0.5)
plt.title('Temperatura Média por Estado e Mês (°C)', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Estado', fontsize=12)
plt.tight_layout()
plt.savefig('/home/ubuntu/dados_complementares/heatmap_temperatura.png', dpi=300)

plt.figure(figsize=(14, 10))
sns.heatmap(df_precip.iloc[:, :-1].astype(float), annot=False, cmap='Blues', 
            linewidths=0.5)
plt.title('Precipitação por Estado e Mês (mm)', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Estado', fontsize=12)
plt.tight_layout()
plt.savefig('/home/ubuntu/dados_complementares/heatmap_precipitacao.png', dpi=300)

plt.figure(figsize=(14, 8))
df_socio.sort_values('IDH', ascending=False).IDH.plot(kind='bar', color='teal')
plt.title('Índice de Desenvolvimento Humano (IDH) por Estado', fontsize=16)
plt.xlabel('Estado', fontsize=12)
plt.ylabel('IDH', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('/home/ubuntu/dados_complementares/idh_por_estado.png', dpi=300)

plt.figure(figsize=(14, 8))
df_socio.sort_values('Renda_Per_Capita', ascending=False).Renda_Per_Capita.plot(kind='bar', color='darkgreen')
plt.title('Renda Per Capita por Estado (R$)', fontsize=16)
plt.xlabel('Estado', fontsize=12)
plt.ylabel('Renda Per Capita (R$)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('/home/ubuntu/dados_complementares/renda_por_estado.png', dpi=300)

plt.figure(figsize=(14, 8))
df_socio.sort_values('Taxa_Urbanizacao', ascending=False).Taxa_Urbanizacao.plot(kind='bar', color='purple')
plt.title('Taxa de Urbanização por Estado (%)', fontsize=16)
plt.xlabel('Estado', fontsize=12)
plt.ylabel('Taxa de Urbanização (%)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('/home/ubuntu/dados_complementares/urbanizacao_por_estado.png', dpi=300)

plt.figure(figsize=(14, 8))
df_socio.sort_values('Acesso_Saneamento', ascending=False).Acesso_Saneamento.plot(kind='bar', color='brown')
plt.title('Acesso a Saneamento Básico por Estado (%)', fontsize=16)
plt.xlabel('Estado', fontsize=12)
plt.ylabel('Acesso a Saneamento (%)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('/home/ubuntu/dados_complementares/saneamento_por_estado.png', dpi=300)

print("Dados e visualizações gerados com sucesso!")
