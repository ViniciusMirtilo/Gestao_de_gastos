import pandas as pd
import streamlit as st
import plotly.express as px

# Filtros por categoria-
# detalhamento -
# gráficos específicos.

#configuaracao da pagina
st.set_page_config(layout="wide")

# Carregar o arquivo CSV
base = pd.read_csv("c:/Users/Mirtilo/Downloads/py_panda/data/gasto.csv", encoding='latin-1')  #voce pode usar o encoding='latin-1' para evitar o erro de codificacao
df = pd.DataFrame(base)

st.write("# Gastos totais por categoria")
    
op1 = st.selectbox(
        'Escolhe uma Categoria',
        df['Categoria'].unique()            
)
    
gastos_por_categoria = df[df['Categoria'] == op1]['Valor'].sum()
st.write(f"Total gastos R$ {gastos_por_categoria:.2f}")


st.write("Detalhamento dos gastos por categoria")
# Exibe os gastos totais por categoria
Detalhamento = df[df['Categoria'] == op1][['Data', 'Descricao', 'Valor']]
st.write(Detalhamento)


#graficos especificos 

st.write("Graficos especificos")

op2 = st.selectbox(
        'Escolhe um grafico',
        ['Grafico de pizza', 'Grafico de barras']
)

if op2 == 'Grafico de pizza':
    grafico = df[df['Categoria'] == op1].groupby('Descricao')['Valor'].sum().sort_values(ascending=False)
    fig = px.pie(
        grafico.reset_index(), 
        values='Valor', 
        names='Descricao', 
        title=f"Gastos por Descrição na Categoria {op2}",
    )
    st.plotly_chart(fig)
elif op2 == 'Grafico de barras':
    grafico = df[df['Categoria'] == op1].groupby('Descricao')['Valor'].sum().sort_values(ascending=False)
    fig = px.bar(
        grafico.reset_index(),
        x='Valor',
        y='Descricao',
        orientation='h',  # Define o gráfico como horizontal
        title=f"Gastos por Descrição na Categoria {op}"
    )
    st.plotly_chart(fig)