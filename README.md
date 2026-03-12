# 📦 Amazon Logistics Performance

### Diagnóstico de Eficiência Operacional e Redução de Atrasos em Entregas


---

## 1. Problema de Negócio

Operações logísticas com alto volume de entregas acumulam dados operacionais que, sem análise, permanecem invisíveis para gestores. O resultado é que decisões sobre frota, rotas e alocação de entregadores continuam sendo tomadas por percepção — e não por evidência.

Este projeto parte de uma realidade concreta: **atrasos em entregas geram insatisfação do cliente, aumentam reclamações e corroem o SLA logístico.** Sem saber *onde* e *por que* os atrasos acontecem, qualquer ação corretiva é um chute.

**A pergunta central deste projeto é:**
> *Quais fatores operacionais — clima, tráfego, tipo de veículo, área de entrega e perfil do entregador — mais contribuem para os atrasos, e que ações práticas podem reduzir a taxa de não-cumprimento de SLA?*

---

## 2. Contexto

O projeto analisa **43.739 registros operacionais reais** de entregas, cobrindo variáveis como:

- Condições climáticas no momento da entrega
- Nível de tráfego na rota
- Tipo de veículo utilizado (moto, scooter, bicicleta)
- Área de entrega (Urban, Semi-Urban, Metropolitano)
- Perfil do entregador (idade, avaliação)
- Categoria do produto entregue

A empresa já possuía esses dados registrados, mas não os utilizava de forma analítica. O objetivo foi transformar esse histórico operacional em **informação estratégica acionável** — com visualizações executivas e recomendações diretas para as áreas de Operações, Logística e Gestão.

> **Por que Python e não uma ferramenta No-Code (Looker, Power BI)?**
> Ferramentas de arraste-e-solte são rápidas para dashboards pontuais, mas limitam reprodutibilidade e escala. Com Python, cada etapa do pipeline é auditável via controle de versão, novos lotes de dados podem ser reprocessados com um único comando, e a análise estatística (como normalização e segmentação multivariada) vai além do que ferramentas de BI convencionais permitem nativamente.

---

## 3. Premissas da Análise

- A coluna `Delivery_Status` é a fonte oficial para classificar uma entrega como *delay* (atrasada) ou *ontime* (no prazo).
- O campo `Delivery_Time` está representado em **minutos**.
- Registros com valores ausentes em `Traffic_Density` e `Weather_Conditions` foram tratados como "informação desconhecida" e excluídos das análises que dependem dessas variáveis, sem impacto no volume total.
- As análises têm foco em **identificação de padrões descritivos**, não em inferência causal estatística — os insights orientam hipóteses para investigações futuras.
- O dataset representa uma amostra válida do comportamento operacional recente; sazonalidades de longo prazo não foram verificadas.

---

## 4. Estratégia da Solução

O projeto foi estruturado em pipeline modular com separação clara entre automação, análise e comunicação executiva:

**Etapa 1 — Limpeza e Preparação (`scripts/preparar_dados.py`)**
Ingestão do CSV bruto, padronização de tipos (`datetime`, `float`, `category`), tratamento de nulos, normalização de strings e criação de atributos derivados: `faixa_horaria`, `atraso_binario` e `tempo_entrega_categoria`. O script é autônomo — processa qualquer novo lote de dados sem intervenção manual.

**Etapa 2 — Análise Exploratória (`notebooks/01_exploracao_dados.ipynb`)**
Verificação de qualidade dos dados, distribuição das variáveis, identificação de outliers e mapeamento das correlações iniciais entre as variáveis operacionais e o status de entrega.

**Etapa 3 — Análise Temporal e de Sazonalidade (`notebooks/02_analise_atrasos_tempo.ipynb`)**
Investigação dos padrões de atraso ao longo do tempo: horários críticos, dias da semana com maior incidência e comportamento por período do dia.

**Etapa 4 — Segmentação Multivariada (`notebooks/03_analise_segmentos.ipynb`)**
Análise cruzada dos atrasos por clima, tráfego, veículo e área de entrega. Esta etapa identificou as combinações de fatores que concentram o maior risco operacional.

**Etapa 5 — Consolidação de Insights e Relatório Executivo (`notebooks/04_insights_negocio.ipynb` + `reports/`)**
Síntese dos principais achados em linguagem de negócio, geração automática do dashboard executivo (`dashboard_executivo.png`) e do relatório PDF (`relatorio_executivo.pdf`) — ambos prontos para apresentação à diretoria sem necessidade de edição manual.

---

## 5. Insights da Análise

**Alta variabilidade operacional**
O tempo médio de entrega é de **~125 minutos**, com desvio padrão de **~52 minutos** — o que indica baixíssima previsibilidade. A entrega mais rápida foi concluída em 10 min; a mais lenta, em 270 min (4,5h). Essa amplitude sugere que o problema não é a média, mas a inconsistência.

**Área Semi-Urban como ponto crítico**
É a única área onde o volume de entregas atrasadas **supera** o de entregas no prazo. Combinada com o uso de motocicletas como veículo principal nessa região, o resultado é a pior avaliação de clientes de toda a operação.

**Clima como multiplicador de falhas existentes**
Neblina e tempestades não criam atrasos por si sós — eles **amplificam falhas operacionais preexistentes**. Rotas já problemáticas em dias de sol tornam-se críticas em condições adversas.

**Tráfego intenso (`Jam`) e perfil do entregador**
Há correlação entre baixas avaliações de entregadores, tráfego nível Jam e alta taxa de atraso. Entregadores acima de 30 anos apresentam maior incidência de atrasos — o que pode indicar tanto experiência de rota quanto adaptação a condições adversas.

**Categoria "Outros" concentra 43% das entregas**
A sub-representação das demais categorias pode estar mascarando padrões específicos. Uma reclassificação dessa categoria é recomendada antes de análises preditivas.

![Dashboard Executivo](reports/graficos/dashboard_executivo.png)

---

## 6. Resultados

| Entregável | Descrição |
|---|---|
| `data/processed/amazon_delivery_tratado.csv` | Dataset limpo, tipado e com atributos derivados — pronto para análise ou modelagem |
| `scripts/preparar_dados.py` | Pipeline de ETL automatizado e reutilizável para novos lotes de dados |
| `notebooks/` (00 a 04) | Pipeline analítico completo: do dado bruto ao insight de negócio |
| `reports/relatorio_executivo.pdf` | Relatório executivo gerado automaticamente para apresentação à diretoria |
| `reports/graficos/dashboard_executivo.png` | Dashboard One-Page com os 4 KPIs principais da operação |
| `docs/` | Documentação técnica: premissas, dicionário de dados, conclusões e recomendações |

O projeto demonstra que **análise descritiva bem executada já gera recomendações acionáveis** — sem necessidade de Machine Learning para entregar valor real ao negócio.

---

## 7. Decisões Técnicas

**Por que análise diagnóstica antes de modelos preditivos?**
É tentador ir direto ao ML. Mas um modelo treinado sobre dados mal compreendidos apenas automatiza os erros existentes. A análise descritiva primeiro garantiu que as variáveis são confiáveis, as premissas estão validadas e os stakeholders entendem os padrões — o que torna qualquer modelo futuro mais sólido e auditável.

**Por que arquitetura modular (scripts + notebooks + reports)?**
Separar automação de análise de comunicação executiva não é perfeccionismo — é escalabilidade. O `preparar_dados.py` pode rodar em produção sem abrir nenhum notebook. Os notebooks documentam o raciocínio analítico. Os reports geram os ativos executivos sem retrabalho manual. Cada camada tem responsabilidade única.

**Por que ReportLab para o PDF e não exportar manualmente?**
Relatórios gerados manualmente são frágeis: uma atualização de dado exige retrabalho em todo o documento. O `gerar_relatorio_executivo.py` regenera o PDF completo com os dados mais recentes em segundos — o que transforma o relatório em um ativo vivo, não um documento estático.

**Trade-off aceito:** A profundidade da análise descritiva aumentou o escopo do projeto. Em contextos com prazo mais curto, a etapa de segmentação multivariada poderia ser simplificada — mas isso custaria os insights mais acionáveis do projeto.

---

## 8. Tecnologias Utilizadas

| Ferramenta | Uso no projeto |
|---|---|
| Python 3.8+ | Linguagem principal |
| Pandas | Limpeza, transformação e análise dos dados |
| NumPy | Operações numéricas e normalização |
| Matplotlib & Seaborn | Visualizações analíticas e executivas |
| Jupyter Notebook | Análise exploratória com narrativa analítica |
| ReportLab | Geração automatizada do relatório executivo em PDF |
| Git & GitHub | Versionamento, auditabilidade e portfólio público |

---

## 9. Como Executar o Projeto

**Pré-requisitos:** Python 3.8+, Git, 4 GB RAM

```bash
# 1. Clone o repositório
git clone https://github.com/Santosdevbjj/analiseDadosNaPratica.git
cd analiseDadosNaPratica

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute o pipeline de dados
python scripts/preparar_dados.py

# 4. Gere os visuais e o relatório executivo
python reports/gerar_relatorio_grafico.py
python reports/gerar_relatorio_executivo.py
```

> Para análise detalhada passo a passo, abra os notebooks na sequência `00 → 01 → 02 → 03 → 04` no Jupyter Notebook ou JupyterLab.

---

## 10. Aprendizados

O maior aprendizado deste projeto foi entender que **a qualidade da pergunta de negócio define a qualidade da análise** — não o volume de dados nem a sofisticação das ferramentas. Antes de escrever uma linha de código, dediquei tempo para definir com precisão o que significava "atraso" no contexto operacional, o que tornou todas as etapas seguintes mais diretas e menos sujeitas a retrabalho.

A separação em camadas (scripts, notebooks, reports) pareceu overhead no início, mas foi o que permitiu iterar rapidamente na análise sem quebrar o pipeline de dados — algo que não aconteceria em um único notebook monolítico.

O que faria diferente hoje: incluiria dados externos de clima e tráfego em tempo real desde o início, para enriquecer a análise de correlação e reduzir a dependência de variáveis categóricas simplificadas.

---

## 11. Próximos Passos

- [ ] **Modelo preditivo de atraso** — treinar classificador (Random Forest ou XGBoost) para prever probabilidade de atraso antes da entrega sair para campo
- [ ] **Integração com APIs** de clima (OpenWeatherMap) e tráfego (Google Maps) para enriquecer o dataset com dados em tempo real
- [ ] **Dashboard interativo** em Power BI ou Streamlit para monitoramento contínuo do SLA operacional
- [ ] **Reclassificação da categoria "Outros"** (43% das entregas) para desmascarar padrões ocultos por categoria de produto
- [ ] **Análise preditiva de avaliação do entregador** — identificar antecipadamente rotas e condições com maior risco de baixa avaliação

---

## Estrutura do Repositório

```
analiseDadosNaPratica/
├── data/
│   ├── raw/                          # Dados brutos originais (imutáveis)
│   └── processed/
│       └── amazon_delivery_tratado.csv   # Dataset limpo e tipado
├── scripts/
│   └── preparar_dados.py             # Pipeline ETL automatizado
├── notebooks/
│   ├── 00_preparacao_dados.ipynb     # Preparação e validação inicial
│   ├── 01_exploracao_dados.ipynb     # EDA e qualidade dos dados
│   ├── 02_analise_atrasos_tempo.ipynb    # Análise temporal e sazonalidade
│   ├── 03_analise_segmentos.ipynb    # Segmentação: clima, tráfego, veículo, área
│   └── 04_insights_negocio.ipynb    # Consolidação de insights estratégicos
├── reports/
│   ├── relatorio_executivo.pdf       # Relatório final para diretoria
│   ├── gerar_relatorio_grafico.py    # Geração automática de gráficos
│   ├── gerar_relatorio_executivo.py  # Geração automática do PDF
│   └── graficos/
│       └── dashboard_executivo.png   # Dashboard One-Page com 4 KPIs
├── docs/
│   ├── definicao_problema.md
│   ├── premissas_analiticas.md
│   ├── dicionario_dados.md
│   ├── conclusoes_tecnicas.md
│   └── recomendacoes_executivas.md
├── requirements.txt
└── README.md
```

---

**Autor:** Sérgio Santos

[![Portfólio Sérgio Santos](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://portfoliosantossergio.vercel.app)
[![LinkedIn Sérgio Santos](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz)
