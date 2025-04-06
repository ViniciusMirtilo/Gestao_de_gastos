import pandas as pd
import streamlit as st
import plotly.express as px
import locale

# Visão Geral	
# Total de gastos, -
# gráficos de pizza -
# barras, KPIs principais.-


base = pd.read_csv("c:/Users/Mirtilo/Downloads/py_panda/data/gasto.csv", encoding='latin-1')  #voce pode usar o encoding='latin-1' para evitar o erro de codificacao
df = pd.DataFrame(base)

col1 = st.columns(1) # espaço para 3 colunas

df['Data'] = pd.to_datetime(df['Data']).dt.strftime('%d/%m/%Y')

st.write("# Visão Geral") # Titulo da pagina

op = st.selectbox(
        'Escolhe uma data',
        df['Data'].unique()            
    )

st.write("# Gastos totais por data") # Exibe os gastos totais por data
gastos_por_data = df[df['Data'] == op]['Valor'].sum()
st.write(f"### Total gastos R$ {gastos_por_data:.2f}")

st.write("## Grafico") # Exibe os gastos totais por categoria
grafico = df.groupby('Categoria')['Valor'].sum().sort_values(ascending=False)

fig = px.pie(
    grafico.reset_index(), 
    values='Valor', 
    names='Categoria', 
)
st.plotly_chart(fig)

st.write("# Graficos de barras") # Exibe os gastos totais por categoria
gastos_por_categoria = df.groupby('Categoria')['Valor'].sum().sort_values(ascending=False)
st.bar_chart(gastos_por_categoria)

# kpis principais gastos totais, mes mais gastos, categoria mais caras
st.write("# KPIs principais") # Exibe os gastos totais por categoria

# KPI 1: Total de gastos
gastos_totais = df['Valor'].sum()

# KPI 2: Mês com mais gastos
df['Mes'] = pd.to_datetime(df['Data'], format='%d/%m/%Y').dt.to_period('M')  # Extrai o mês
mes_mais_gastos = df.groupby('Mes')['Valor'].sum().idxmax()
valor_mes_mais_gastos = df.groupby('Mes')['Valor'].sum().max()

# Configurar o locale para português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# Formatar o mês no padrão brasileiro
mes_mais_gastos_formatado = mes_mais_gastos.start_time.strftime('%B de %Y')  # Exemplo: "Março de 2025"

# KPI 3: Categoria mais cara
categoria_mais_cara = df.groupby('Categoria')['Valor'].sum().idxmax()
valor_categoria_mais_cara = df.groupby('Categoria')['Valor'].sum().max()

# Exibição dos KPIs no Streamlit
st.metric(label="Gastos Totais", value=f"R$ {gastos_totais:.2f}")
st.metric(label="Mês com Mais Gastos", value=mes_mais_gastos_formatado, delta=f"R$ {valor_mes_mais_gastos:.2f}")
st.metric(label="Categoria Mais Cara", value=categoria_mais_cara, delta=f"R$ {valor_categoria_mais_cara:.2f}")

