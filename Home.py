import streamlit as st
import time
import numpy as np
# from st_pages import Page, Section, show_pages, add_page_title, hide_pages

st.set_page_config(page_title="Meu Streamlit!", page_icon="📈")

# show_pages(
#     [
#         Page("home.py", "Home"),
#         Page("pages/1_Geral.py", "Geral"),
#         Page("pages/2_Gasto_por_categoria.py", "Gasto por categoria"),
#         Page("pages/3_Gasto_por_mes.py", "Gasto por mês"),
#         Page("pages/Insights.py", "Insights"),
#     ]
# )

st.markdown("## 📈 Meu primeiro aplicativo Streamlit! 📉")
st.markdown("# Sobre o aplicativo:")
st.markdown(
    """
    - Upload de arquivo .csv com o extrato bancário.
    - Limpeza e tratamento dos dados.
    - Classificação dos gastos por categorias.
    - Mostrar dashboards com:
        - Gastos totais por categoria.
        - Gráficos (barras, pizza, evolução mensal).
        - Insights importantes (ex: qual categoria mais gastou, qual mês mais gastou).
    - Interface agradável e organizada.
    
    # Objetivo do App:
    - Upload de arquivo .csv com o extrato bancário.
    - Limpeza e tratamento dos dados.
    - Classificação dos gastos por categorias.
    - Mostrar dashboards com:
        - Gastos totais por categoria.
        - Gráficos (barras, pizza, evolução mensal).
        - Insights importantes (ex: qual categoria mais gastou, qual mês mais gastou).
    - Interface agradável e organizada.
    - Exibir os dados em um dataframe.  
    
    Repositorio no Github:
    ```sh
        git clone https://github.com/ViniciusMirtilo/py_panda.git
    ```

    Ferramentas utilizadas:
    - Python 
    - Pandas
    - Streamlit
    """
    
)
