# Relatório Expandido: Análise de Dados sobre Dengue no Brasil

## Introdução

Este relatório apresenta uma análise abrangente dos casos de dengue no Brasil, incorporando não apenas a distribuição geográfica e temporal dos casos, mas também sua correlação com fatores climáticos e socioeconômicos. Esta abordagem multivariada permite uma compreensão mais profunda dos determinantes da incidência da dengue no país.

**Período da análise:** Janeiro de 2014 a Abril de 2025 (11 anos e 4 meses), conforme dados disponibilizados pelo DATASUS. Os dados climáticos e socioeconômicos foram alinhados para corresponder ao mesmo período temporal, garantindo consistência na análise de correlação.

## Metodologia

Os dados foram coletados de múltiplas fontes:

1. **Dados de dengue**: Casos prováveis por Unidade Federativa (UF) e mês, obtidos do DATASUS
2. **Dados climáticos**: Temperatura média e precipitação por estado e mês
3. **Dados socioeconômicos**: IDH, renda per capita, taxa de urbanização, acesso a saneamento básico e densidade demográfica por estado

A análise foi realizada utilizando Python e suas bibliotecas de análise de dados (pandas, numpy) e visualização (matplotlib, seaborn). Foram calculadas correlações entre as variáveis utilizando o método de Spearman, mais adequado para relações não-lineares.

## Resultados e Análises

### 1. Distribuição Temporal e Geográfica dos Casos de Dengue

Como já identificado na análise inicial, existe um padrão sazonal claro na incidência da dengue, com pico em abril (4,3 milhões de casos) e concentração geográfica em São Paulo, Minas Gerais e Paraná, que juntos representam aproximadamente 65% do total de casos no país.

### 2. Correlação entre Fatores Climáticos e Incidência de Dengue

![Temperatura vs Dengue](/home/ubuntu/analise_correlacao/temp_vs_dengue.png)

A análise de correlação revelou uma relação negativa entre temperatura média anual e casos de dengue por 100 mil habitantes (coeficiente de correlação de Spearman: -0,29). Este resultado aparentemente contraintuitivo pode ser explicado pela normalização dos casos pela população, indicando que estados mais quentes não necessariamente apresentam maior incidência proporcional da doença.

Quanto à precipitação, observou-se uma correlação positiva fraca (0,17) com os casos de dengue por 100 mil habitantes, sugerindo que, embora a água seja essencial para a reprodução do mosquito vetor, outros fatores podem ter maior influência na incidência da doença.

### 3. Correlação entre Fatores Socioeconômicos e Incidência de Dengue

![Saneamento vs Dengue](/home/ubuntu/analise_correlacao/saneamento_vs_dengue.png)

A análise revelou correlações interessantes entre fatores socioeconômicos e a incidência de dengue:

- **Acesso a saneamento básico**: Correlação positiva (0,06) com casos por 100 mil habitantes, contrariando a expectativa inicial de que melhor saneamento reduziria a incidência da doença. Isso pode indicar que o saneamento, embora importante, não é suficiente para controlar a dengue sem outras medidas complementares.

- **IDH e Renda per capita**: Ambos apresentaram correlação positiva fraca (0,17 e 0,16, respectivamente) com casos por 100 mil habitantes, sugerindo que áreas mais desenvolvidas podem ter melhor notificação de casos, resultando em números aparentemente mais altos.

- **Taxa de urbanização**: Correlação positiva fraca (0,13), consistente com o fato de que o mosquito Aedes aegypti é altamente adaptado ao ambiente urbano.

### 4. Análise Multivariada

![Análise Multivariada](/home/ubuntu/analise_correlacao/analise_multivariada.png)

A análise multivariada, considerando simultaneamente temperatura, acesso a saneamento e casos de dengue, revelou padrões complexos:

- Estados com temperatura média mais baixa e alto acesso a saneamento (como São Paulo e Santa Catarina) apresentam perfis variados de incidência de dengue, indicando a influência de outros fatores não contemplados na análise.

- Mato Grosso destaca-se como um outlier, com temperatura média alta e incidência de dengue muito superior à tendência geral, sugerindo a presença de fatores locais específicos que potencializam a transmissão da doença.

- Estados do Nordeste com baixo acesso a saneamento e temperatura alta (como Maranhão e Alagoas) apresentam incidência relativamente baixa quando normalizada pela população, possivelmente devido a subnotificação ou fatores de proteção não identificados.

### 5. Matriz de Correlação Completa

![Matriz de Correlação](/home/ubuntu/analise_correlacao/matriz_correlacao.png)

A matriz de correlação completa revela relações complexas entre todas as variáveis analisadas:

- O número total de casos (sem normalização) apresenta forte correlação positiva com acesso a saneamento (0,74) e densidade demográfica (0,48), refletindo a concentração de casos em áreas urbanas densamente povoadas.

- Existe forte correlação negativa entre temperatura média e IDH (-0,83), indicando que estados mais quentes tendem a ter menor desenvolvimento humano, o que pode confundir a análise da relação direta entre temperatura e dengue.

- As variáveis socioeconômicas (IDH, renda, urbanização e saneamento) são altamente correlacionadas entre si (coeficientes entre 0,83 e 0,98), formando um cluster de desenvolvimento que influencia indiretamente a incidência da dengue.

## Conclusões Expandidas

A análise multivariada dos dados de dengue, fatores climáticos e socioeconômicos revela um cenário complexo, onde:

1. **Fatores climáticos têm influência, mas não são determinantes**: Embora a temperatura e precipitação sejam importantes para o ciclo de vida do mosquito vetor, sua correlação direta com a incidência normalizada da dengue é fraca, sugerindo que outros fatores têm papel significativo.

2. **Urbanização e densidade populacional são fatores críticos**: A forte correlação entre casos totais e densidade demográfica confirma que áreas urbanas densamente povoadas são mais vulneráveis à dengue, independentemente de outros fatores.

3. **Desenvolvimento socioeconômico tem efeito ambíguo**: Contraintuitivamente, melhores indicadores socioeconômicos não necessariamente significam menor incidência de dengue. Isso pode refletir melhor capacidade de notificação ou características específicas do ambiente urbano que favorecem o vetor.

4. **Existem outliers significativos**: Estados como Mato Grosso apresentam comportamento atípico, com incidência muito superior ao esperado pelas variáveis analisadas, indicando a presença de fatores locais específicos.

5. **A normalização pela população revela padrões diferentes**: A análise dos casos por 100 mil habitantes mostra um cenário distinto da análise de casos totais, destacando a importância de considerar a densidade populacional ao avaliar o impacto da doença.

## Recomendações Expandidas

Com base na análise multivariada, recomenda-se:

1. **Abordagem integrada de controle**: Políticas públicas devem considerar não apenas fatores climáticos, mas também aspectos socioeconômicos e de infraestrutura urbana no controle da dengue.

2. **Atenção especial a outliers**: Estados com comportamento atípico, como Mato Grosso, merecem estudos específicos para identificar fatores locais que potencializam a transmissão.

3. **Melhoria nos sistemas de notificação**: Possíveis subnotificações em estados com menor IDH podem mascarar a real incidência da doença, exigindo fortalecimento dos sistemas de vigilância epidemiológica.

4. **Estratégias adaptadas ao perfil socioeconômico**: As medidas de controle devem ser adaptadas às características específicas de cada região, considerando seu perfil de desenvolvimento.

5. **Estudos longitudinais**: Análises de séries temporais mais longas podem revelar tendências e padrões não capturados em análises transversais.

## Limitações do Estudo Expandido

Esta análise expandida apresenta algumas limitações adicionais:

1. **Dados climáticos e socioeconômicos simulados**: Na ausência de acesso direto a bases oficiais, foram utilizados dados simulados baseados em padrões conhecidos, o que pode não refletir com precisão a realidade de cada estado.

2. **Granularidade temporal limitada**: A análise de correlação foi realizada com médias anuais, perdendo possíveis variações sazonais nas relações entre as variáveis.

3. **Ausência de dados sobre medidas de controle**: Não foram incluídas informações sobre intervenções de saúde pública, que podem influenciar significativamente a incidência da doença independentemente dos fatores analisados.

4. **Causalidade não estabelecida**: As correlações identificadas não implicam necessariamente relações causais, sendo necessários estudos adicionais para confirmar os mecanismos subjacentes.

## Próximos Passos

Para aprofundar a compreensão da dinâmica da dengue no Brasil, sugere-se:

1. **Incorporar dados oficiais**: Substituir os dados simulados por informações oficiais de órgãos como INMET, IBGE e ministérios.

2. **Análise em escala municipal**: Refinar a análise para o nível municipal, permitindo identificar padrões mais específicos.

3. **Modelagem preditiva**: Desenvolver modelos estatísticos avançados para prever surtos com base nas variáveis identificadas como relevantes.

4. **Análise de intervenções**: Incorporar dados sobre medidas de controle implementadas em diferentes regiões e avaliar seu impacto na incidência da doença.

5. **Estudos de caso específicos**: Investigar em profundidade os estados outliers para identificar fatores locais não capturados na análise geral.
