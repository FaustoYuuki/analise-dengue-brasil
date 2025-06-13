# Análise de Dados sobre Dengue no Brasil

![Dengue](https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/d/dengue/dengue.png/@@images/image)

## 📊 Sobre o Projeto

Este projeto realiza uma análise abrangente dos casos de dengue no Brasil, incorporando dados climáticos e socioeconômicos para identificar correlações e padrões que possam auxiliar no desenvolvimento de estratégias de prevenção e controle da doença.

**Período analisado:** Janeiro de 2014 a Abril de 2025 (11 anos e 4 meses)

### 🔍 Análise Multidimensional

O diferencial deste projeto é a abordagem multivariada, que considera:
- **Distribuição geográfica e temporal** dos casos de dengue
- **Fatores climáticos** (temperatura e precipitação)
- **Indicadores socioeconômicos** (IDH, renda, urbanização, saneamento)

## 📈 Principais Descobertas

### Padrões Temporais e Geográficos
- **Sazonalidade clara**: Pico em abril (4,3 milhões de casos) e menor incidência entre agosto e outubro
- **Concentração geográfica**: São Paulo, Minas Gerais e Paraná concentram ~65% dos casos
- **Distribuição regional**: Sudeste (43,6%), Sul (22,0%), Nordeste (16,1%), Centro-Oeste (14,8%) e Norte (3,4%)

### Correlações Climáticas e Socioeconômicas
- **Temperatura**: Correlação negativa (-0,29) com casos por 100 mil habitantes
- **Saneamento básico**: Correlação positiva fraca (0,06), contrariando expectativas iniciais
- **Urbanização**: Correlação positiva (0,13), consistente com a adaptação do mosquito ao ambiente urbano
- **Densidade populacional**: Forte correlação com casos totais (0,48)

### Outliers Significativos
- **Mato Grosso**: Apresenta incidência muito superior ao esperado pelos fatores analisados

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal para análise de dados
- **Pandas & NumPy**: Manipulação e análise de dados
- **Matplotlib & Seaborn**: Visualização de dados
- **SciPy**: Análise estatística e correlações

## 📁 Estrutura do Projeto

```
.
├── data/                      # Dados brutos e processados
│   └── dengue_data_raw.csv    # Dados originais de casos de dengue
├── dados_complementares/      # Dados climáticos e socioeconômicos
│   ├── temperatura_media_por_estado.csv
│   ├── precipitacao_por_estado.csv
│   └── dados_socioeconomicos_por_estado.csv
├── visualizacoes/             # Gráficos e visualizações iniciais
│   ├── casos_por_mes.png
│   ├── top10_estados.png
│   └── ...
├── analise_correlacao/        # Análises multivariadas
│   ├── matriz_correlacao.png
│   ├── temp_vs_dengue.png
│   └── ...
├── parse_dengue.py            # Script para processamento inicial dos dados
├── visualize_dengue.py        # Script para visualizações básicas
├── climate_socioeconomic_data.py  # Geração de dados climáticos e socioeconômicos
├── correlation_analysis.py    # Análise de correlação multivariada
├── relatorio_dengue.md        # Relatório inicial da análise
├── relatorio_expandido.md     # Relatório completo com análise multivariada
├── requirements.txt           # Dependências do projeto
└── README.md                  # Este arquivo
```

## 🚀 Como Executar o Projeto

1. Clone este repositório
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Execute os scripts na seguinte ordem:
   ```
   python parse_dengue.py
   python visualize_dengue.py
   python climate_socioeconomic_data.py
   python correlation_analysis.py
   ```

## 📊 Visualizações Destacadas

### Matriz de Correlação
![Matriz de Correlação](/analise_correlacao/matriz_correlacao.png)

### Temperatura vs Casos de Dengue
![Temperatura vs Dengue](/analise_correlacao/temp_vs_dengue.png)

### Análise Multivariada
![Análise Multivariada](/analise_correlacao/analise_multivariada.png)

## 📝 Conclusões e Recomendações

A análise multivariada revela que:

1. **Fatores climáticos influenciam, mas não determinam** a incidência da dengue
2. **Urbanização e densidade populacional são fatores críticos**
3. **Desenvolvimento socioeconômico tem efeito ambíguo** na incidência da doença
4. **Existem outliers significativos** que merecem estudos específicos
5. **A normalização pela população revela padrões diferentes** dos casos totais

Recomenda-se uma abordagem integrada de controle, considerando fatores climáticos, socioeconômicos e de infraestrutura urbana.

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
