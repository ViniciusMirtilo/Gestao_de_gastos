import pandas as pd
import streamlit as st

# Configuração da página
st.set_page_config(page_title="Gasto por mês!", page_icon="💵", layout="wide")

# Carregar os dados
base = pd.read_csv("c:/Users/Mirtilo/Downloads/py_panda/data/gasto.csv", encoding='latin-1')

# Converter a coluna 'Data' para o formato datetime
base['Data'] = pd.to_datetime(base['Data'], format='%Y-%m-%d', errors='coerce')

# Frases automáticas
st.markdown(f"<h3 style='text-align: center;'>Gastos totais: R$  {base['Categoria'].mode()[0]}</h3>", unsafe_allow_html=True)

# Extrair o nome do mês com maior gasto
mes_mais_gasto = base.groupby(base['Data'].dt.month)['Valor'].sum().idxmax()
mes_nome = pd.to_datetime(f"2023-{mes_mais_gasto}-01", format='%Y-%m-%d').strftime('%B')
st.markdown(f"<h3 style='text-align: center;'>Mês com mais gastos: {mes_nome}</h3>", unsafe_allow_html=True)

# Gasto médio mensal
st.markdown(f"<h3 style='text-align: center;'>Gasto médio mensal: R$ {base['Valor'].mean():.2f}</h3>", unsafe_allow_html=True)
