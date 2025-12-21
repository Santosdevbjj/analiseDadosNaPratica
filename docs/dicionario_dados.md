📖 **Dicionário de Dados: Amazon Logistics Dataset**

Este documento serve como a Fonte da Verdade técnica para as variáveis utilizadas no projeto de análise de performance logística. Ele detalha a tipagem, descrição e restrições de cada campo presente no dataset.

📊 **Estrutura das Variáveis**

| Atributo | Tipo de Dado | Descrição | Exemplo / Restrições |
|---|---|---|---|
| Order_ID | String | Identificador único alfanumérico do pedido. | 0x3a4b... |
| Agent_Age | Integer | Idade do entregador responsável em anos. | 18 - 50 |
| Agent_Rating | Float | Avaliação média histórica do entregador (0-5). | 4.7 |
| Store_Latitude | Float | Latitude do ponto de coleta (Origem). | Coordenadas Geográficas |
| Store_Longitude | Float | Longitude do ponto de coleta (Origem). | Coordenadas Geográficas |
| Drop_Latitude | Float | Latitude do local de entrega (Destino). | Coordenadas Geográficas |
| Drop_Longitude | Float | Longitude do local de entrega (Destino). | Coordenadas Geográficas |
| Order_Date | Date | Data completa da realização do pedido. | YYYY-MM-DD |
| Order_Year | String | Identificador de Ano e Mês do pedido. | 2022-12 |
| Order_Week | String | Semana do calendário para análise de sazonalidade. | 2022-W48 |
| Order_Time | Time | Horário exato do fechamento do pedido pelo cliente. | HH:MM:SS |
| Pickup_Time | Time | Horário em que o agente coletou o produto na loja. | HH:MM:SS |
| Weather | Categorical | Condição climática durante o percurso da entrega. | Sunny, Stormy, Fog |
| Traffic | Categorical | Nível de congestionamento no momento da rota. | Low, Medium, High, Jam |
| Vehicle | Categorical | Meio de transporte utilizado pelo entregador. | motorcycle, scooter, van |
| Area | Categorical | Classificação demográfica do local de destino. | Urban, Semi-Urban, Metropolitan |
| Delivery_Time | Integer | Tempo total decorrido da entrega em minutos. | Média: 125 min |
| Delivery_Status | Boolean | Variável alvo indicando cumprimento do prazo. | ontime, delay |
| Category | Categorical | Segmento do produto transportado. | Electronics, Grocery, Other |


🛠️ **Notas de Processamento**

 • **Tratamento de Missing Values:** Registros com dados ausentes em Traffic ou Weather foram imputados como "Unknown" para manter a integridade da volumetria de análise (43.739 linhas).
   
 •  **Conversão de Tipos:** Para fins analíticos, a coluna Delivery_Status foi mapeada como variável binária em modelos experimentais (1 para delay, 0 para ontime).
   
 • **Unidades de Medida:** Todos os tempos de entrega (Delivery_Time) estão padronizados em minutos, com limites operacionais identificados entre 10 e 270 minutos.

   
📈 **Relevância para o Negócio**
Este dicionário suporta a identificação de correlações críticas, como o impacto do tráfego Jam e áreas Semi-Urban na variável Delivery_Status, permitindo ações corretivas diretas na operação logística.


