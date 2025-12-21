📑 **Premissas da Análise e Governança de Dados**

Este documento estabelece o framework conceitual e técnico utilizado para garantir a integridade, transparência e reprodutibilidade dos insights gerados neste projeto.

1. Definição da Variável Alvo (Target)
 * Fonte da Verdade: A coluna Delivery_Status é a única métrica oficial de performance.
 
 * Classificação: * ontime: Entrega conforme SLA (Acordo de Nível de Serviço).
   
   * delay: Entrega em descumprimento com a promessa ao cliente.
     
 * Decisão: Optou-se por não reprocessar os tempos de entrega manualmente para respeitar a regra de negócio já consolidada no sistema de origem da Amazon.
   
**2. Escopo Metodológico**
 * Nível de Análise: O projeto está situado na camada de Analytics Descritivo e Diagnóstico.

   
 * Abordagem: Foco em identificar o onde e o porquê dos atrasos (causas raízes) através de análise de Pareto e segmentação de variáveis categóricas.
   
 * Limitação: Esta fase não contempla modelos de Machine Learning preditivo, focando em fornecer uma base sólida para decisões operacionais imediatas.


**3. Tratamento de Outliers e Variabilidade**
 * Métrica de Tempo: Delivery_Time foi analisado sob a ótica de tendência central (Média) e dispersão (Desvio Padrão).
   
 * Filtros de Qualidade: Foram considerados apenas registros com tempos de entrega positivos e consistentes com a realidade logística (evitando erros de input de sistema).


**4. Estratégia de Data Cleaning (Limpeza)**
 * Dados Ausentes (Nulls): Adotou-se a estratégia de manutenção da volumetria. Em vez de excluir linhas (o que poderia enviesar a taxa de atraso), valores nulos em variáveis como Weather ou Traffic foram rotulados como Unknown.
   
 * Integridade: Remoção sistemática de duplicatas para evitar a inflação artificial de métricas de sucesso ou falha.
   
 * Tipagem: Padronização rigorosa de formatos de data (Order_Date) e numéricos para garantir a precisão dos cálculos de agregação semanal.
   
**5. Granularidade Temporal**
 * Agregação: As datas foram convertidas para Order_Week (Semana do Ano).
   
 * Justificativa: A análise semanal suaviza ruídos diários e permite identificar tendências sazonais mais claras para a diretoria, facilitando o planejamento de capacidade de frota.
   
6. Ética e Viés de Análise
 * Neutralidade: As análises por Agent_Age e Agent_Rating buscam padrões operacionais, evitando conclusões discriminatórias e focando em correlações que possam indicar necessidade de treinamento ou suporte logístico.



