🎯 **Problema de Negócio: Diagnóstico e Otimização Logística**

**1. Contexto e Desafio Estratégico**
A confiança do consumidor é o ativo mais valioso de uma operação de e-commerce. Recentemente, a operação logística da Amazon identificou um desvio crítico: o aumento sistemático do churn de clientes motivado pelo descumprimento dos SLAs (Service Level Agreements) de entrega.

O time de Customer Experience (CX) reportou um pico de reclamações no SAC, indicando que a percepção de valor da marca está sendo corroída por atrasos que a operação, até então, não conseguia justificar de forma quantitativa.

**2. Impacto nos KPIs de Negócio**
A ineficiência nas entregas não é apenas um problema logístico, mas uma perda financeira direta que afeta:
 
 * NPS (Net Promoter Score): Redução da lealdade do cliente devido à incerteza dos prazos.
 
 * Custo de Servir (Cost-to-Serve): Reentregas e atendimento ao cliente elevam o custo operacional por pacote.

 * LTV (Lifetime Value): Clientes que experienciam atrasos em suas primeiras compras possuem 40% menos chance de recompra.

**3. Objetivos da Intervenção Analítica**
Como Analista de Dados Sênior, minha missão neste projeto foi transformar a base histórica de 43.739 registros em um roteiro de ação para a diretoria, focando em:

 * Identificação de "Gargalos" Críticos: Mapear os ofensores por área, clima e tipo de veículo.
 
 * Diagnóstico de Performance por Segmento: Entender se o atraso é uma falha sistêmica ou se está isolado em nichos específicos (ex: Áreas Semi-Urbanas).
 
 * Priorização de Investimento (ROI): Definir onde a alocação de recursos (ex: troca de frota ou treinamento) gerará a maior redução percentual na taxa de atrasos.

**4. Perguntas Norteadoras (Business Questions)**
 
 
 **​1. Qual a volumetria atual de atrasos e sua tendência semanal?**
​Resposta: A base de dados revela uma volumetria de 43.739 pedidos, com uma taxa de atraso que flutua consideravelmente. A tendência semanal mostra picos de atraso que coincidem com períodos de alta demanda. O tempo médio de entrega é de 125 minutos, mas o desvio padrão de 52 minutos indica que a operação sofre com falta de previsibilidade, tornando a experiência do cliente inconsistente semana a semana.

**​2. O clima severo é a causa principal ou apenas um agravante de falhas operacionais?**
​Resposta: O clima atua como um potencializador crítico. Embora ocorram atrasos em dias ensolarados, as condições de Fog (Neblina) e Stormy (Tempestades) apresentam as maiores taxas proporcionais de atraso. O dado revela que a operação não possui um plano de contingência resiliente ao clima, transformando condições meteorológicas adversas em gargalos logísticos imediatos.

**​3. O modelo de entrega por motocicletas é eficiente em todas as zonas demográficas?**
​Resposta: Não. O modelo de motocicletas demonstra ineficiência aguda na zona Semi-Urban. Enquanto em áreas Metropolitanas e Urbanas a agilidade da moto ajuda a mitigar o tráfego, na zona Semi-Urban o volume de atrasos supera o de entregas no prazo. Isso sugere que a infraestrutura dessas áreas ou as distâncias percorridas não favorecem esse modal, sendo o principal ponto de atenção para troca de frota.

**​4. Existe correlação entre o perfil/avaliação do entregador e a eficiência da rota?**
​Resposta: Sim. Observou-se que entregadores com avaliações (Agent_Rating) mais baixas estão frequentemente associados a tempos de entrega maiores e status de delay. Além disso, o cruzamento de dados sugere que entregadores na faixa etária acima de 30 anos enfrentam desafios maiores de tempo em certas rotas de tráfego pesado (Jam), o que pode indicar a necessidade de otimização de roteirização ou treinamentos específicos para uso de tecnologias de navegação.
 
 
 
 
 
 ---





