import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Configurações de Estilo
sns.set_theme(style="whitegrid")
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'

def gerar_graficos():
    # 1. Carregamento dos dados processados
    # Certifique-se de que o caminho está correto conforme sua estrutura no GitHub
    try:
        df = pd.read_csv('data/processed/amazon_delivery_tratado.csv')
    except FileNotFoundError:
        print("Erro: Arquivo 'data/processed/amazon_delivery_tratado.csv' não encontrado.")
        return

    # Criar pasta de saída se não existir
    os.makedirs('reports/graficos', exist_ok=True)

    # --- GRÁFICO 1: Evolução dos atrasos ao longo do tempo (Exercício 1) ---
    plt.figure(figsize=(12, 6))
    df_delay = df[df['Delivery_Status'] == 'delay']
    atrasos_semana = df_delay.groupby('Order_Week')['Order_ID'].count().reset_index()
    sns.barplot(data=atrasos_semana, x='Order_Week', y='Order_ID', color='steelblue')
    plt.title('Evolução Semanal de Pedidos Atrasados', fontsize=14, fontweight='bold')
    plt.xlabel('Semana do Pedido')
    plt.ylabel('Quantidade de Atrasos')
    plt.xticks(rotation=45)
    plt.savefig('reports/graficos/atrasos_por_semana.png')
    plt.close()

    # --- GRÁFICO 2: Impacto do clima nos atrasos (Exercício 3) ---
    plt.figure(figsize=(10, 6))
    # Cálculo do percentual de atraso por condição climática
    prop_clima = df.groupby('Weather')['Delivery_Status'].value_counts(normalize=True).unstack().fillna(0)
    prop_clima = prop_clima['delay'].sort_values(ascending=False) * 100
    
    sns.barplot(x=prop_clima.values, y=prop_clima.index, palette='Reds_r')
    plt.title('Percentual de Atraso por Condição Climática', fontsize=14, fontweight='bold')
    plt.xlabel('% de Pedidos com Atraso')
    plt.ylabel('Clima')
    plt.savefig('reports/graficos/atrasos_por_clima.png')
    plt.close()

    # --- GRÁFICO 3: Veículos e eficiência (Exercício 4 - Barras Normalizadas) ---
    plt.figure(figsize=(10, 6))
    prop_veiculo = pd.crosstab(df['Vehicle'], df['Delivery_Status'], normalize='index') * 100
    prop_veiculo.plot(kind='barh', stacked=True, color=['#e74c3c', '#2ecc71'], ax=plt.gca())
    plt.title('Proporção de Status de Entrega por Veículo', fontsize=14, fontweight='bold')
    plt.xlabel('Percentual (%)')
    plt.ylabel('Tipo de Veículo')
    plt.legend(title='Status', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig('reports/graficos/atrasos_por_veiculo.png')
    plt.close()

    # --- GRÁFICO 4: Atrasos por área de entrega (Exercício 5) ---
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Area', hue='Delivery_Status', palette={'delay': '#e74c3c', 'ontime': '#2ecc71'})
    plt.title('Volume de Entregas por Área e Status', fontsize=14, fontweight='bold')
    plt.xlabel('Área de Entrega')
    plt.ylabel('Total de Pedidos')
    plt.savefig('reports/graficos/atrasos_por_area.png')
    plt.close()

    print("✅ Sucesso: 4 gráficos gerados em 'reports/graficos/'")

if __name__ == "__main__":
    gerar_graficos()
