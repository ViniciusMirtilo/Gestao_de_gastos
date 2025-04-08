# Controle de Gastos Pessoais 💸

[![Open in Streamlit][share_badge]][share_link]

Este repositório contém o código-fonte de um projeto para controle e análise de gastos pessoais, utilizando Python, Pandas e Streamlit.

> **Atenção:** Este projeto foi desenvolvido para fins educacionais e de portfólio. Os dados utilizados são fictícios.

## 📌 Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto
- **Pandas**: Manipulação e análise dos dados
- **Streamlit**: Criação do dashboard interativo
- **Git/GitHub**: Versionamento de código

## 📂 Estrutura do Projeto

```
📂 projeto_gastos
│—— app.py                 # Arquivo principal da aplicação
│—— requirements.txt       # Dependências do projeto
│—— README.md              # Documentação do projeto
│
│📂 data                # Arquivos de dados CSV
│     └— gastos.csv       # Dados fictícios utilizados
│
│📂 pages               # Múltiplas páginas do Streamlit
│     ├— 1_Visao_Geral.py
│     ├— 2_Gastos_por_Categoria.py
│     ├— 3_Gastos_por_Mes.py
│     └— 4_Insights.py
```

## 🎯 Funcionalidades Implementadas

- **Upload de arquivos CSV** com informações de gastos
- **Dashboard interativo** com múltiplas páginas:
  - Visão geral dos gastos
  - Gastos por categoria
  - Gastos por mês
  - Geração de insights automáticos
- **Filtros** por período e categoria
- **Exportação** de dados filtrados
- Interface intuitiva e responsiva

## 💻 Como Executar o Projeto

1. Faça o download ou clone este repositório:

```sh
git clone https://github.com/ViniciusMirtilo/Gestao_de_gastos.git
```

2. Instale as dependências:

```sh
pip install -r requirements.txt
```

3. Execute o projeto:

```sh
streamlit run app.py
```

## 📞 Contato

Caso tenha dúvidas ou sugestões, sinta-se à vontade para abrir uma *issue* no repositório.

**Repositório no GitHub**: [Projeto de Controle de Gastos pessoais](https://github.com/ViniciusMirtilo/Gestao_de_gastos.git)

[share_badge]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[share_link]: https://share.streamlit.io/okld/streamlit-gallery/main?p=elements

