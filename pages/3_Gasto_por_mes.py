import pandas as pd
import streamlit as st
import plotly.express as px

# Linha do tempo dos gastos, comparação mês a mês.

base = pd.read_csv("c:/Users/Mirtilo/Downloads/py_panda/data/gasto.csv", encoding='latin-1')  # voce pode usar o encoding='latin-1' para evitar o erro de codificacao

# Configuração da página
st.set_page_config(page_title="Gasto por mês!", page_icon="💵")

# Linha do tempo dos gastos
st.title("Linha do tempo dos gastos")

# Converter a coluna 'Data' para o formato datetime
base['Data'] = pd.to_datetime(base['Data'], format='%Y-%m-%d')

# Agrupar os gastos por data
gastos_por_data = base.groupby('Data')['Valor'].sum().reset_index()

# Criar o gráfico de linha

op = st.selectbox(
    'escolha o ano'
    , base['Data'].dt.year.unique()
)



fig = px.line(
    gastos_por_data,
    x='Data',
    y='Valor',
    title="Linha do Tempo dos Gastos",
    labels={'Data': 'Data', 'Valor': 'Valor (R$)'}
)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig, use_container_width=True)