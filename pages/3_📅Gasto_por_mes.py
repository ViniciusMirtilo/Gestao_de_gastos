import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Gasto por mês", page_icon="📅", layout='wide')

base = pd.read_csv("./data/gasto.csv", encoding='latin-1')  # voce pode usar o encoding='latin-1' para evitar o erro de codificacao

st.markdown("<h1 style='text-align: center; padding-bottom:30px;'>Linha do tempo dos gastos</h1>", unsafe_allow_html=True)

base['Data'] = pd.to_datetime(base['Data'], format='%Y-%m-%d')

gastos_por_data = base.groupby('Data')['Valor'].sum().reset_index()

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

st.plotly_chart(fig, use_container_width=True)

st.markdown("<h1 style='text-align: center; padding-bottom:30px;'>Comparação de gastos por mês</h1>", unsafe_allow_html=True)

gastos_por_mes = base[base['Data'].dt.year == op].groupby(base['Data'].dt.month)['Valor'].sum().reset_index()

gastos_por_mes.columns = ['Mês', 'Valor']

gastos_por_mes['Mês'] = gastos_por_mes['Mês'].apply(lambda x: pd.to_datetime(f'2023-{x}-01', format='%Y-%m-%d').strftime('%B'))

fig = px.bar(
    gastos_por_mes,
    x='Mês',
    y='Valor',
    title=f"Gastos por Mês no Ano {op}",
    labels={'Mês': 'Mês', 'Valor': 'Valor (R$)'},
    text='Valor'
)

st.plotly_chart(fig, use_container_width=True)