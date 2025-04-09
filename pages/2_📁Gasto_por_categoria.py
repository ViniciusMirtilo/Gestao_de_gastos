import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Gastos por Categorias", page_icon="📁", layout = "wide")

st.markdown(
    """
    <style>
    .center-table {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    table {
        margin: 0 auto; /* Centraliza a tabela */
        border-collapse: collapse;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

base = pd.read_csv("./data/gasto.csv", encoding='latin-1')  #voce pode usar o encoding='latin-1' para evitar o erro de codificacao
df = pd.DataFrame(base)

st.markdown("<h1 style='text-align: center; padding-bottom:30px;'>Gastos totais por categoria</h1>", unsafe_allow_html=True)
    
op1 = st.selectbox(
        'Escolhe uma Categoria',
        df['Categoria'].unique()            
)
    
gastos_por_categoria = df[df['Categoria'] == op1]['Valor'].sum()
st.markdown(f"<h2 style='text-align: center;'>Gastos totais: R$ {gastos_por_categoria:.2f}</h2>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; padding-bottom:30px;'>Detalhamento dos gastos por categoria</h1>", unsafe_allow_html=True)

Detalhamento = df[df['Categoria'] == op1][['Data', 'Descricao', 'Valor']]

html_detalhamento = Detalhamento.to_html(escape=False, index=False)

st.markdown(f'<div class="center-table">{html_detalhamento}</div>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; padding-bottom:30px;'>Graficos especificos</h1>", unsafe_allow_html=True)

op2 = st.selectbox(
        'Escolhe um grafico',
        ['Grafico de pizza', 'Grafico de barras', 'Grafico de linhas']
)

if op2 == 'Grafico de pizza':
    grafico = df[df['Categoria'] == op1].groupby('Descricao')['Valor'].sum().sort_values(ascending=False)
    fig = px.pie(
        grafico.reset_index(), 
        values='Valor', 
        names='Descricao',
    )
    st.plotly_chart(fig)
elif op2 == 'Grafico de barras':
    grafico = df[df['Categoria'] == op1].groupby('Descricao')['Valor'].sum().sort_values(ascending=False)
    fig = px.bar(
        grafico.reset_index(),
        x='Valor',
        y='Descricao',
        orientation='h',
    )
    st.plotly_chart(fig)
elif op2 == 'Grafico de linhas':
    grafico = df[df['Categoria'] == op1].groupby('Descricao')['Valor'].sum().sort_values(ascending=False)
    fig = px.line(
        grafico.reset_index(),
        x='Descricao',
        y='Valor',
    )
    st.plotly_chart(fig)