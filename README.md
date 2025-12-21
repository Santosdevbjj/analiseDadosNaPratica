# analiseDadosNaPratica
Você faz parte do time de Dados de uma empresa de logística. Nas últimas semanas, o time de CX reportou aumento de reclamações: clientes dizendo que o prazo não está sendo cumprido.

---


graph TD
    A[data/raw/amazon_delivery.csv] -->|scripts/preparar_dados.py| B(data/processed/amazon_delivery_tratado.csv)
    B --> C{Notebooks de Análise}
    C -->|02_analise_tempo| D[Evolução Semanal]
    C -->|03_analise_segmentos| E[Análise por Clima/Veículo]
    D --> F[reports/graficos/atrasos_por_semana.png]
    E --> G[reports/graficos/atrasos_por_clima.png]
    G --> H((Relatório Executivo Final))
    F --> H






---



