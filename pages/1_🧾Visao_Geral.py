import pandas as pd
import streamlit as st
import plotly.express as px
import locale

st.set_page_config(page_title="Visao Geral", page_icon="🧾", layout = "wide")

base = pd.read_csv("./data/gasto.csv", encoding='latin-1')  
df = pd.DataFrame(base)

col1 = st.columns(1) # espaço para 3 colunas

df['Data'] = pd.to_datetime(df['Data']).dt.strftime('%d/%m/%Y')

st.markdown("<h1 style='text-align: center; padding-bottom:30px;'>Visão Geral</h1>", unsafe_allow_html=True)

op = st.selectbox(
        'Escolhe uma data',
        df['Data'].unique()            
    )

st.markdown("<h1 style='text-align: center; padding-bottom:30px;'>Gastos totais por data</h1>", unsafe_allow_html=True)
gastos_por_data = df[df['Data'] == op]['Valor'].sum()
st.markdown(f"<h2 style='text-align: center;'>{gastos_por_data:.2f}</h2>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Gastos totais por categoria</h1>", unsafe_allow_html=True) 
grafico = df.groupby('Categoria')['Valor'].sum().sort_values(ascending=False)

fig = px.pie(
    grafico.reset_index(), 
    values='Valor', 
    names='Categoria', 
)
st.plotly_chart(fig)

st.markdown("<h1 style='text-align: center; padding-bottom:60px;'>Gastos totais por categoria (gráfico de barras)</h1>", unsafe_allow_html=True) 
gastos_por_categoria = df.groupby('Categoria')['Valor'].sum().sort_values(ascending=False)
st.bar_chart(gastos_por_categoria)

st.markdown("<h1 style='text-align: center; padding-bottom:60px;'>Evolução mensal</h1>", unsafe_allow_html=True) 

gastos_totais = df['Valor'].sum()

df['Mes'] = pd.to_datetime(df['Data'], format='%d/%m/%Y').dt.to_period('M')  
mes_mais_gastos = df.groupby('Mes')['Valor'].sum().idxmax()
valor_mes_mais_gastos = df.groupby('Mes')['Valor'].sum().max()

#Tive que colocar essa parte do codigo pq o deploy do streamlit estava dando erro na antiga codificação
# e não estava reconhecendo o locale 'pt_BR.UTF-8'
meses_traduzidos = {
    "January": "Janeiro", "February": "Fevereiro", "March": "Março",
    "April": "Abril", "May": "Maio", "June": "Junho",
    "July": "Julho", "August": "Agosto", "September": "Setembro",
    "October": "Outubro", "November": "Novembro", "December": "Dezembro"
}

# Formatar o mês manualmente
mes_mais_gastos_formatado = mes_mais_gastos.start_time.strftime('%B de %Y')
mes_mais_gastos_formatado = ' '.join([meses_traduzidos.get(mes_mais_gastos_formatado.split()[0], mes_mais_gastos_formatado.split()[0]), mes_mais_gastos_formatado.split()[2]])

categoria_mais_cara = df.groupby('Categoria')['Valor'].sum().idxmax()
valor_categoria_mais_cara = df.groupby('Categoria')['Valor'].sum().max()

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.metric(label="Gastos Totais", value=f"R$ {gastos_totais:.2f}")

with col2:
    st.metric(label="Mês com Mais Gastos", value=mes_mais_gastos_formatado, delta=f"R$ {valor_mes_mais_gastos:.2f}")

with col3:
    st.metric(label="Categoria Mais Cara", value=categoria_mais_cara, delta=f"R$ {valor_categoria_mais_cara:.2f}")