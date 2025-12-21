import pandas as pd

# =========================================
# Preparação dos Dados - Amazon Delivery
# =========================================

# Caminhos
INPUT_PATH = "../data/raw/amazon_delivery_dados_alunos.csv"
OUTPUT_PATH = "../data/processed/amazon_delivery_tratado.csv"

# Carregamento
df = pd.read_csv(INPUT_PATH)

# -------------------------------
# Tratamento de Tipos Numéricos
# -------------------------------
cols_numericas = [
    "Agent_Rating",
    "Store_Latitude", "Store_Longitude",
    "Drop_Latitude", "Drop_Longitude"
]

for col in cols_numericas:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# -------------------------------
# Conversão de Datas
# -------------------------------
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# -------------------------------
# Remoção de Duplicados
# -------------------------------
df = df.drop_duplicates()

# -------------------------------
# Salvando Dataset Tratado
# -------------------------------
df.to_csv(OUTPUT_PATH, index=False)

print("✅ Arquivo amazon_delivery_tratado.csv gerado com sucesso!")
print(f"📁 Caminho: {OUTPUT_PATH}")
print(f"📊 Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")
