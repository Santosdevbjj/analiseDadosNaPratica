# Premissas da Análise

Para garantir coerência, transparência e reprodutibilidade, a análise de dados deste projeto foi conduzida com base nas seguintes premissas:

## 1. Definição de atraso
- A coluna `Delivery_Status` é considerada a fonte oficial para identificar entregas:
  - `ontime` → entrega realizada dentro do prazo;
  - `delay` → entrega realizada fora do prazo.
- Não foram recalculados prazos com base em regras externas ou SLAs não documentados.

## 2. Natureza da análise
- A análise é **descritiva e diagnóstica**, com foco em identificação de padrões e concentrações de atraso.
- Não há inferência causal estatística nem modelos preditivos neste estágio do projeto.

## 3. Tempo de entrega
- A variável `Delivery_Time` representa o tempo total de entrega em **minutos**.
- Métricas como média, desvio padrão, mínimo e máximo são utilizadas para avaliação da variabilidade.

## 4. Tratamento de dados ausentes
- Registros com valores ausentes em colunas não críticas foram mantidos.
- Valores ausentes em colunas numéricas foram convertidos para `NaN` quando necessário.
- Não foram realizadas imputações complexas para evitar viés artificial.

## 5. Qualidade e consistência dos dados
- Registros duplicados foram removidos.
- Conversões explícitas de tipos de dados foram realizadas para garantir consistência analítica.

## 6. Representatividade temporal
- O período analisado é considerado uma amostra válida do comportamento operacional recente da empresa.
- As análises temporais utilizam agregações semanais para facilitar interpretação gerencial.

Essas premissas asseguram que os resultados apresentados reflitam fielmente os dados disponíveis, mantendo alinhamento com o objetivo de apoiar decisões práticas e estratégicas.
