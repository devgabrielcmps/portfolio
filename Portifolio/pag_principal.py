#Portifolio com meus projetos 
# streamlit run Projetos2024\Portifolio\pag_principal.py
import sys
import os
import streamlit as st
import prev_temp as pt  

# Aplicando CSS para mudar a fonte do texto
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap');
    
    .titulo {
        font-family: 'Open Sans', Courier, monospace;
        font-size: 50px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def home_page():
    st.markdown("<h1 class='titulo' style='text-align: left;'>🐍 Portfolio </h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        Welcome to my portfolio. My name is Gabriel Campos, and I am a technician in industrial automation and a systems development student. This portfolio contains some of the projects I have been developing to apply my knowledge. In the sidebar on the left, you can find some of my projects, all developed in Python.
        """, unsafe_allow_html=True)

        st.markdown("""
        GitHub: https://github.com/devgabrielcmps \n
        Linkedin: https://www.linkedin.com/in/gabrielcamposdev/
        """, unsafe_allow_html=True)
       
    with col2:
         st.image("Projetos2024/Portifolio/image2.png", width=150)

        

def sidebar():
    st.sidebar.image("Projetos2024/Portifolio/image3.png", width=70)
    st.sidebar.title('Projects')

    if st.sidebar.button('📈 Quotes'):
        # Adicione a lógica para a página de cotações aqui
        st.session_state.page = 'quotes'
    
    if st.sidebar.button('🌤️ Weather Forecast'):
        # Redireciona para a página de previsão do tempo
        st.session_state.page = 'previsao_tempo'

    if st.sidebar.button('🛢 CRUD'):
        # Redireciona para a página de previsão do tempo
        st.session_state.page = 'crud'

    if st.sidebar.button('🌐 CEP'):
        # Redireciona para a página de previsão do tempo
        st.session_state.page = 'cep'

    st.sidebar.text('\n\n')
    if st.sidebar.button('🏠 Return Home'):
        # Adicione a lógica para a página de cotações aqui
        st.session_state.page = 'home'

def previsao_tempo():
  pt.run()
  st.markdown("<h1 class='titulo' style='text-align: left;'> About the Project</h1>", unsafe_allow_html=True)
  st.markdown("""
  I developed a weather forecast project using Streamlit and the OpenWeather API. With this app, I can check the weather forecast for any city. By entering the city's name, the app provides me with information about the current temperature and the five-day forecast, including icons and descriptions of weather conditions.
  I used Streamlit to create an interactive interface, Requests to make API requests, and Datetime to handle dates and times. This project offers a practical and visually appealing solution for checking weather information.
            """, unsafe_allow_html=True)

def quotes():
  st.markdown("<h1 class='titulo' style='text-align: left;'> About the Project</h1>", unsafe_allow_html=True)
  st.markdown("""
    💼 Desenvolvimento de Aplicativo de Conversão de Moedas 💱
              
    Link do Codigo: https://github.com/devgabrielcmps 

    Desenvolvi essa aplicação envolvendo customTKinter e API da AwesomeAPI para colocar em prática os conceitos que venho estudando e para enriquecer meu portifólio. O projeto consiste em um aplicativo de conversão de moedas, criado para simplificar a vida de quem precisa acompanhar cotações e realizar conversões rapidamente.

    🔧 Tecnologias Utilizadas:

    API de cotações: Utilizei a AwesomeAPI para obter as taxas de câmbio em tempo real.\n
    Requests e JSON: Para fazer as requisições à API e interpretar as respostas.\n
    Datetime: Para capturar a data e hora atual de cada conversão.\n
    CustomTkinter: Utilizado para construir uma interface gráfica intuitiva e interativa.\n
    Matplotlib: Responsável por gerar gráficos das variações das cotações nos últimos 30 dias.\n
    📂 Conceitos Aplicados: Durante o desenvolvimento, coloquei em prática conceitos essenciais como packages, módulos, funções e tratamento de erros, garantindo uma organização sólida e manutenção facilitada.

    📋 Principais Funcionalidades:

    O aplicativo inicia pelo script IniciaApp, que carrega a janela principal.
    O usuário pode selecionar uma moeda para conversão e visualizar o nome da moeda, a data e hora atuais.
    Campos de conversão permitem transformar valores entre reais e a moeda escolhida, com validação de entrada de dados para prevenir erros.
    Um gráfico com as últimas 30 cotações é gerado automaticamente ao clicar em um botão.\n
              
    📂 Estrutura do Projeto:\n
    hora: Responsável por obter a data e hora.\n
    cotacao: Módulo para obter as cotações das moedas.\n
    janelaPrincipal: Controla o layout e navegação do app.\n
    Pasta moedas: Contém arquivos individuais para cada moeda, facilitando a manutenção do código.\n
    🔄 Melhorias Futuras: Embora o projeto já tenha cumprido seu objetivo inicial, planejo aprimorar a aplicação com novas funcionalidades, como a inclusão de mais moedas, melhorias nos tratamentos de erros, e otimizações na navegação para evitar a abertura de várias janelas simultâneas.
            """, unsafe_allow_html=True)
  
  st.image("Projetos2024/Portifolio/01.png", width=1000)
  

def crud():
    st.text('Em desenvolvimento')

def cep():
    st.text('Em desenvolvimento')


# Inicializa o estado da página se não estiver presente
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Define a barra lateral
sidebar()

# Exibe o conteúdo da página selecionada
if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'previsao_tempo':
    previsao_tempo()
elif st.session_state.page == 'quotes':
    quotes()
