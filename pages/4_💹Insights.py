import pandas as pd
import streamlit as st

# Configuração da página
st.set_page_config(page_title="Insights", page_icon="💹", layout="wide")

# Carregar os dados
base = pd.read_csv("./data/gasto.csv", encoding='latin-1')

# Converter a coluna 'Data' para o formato datetime
base['Data'] = pd.to_datetime(base['Data'], format='%Y-%m-%d', errors='coerce')

# Frases automáticas
st.markdown(f"<h1 style='text-align: center; padding-bottom: 30px;'>Gastos totais</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center;'>R$ {base['Valor'].sum():.2f}</h2>", unsafe_allow_html=True)

#Tive que colocar essa parte do codigo pq o deploy do streamlit estava dando erro na antiga codificação
# e não estava reconhecendo o locale 'pt_BR.UTF-8'
meses_traduzidos = {
    "January": "Janeiro", "February": "Fevereiro", "March": "Março",
    "April": "Abril", "May": "Maio", "June": "Junho",
    "July": "Julho", "August": "Agosto", "September": "Setembro",
    "October": "Outubro", "November": "Novembro", "December": "Dezembro"
}

mes_mais_gasto = base.groupby(base['Data'].dt.month)['Valor'].sum().idxmax()

mes_nome = pd.to_datetime(f"2023-{mes_mais_gasto}-01", format='%Y-%m-%d').strftime('%B')

mes_mais_gastos_formatado = meses_traduzidos.get(mes_nome, mes_nome)

st.markdown(f"<h1 style='text-align: center; padding-top: 30px; padding-bottom: 30px;'>Mês com mais gastos</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center;'>{mes_mais_gastos_formatado}</h2>", unsafe_allow_html=True)

# Gasto médio mensal
st.markdown(f"<h1 style='text-align: center; padding-top: 30px; padding-bottom: 30px;'>Gasto médio mensal</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center;'>R$ {base['Valor'].mean():.2f}</h2>", unsafe_allow_html=True)