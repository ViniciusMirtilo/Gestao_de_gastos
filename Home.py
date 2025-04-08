import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="Meu Streamlit!", page_icon="📈")

st.image("./imagens/logo.png", width=200)
st.markdown("# Sobre o aplicativo:")
st.markdown(
        """
        <p>
            <ul>
                <li>Upload de arquivo .csv com o extrato bancário.<br></li>
                <li>Limpeza e tratamento dos dados.<br></li>
                <li>Classificação dos gastos por categorias.<br></li>
                <li>Mostrar dashboards com:<br></li>
                    <dd>
                        <li>Gastos totais por categoria.<br></li>
                        <li>Gráficos (barras, pizza, evolução mensal).<br></li>
                        <li>Insights importantes (ex: qual categoria mais gastou, qual mês mais gastou).<br></li>
                    </dd>
                <li>Interface agradável e organizada.<br></li>
                <li>Exibir os dados em um dataframe.<br></li>
            </ul>
        </p>
        
        <h1>Objetivo do App:</h1>
        
        <p style=''>
            <ul>
                <li>Upload de arquivo .csv com o extrato bancário.<br></li>
                <li>Limpeza e tratamento dos dados.<br></li>
                <li>Classificação dos gastos por categorias.<br></li>
                <li>Mostrar dashboards com:<br></d>
                    <dd>
                        <li>Gastos totais por categoria.<br></li>
                        <li>Gráficos (barras, pizza, evolução mensal).<br></li>
                        <li>Insights importantes (ex: qual categoria mais gastou, qual mês mais gastou).<br></li>
                    </dd>
                <li>Interface agradável e organizada.<br></li>
                <li>Exibir os dados em um dataframe.<br></li>
            </ul>
        </p>
        
        <h1>Como usar o app:</h1>
        
        ```sh
        git clone https://github.com/ViniciusMirtilo/py_panda.git
        ```
        
        <h1>Ferramentas utilizadas:</h1>
        
        <p style=''>
            <ul>
                <li>Python<br></li>
                <li>Pandas<br></li>
                <li>Streamlit<br></li>
            </ul>
        </p>
        
        <footer> 
            <p style='text-align: center; font-size: 12px; color: #888; margin-top: 20px;'>
                Desenvolvido por <a style="text-decoration:none;" href="https://github.com/ViniciusMirtilo">Mirtilo</a> - 2025
            </p>
        </footer>
        """,
        unsafe_allow_html=True
)
