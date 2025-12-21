# Dicionário de Dados  
## Dataset: Amazon Delivery

Este documento descreve as variáveis presentes no dataset utilizado no projeto de análise de atrasos de entregas.

| Coluna | Descrição |
|------|----------|
| Order_ID | Identificador único do pedido/entrega |
| Agent_Age | Idade do entregador (em anos) |
| Agent_Rating | Avaliação média do entregador |
| Store_Latitude | Latitude do ponto de origem (loja ou centro de distribuição) |
| Store_Longitude | Longitude do ponto de origem |
| Drop_Latitude | Latitude do destino (cliente) |
| Drop_Longitude | Longitude do destino |
| Order_Date | Data em que o pedido foi realizado |
| Order_Year | Ano e mês do pedido |
| Order_Week | Semana do calendário no formato ano-semana |
| Order_Time | Horário em que o pedido foi feito |
| Pickup_Time | Horário em que o pedido foi coletado para entrega |
| Weather | Condição climática no momento da entrega (ex.: Sunny, Fog, Stormy) |
| Traffic | Condição de tráfego (Low, Medium, High, Jam) |
| Vehicle | Tipo de veículo utilizado na entrega |
| Area | Tipo de área de entrega (Metropolitan, Urban, Semi-Urban, Other) |
| Delivery_Time | Tempo total de entrega em minutos |
| Delivery_Status | Status da entrega (`ontime` ou `delay`) |
| Category | Categoria do produto entregue |

## Observações
- As variáveis geográficas (latitude e longitude) não foram exploradas nesta fase, mas permitem análises espaciais futuras.
- O dataset contém dados históricos suficientes para análises descritivas e diagnósticas.
- O dicionário facilita entendimento do dataset por públicos técnicos e não técnicos.
