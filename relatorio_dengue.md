# Relatório de Análise de Dados sobre Dengue no Brasil

## Introdução

Este relatório apresenta os resultados da análise de dados sobre casos de dengue no Brasil, utilizando dados coletados do DATASUS. A análise foi estruturada para identificar padrões sazonais, distribuição geográfica e tendências temporais dos casos de dengue, fornecendo insights importantes para a compreensão da dinâmica da doença no país.

## Metodologia

Os dados foram coletados do DATASUS, processados e analisados utilizando Python e suas bibliotecas de análise de dados (pandas) e visualização (matplotlib, seaborn). O conjunto de dados inclui informações sobre casos prováveis de dengue por Unidade Federativa (UF) e mês, cobrindo o período de 2014 a 2025.

## Resultados e Análises

### 1. Distribuição Temporal dos Casos de Dengue

![Casos por Mês](/home/ubuntu/visualizacoes/casos_por_mes.png)

A análise temporal dos casos de dengue no Brasil revela um padrão sazonal muito claro. Observa-se que:

- O pico de casos ocorre em abril, com 4.304.428 casos registrados
- Há um aumento progressivo de casos a partir de janeiro, atingindo o pico em abril
- Após abril, ocorre uma queda acentuada até agosto
- Os meses de agosto a outubro apresentam os menores números de casos
- A partir de novembro, os casos começam a aumentar novamente

Este padrão sazonal está fortemente relacionado com as condições climáticas favoráveis à proliferação do mosquito Aedes aegypti, vetor da dengue. O período de maior incidência coincide com os meses mais quentes e úmidos no Brasil, condições ideais para a reprodução do mosquito.

### 2. Distribuição Geográfica dos Casos

![Top 10 Estados](/home/ubuntu/visualizacoes/top10_estados.png)

A distribuição geográfica dos casos de dengue mostra uma concentração significativa em determinados estados:

- São Paulo lidera com aproximadamente 5,37 milhões de casos
- Minas Gerais aparece em segundo lugar com cerca de 3,43 milhões de casos
- Paraná ocupa a terceira posição com 3,11 milhões de casos
- Os três estados mais afetados concentram aproximadamente 65% do total de casos no país
- Há uma grande disparidade entre os estados mais afetados e os demais

Esta concentração pode ser explicada por diversos fatores, incluindo densidade populacional, condições climáticas específicas, urbanização e eficácia das políticas de controle do vetor em cada estado.

### 3. Padrões Sazonais por Estado

![Heatmap Estados x Meses](/home/ubuntu/visualizacoes/heatmap_estados_meses.png)

O mapa de calor que relaciona estados e meses revela padrões interessantes:

- São Paulo apresenta alta concentração de casos entre março e maio
- Minas Gerais mostra um padrão similar, com pico em março e abril
- Paraná apresenta um comportamento atípico, com alta concentração em dezembro
- A maioria dos estados segue o padrão nacional, com picos entre março e maio
- Estados do Norte e Nordeste apresentam distribuição mais uniforme ao longo do ano

Estas diferenças regionais podem estar relacionadas a variações climáticas específicas de cada região, bem como a fatores socioeconômicos e de infraestrutura urbana.

### 4. Análise por Região

![Casos por Região](/home/ubuntu/visualizacoes/casos_por_regiao.png)

A análise por região geográfica do Brasil mostra comportamentos distintos:

- A região Sudeste apresenta o maior número de casos, com picos expressivos em março e abril
- A região Sul mostra um comportamento atípico, com um pico significativo em dezembro
- As regiões Centro-Oeste e Nordeste seguem padrões similares, com picos entre março e maio
- A região Norte apresenta o menor número de casos e uma distribuição mais uniforme ao longo do ano

![Distribuição por Região](/home/ubuntu/visualizacoes/distribuicao_por_regiao.png)

Em termos percentuais:
- A região Sudeste concentra 43,6% dos casos
- A região Sul representa 22,0% dos casos
- O Nordeste corresponde a 16,1% dos casos
- O Centro-Oeste representa 14,8% dos casos
- A região Norte apresenta apenas 3,4% dos casos

Esta distribuição reflete não apenas as condições climáticas favoráveis ao vetor, mas também a densidade populacional e o grau de urbanização das regiões.

### 5. Sazonalidade por Trimestre e Região

![Casos por Trimestre](/home/ubuntu/visualizacoes/casos_por_trimestre.png)

A análise trimestral revela padrões sazonais importantes:

- O verão (jan-mar) e o outono (abr-jun) concentram a maioria dos casos em todas as regiões
- O Sudeste apresenta números expressivamente maiores no verão e outono
- A região Sul mostra um comportamento diferenciado, com alta incidência na primavera (out-dez)
- O inverno (jul-set) apresenta os menores números em todas as regiões
- O Nordeste e Centro-Oeste mostram padrões similares, com picos na primavera

Esta análise trimestral confirma a forte sazonalidade da dengue no Brasil, com variações regionais significativas que devem ser consideradas nas estratégias de controle.

## Conclusões

A análise dos dados de dengue no Brasil revela padrões importantes que podem orientar políticas públicas de prevenção e controle:

1. **Sazonalidade marcante**: Os casos de dengue apresentam um padrão sazonal claro, com pico entre março e abril, indicando a necessidade de intensificar as ações preventivas nos meses que antecedem este período.

2. **Concentração geográfica**: Três estados (São Paulo, Minas Gerais e Paraná) concentram a maioria dos casos, sugerindo a necessidade de ações específicas nestas regiões.

3. **Variações regionais**: Cada região do Brasil apresenta padrões distintos, com a região Sul mostrando um comportamento atípico com pico em dezembro, enquanto as demais regiões seguem o padrão nacional.

4. **Predominância do Sudeste**: A região Sudeste concentra quase metade dos casos do país, refletindo sua alta densidade populacional e urbanização.

5. **Baixa incidência no inverno**: O período de julho a setembro apresenta os menores números de casos em todas as regiões, oferecendo uma janela estratégica para ações preventivas antes do próximo ciclo.

## Recomendações

Com base nos resultados obtidos, recomenda-se:

1. Intensificar campanhas de prevenção e controle do vetor nos meses que antecedem o pico de casos (dezembro a fevereiro).

2. Desenvolver estratégias específicas para os estados mais afetados, considerando suas particularidades.

3. Adaptar o calendário de ações preventivas de acordo com as variações regionais identificadas.

4. Aproveitar o período de baixa incidência (inverno) para fortalecer a infraestrutura de saúde e preparar-se para o próximo ciclo.

5. Realizar estudos mais aprofundados para compreender o comportamento atípico da região Sul, com pico em dezembro.

6. Integrar dados climáticos e socioeconômicos para uma análise mais completa dos fatores que influenciam a incidência da dengue.

## Limitações do Estudo

Este estudo apresenta algumas limitações que devem ser consideradas:

1. Os dados não incluem informações sobre óbitos, impossibilitando a análise de letalidade.

2. Não foram considerados fatores climáticos específicos que podem influenciar a proliferação do vetor.

3. A análise não contempla variáveis socioeconômicas que podem estar relacionadas à incidência da dengue.

4. Possíveis subnotificações podem afetar a precisão dos dados, especialmente em regiões com menor acesso a serviços de saúde.

## Próximos Passos

Para aprofundar a compreensão da dinâmica da dengue no Brasil, sugere-se:

1. Incorporar dados climáticos (temperatura, precipitação) para correlacionar com a incidência da doença.

2. Analisar séries temporais mais longas para identificar tendências de longo prazo.

3. Incluir dados socioeconômicos e de infraestrutura urbana na análise.

4. Desenvolver modelos preditivos para antecipar surtos e orientar ações preventivas.

5. Realizar análises comparativas com outras arboviroses transmitidas pelo mesmo vetor (Zika, Chikungunya).
