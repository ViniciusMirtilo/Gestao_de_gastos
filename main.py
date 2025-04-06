# Objetivo do App:
# Upload de arquivo .csv com o extrato bancário.-

# Limpeza e tratamento dos dados.-

# Classificação dos gastos por categorias.-

# Mostrar dashboards com:

# Gastos totais por categoria.-

# Gráficos (barras, pizza, evolução mensal).

# Insights importantes (ex: qual categoria mais gastou, qual mês mais gastou).

# Interface agradável e organizada.


import pandas as pd
import streamlit as st


base = pd.read_csv("gasto.csv",encoding='latin-1')  #voce pode usar o encoding='latin-1' para evitar o erro de codificacao

df = pd.DataFrame(base)
df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')  # Converte para numérico, substitui valores inválidos por NaN

st.title("Análise de Gastos Pessoais")

st.dataframe(df)

col1, col2, col3 = st.columns(3) # espaço para 3 colunas


with col1:
    
    st.write("### Gastos totais por categoria")
    
    op1 = st.selectbox(
        'Escolhe uma Categoria',
        df['Categoria'].unique()            
    )
    
    gastos_por_categoria = df[df['Categoria'] == op1]['Valor'].sum()
    st.write(f"Total gastos R$ {gastos_por_categoria:.2f}")
with col2:
    print("### Gastos totais por categoria")