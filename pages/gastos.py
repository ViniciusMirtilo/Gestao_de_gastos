import pandas as pd
import streamlit as st


base = pd.read_csv("c:/Users/Mirtilo/Downloads/py_panda/gasto.csv", encoding='latin-1')  #voce pode usar o encoding='latin-1' para evitar o erro de codificacao
df = pd.DataFrame(base)

col1 = st.columns(1) # espaço para 3 colunas

op = st.selectbox(
        'Escolhe uma data',
        df['Data'].unique()            
    )


st.write("### Gastos totais por data") # Exibe os gastos totais por data
gastos_por_data = df[df['Data'] == op]['Valor'].sum()
st.write(f"Total gastos R$ {gastos_por_data:.2f}")