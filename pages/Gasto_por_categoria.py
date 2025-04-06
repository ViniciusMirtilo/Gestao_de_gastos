import pandas as pd
import streamlit as st

# Filtros por categoria
# detalhamento -
# gráficos específicos.

#configuaracao da pagina
st.set_page_config(layout="wide")

# Carregar o arquivo CSV
base = pd.read_csv("c:/Users/Mirtilo/Downloads/py_panda/data/gasto.csv", encoding='latin-1')  #voce pode usar o encoding='latin-1' para evitar o erro de codificacao
df = pd.DataFrame(base)

st.write(" Gastos totais por categoria")
    
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