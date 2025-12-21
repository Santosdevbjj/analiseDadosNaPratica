from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

file_path = "reports/relatorio_executivo.pdf"

doc = SimpleDocTemplate(
    file_path,
    pagesize=A4,
    rightMargin=36,
    leftMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()
story = []

texto = """
<b>Relatório Executivo – Análise de Atrasos de Entregas da Amazon</b><br/><br/>

<b>1. Contexto e Problema de Negócio</b><br/>
A operação logística de entregas enfrenta aumento no volume de pedidos fora do prazo,
impactando a experiência do cliente e a previsibilidade operacional.<br/><br/>

<b>2. Estratégia de Análise</b><br/>
A análise seguiu abordagem descritiva e diagnóstica, explorando dimensões como tempo,
área de entrega, clima, tráfego, tipo de veículo e perfil do entregador.<br/><br/>

<b>3. Principais Insights</b><br/>
- Área Semi-Urban concentra maior volume de atrasos;<br/>
- Clima adverso aumenta o risco de atraso;<br/>
- Motocicletas apresentam maior taxa de atraso;<br/>
- Tráfego intenso (Jam) está associado a entregas fora do prazo.<br/><br/>

<b>4. Recomendações</b><br/>
- Priorizar ações na área Semi-Urban;<br/>
- Avaliar mudança de veículos em regiões críticas;<br/>
- Ajustar planejamento conforme clima e tráfego;<br/>
- Criar dashboards de monitoramento contínuo.<br/><br/>

<b>5. Conclusão</b><br/>
A análise de dados permitiu transformar informações operacionais em decisões práticas,
apoiando a redução de atrasos e a melhoria da experiência do cliente.
"""

story.append(Paragraph(texto, styles["Normal"]))
story.append(Spacer(1, 12))

doc.build(story)

print("✅ relatorio_executivo.pdf gerado com sucesso!")
