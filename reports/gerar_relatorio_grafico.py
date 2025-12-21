import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Configurações globais de estética
sns.set_theme(style="whitegrid")
plt.rcParams['figure.dpi'] = 300

def gerar_dashboard(df):
    """Gera uma visão consolidada (Dashboard) em uma única imagem."""
    fig = plt.figure(figsize=(20, 12))
    fig.suptitle('📊 Dashboard Executivo: Performance Logística Amazon', fontsize=24, fontweight='bold', y=0.95)

    # 1. Evolução Semanal (Top Left)
    ax1 = plt.subplot(2, 2, 1)
    df_delay = df[df['Delivery_Status'] == 'delay']
    atrasos_semana = df_delay.groupby('Order_Week')['Order_ID'].count().reset_index()
    sns.lineplot(data=atrasos_semana, x='Order_Week', y='Order_ID', marker='o', color='red', ax=ax1)
    ax1.set_title('Tendência de Atrasos por Semana', fontsize=14)
    ax1.tick_params(axis='x', rotation=45)

    # 2. Clima vs Performance (Top Right)
    ax2 = plt.subplot(2, 2, 2)
    prop_clima = df.groupby('Weather')['Delivery_Status'].value_counts(normalize=True).unstack().fillna(0)['delay'] * 100
    prop_clima.sort_values().plot(kind='barh', color='salmon', ax=ax2)
    ax2.set_title('% de Atraso por Condição Climática', fontsize=14)
    ax2.set_xlabel('Percentual (%)')

    # 3. Eficiência por Veículo (Bottom Left)
    ax3 = plt.subplot(2, 2, 3)
    prop_veiculo = pd.crosstab(df['Vehicle'], df['Delivery_Status'], normalize='index') * 100
    prop_veiculo.plot(kind='bar', stacked=True, color=['#e74c3c', '#2ecc71'], ax=ax3)
    ax3.set_title('Status de Entrega por Veículo (Normalizado)', fontsize=14)
    ax3.legend(loc='lower right', fontsize=8)

    # 4. Concentração por Área (Bottom Right)
    ax4 = plt.subplot(2, 2, 4)
    sns.countplot(data=df, x='Area', hue='Delivery_Status', palette={'delay': '#e74c3c', 'ontime': '#2ecc71'}, ax=ax4)
    ax4.set_title('Volume de Entregas por Área Geográfica', fontsize=14)

    plt.tight_layout(rect=[0, 0.03, 1, 0.92])
    plt.savefig('reports/graficos/dashboard_executivo.png')
    plt.close()
    print("✅ Dashboard consolidado gerado com sucesso!")

def gerar_graficos_individuais(df):
    """Mantém a geração dos gráficos separados para o relatório PDF."""
    os.makedirs('reports/graficos', exist_ok=True)
    
    # Exemplo resumido: Atrasos por Área
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Area', hue='Delivery_Status', palette={'delay': '#e74c3c', 'ontime': '#2ecc71'})
    plt.title('Volume de Entregas por Área')
    plt.savefig('reports/graficos/atrasos_por_area.png')
    plt.close()
    # (Os outros gráficos seguem a mesma lógica do script anterior...)

if __name__ == "__main__":
    try:
        data = pd.read_csv('data/processed/amazon_delivery_tratado.csv')
        gerar_graficos_individuais(data)
        gerar_dashboard(data)
    except Exception as e:
        print(f"❌ Erro ao processar: {e}")
